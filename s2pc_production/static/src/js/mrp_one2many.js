odoo.define('s2pc_production.mrp_one2many', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var core = require('web.core');
var field_registry = require('web.field_registry');
var field_utils = require('web.field_utils');
var relational_field = require('web.relational_fields');
var ListRenderer = require('web.ListRenderer');
var dom = require('web.dom');
const { sprintf, toBoolElse } = require("web.utils");

var QWeb = core.qweb;
var _t = core._t;


var MrpListRenderer = ListRenderer.extend({

    init: function(parent, state, params){
        this._super.apply(this, arguments);
        this.group = params.group;
        this.referred = params.referred;
        this.selected_reference = false;
        this.parent_tmp = parent;
    },
    _get_filtered_rows: function(reference_id){
        return this.state.data.filter( line => line.data[this.group].res_id == parseInt(reference_id))
    },

    _get_unassigned_rows: function(){
        return this.state.data.filter( line => !line.data[this.group])
    },

    _addQuickCreateRow: function(reference){

        if (this.addCreateLine && this.parent_tmp.mode == 'edit') {
            var $tr = $('<tr>');
            var colspan = this._getNumberOfCols();
            if (this.handleField) {
                colspan = colspan - 1;
                $tr.append('<td>');
            }
            var $td = $('<td>')
                .attr('colspan', colspan)
                .addClass('o_field_x2many_list_row_add');
            $tr.append($td);

            if (this.addCreateLine) {
                _.each(this.creates, function (create, index) {
                    var $a = $('<a href="#" role="button">')
                        .attr('data-context', create.context)
                        .attr('reference', reference)
                        .text(create.string)
                        .addClass('o_field_x2many_list_row_add')
                        .addClass('bonjour-bonjour');
                    if (index > 0) {
                        $a.addClass('ml16');
                    }
                    $td.append($a);
                });
            }
            return $tr
        }
    },

    _renderRows: function () {
        var self = this;
        var result = [];
        if(this.referred.length){
            _.each(self.referred, function(ref){
                var filtered_data = self._get_filtered_rows(ref[0]);
                var $tr = $('<tr>', { class: 'referred-operation-id', style: 'background: aliceblue'})
                            .attr('data-id', ref[0])
                            .append($('<td>').attr('colspan', self.columns.length + 1)
                            .append($('<strong>').text(ref[1] + ' (' + filtered_data.length + ')')));
                result.push($tr);
                result = $.merge(result, filtered_data.map(self._renderRow.bind(self)))
                result.push(self._addQuickCreateRow(ref[0]))
            })
            var unassigned_data = self._get_unassigned_rows();
            if(unassigned_data.length > 0){
                var $tr = $('<tr>', { class: 'referred-operation-id', style: 'background: aliceblue'})
                            .attr('data-id', false)
                            .append($('<td>').attr('colspan', self.columns.length + 1)
                            .append($('<strong>').text('Non assigné' + ' (' + unassigned_data.length + ')')));
                result.push($tr);
                result = $.merge(result, unassigned_data.map(self._renderRow.bind(self)))
                result.push(self._addQuickCreateRow(false))
            }
        }
        else{
            return this._super()
        }
        return result
    },

    _onAddRecord: function (ev) {
        ev.preventDefault();
        ev.stopPropagation();
        var self = this;
        var def = new Promise(function(resolve){
            self.selected_reference = $(ev.target).attr('reference');
            self.parent_tmp.optional_reference = $(ev.target).attr('reference');
            resolve();
        });
        return def.then(function(){
            self.unselectRow().then(function () {
                self.trigger_up('add_record', {context: ev.currentTarget.dataset.context && [ev.currentTarget.dataset.context]});
            })
        })

    },
    setRowMode: function (recordID, mode){
        var self= this;
        return this._super.apply(this, arguments).then(function(){
              var reference = self.selected_reference || self.parent_tmp.optional_reference;
              var target = $("a[reference='"+reference+"']").closest('tr');
              var record = self._getRecord(recordID);
              if(record.isNew() && $.inArray(recordID, self.parent_tmp.added_line) < 0){
                    $('.o_selected_row').insertBefore(target);
                    self.trigger_up('edited_list', { id: self.parent_tmp.value.id });
              }
        })
    },
    confirmChange: function (state, recordID) {
        var self = this;
        return this._super.apply(this, arguments).then(function (widgets) {
            self.parent_tmp.added_line.push(recordID)
        });
    },

    confirmUpdate: function (state, id, fields, ev) {
        var self = this;

        var oldData = this.state.data;
        return this.confirmChange(state, id, fields, ev).then(function () {
            // If no record with 'id' can be found in the state, the
            // confirmChange method will have rerendered the whole view already,
            // so no further work is necessary.
            var record = self._getRecord(id);
            if (!record) {
                return;
            }
            _.each(oldData, function (rec) {
                if (rec.id !== id) {
                    // update modifiers of the other rows for the upcoming rendering
                    self._updateAllModifiers(rec);
                    // destroy the widgets of the other rows as new ones will be instantiated
                    self._destroyFieldWidgets(rec.id);
                }
            });

             // Keep ref of the current row's widgets
             const currentRowFieldWidgets = self.allFieldWidgets[id];
             // Remove it from the list just for a clean start for generating the new content (avoid later memory leak)
             delete self.allFieldWidgets[id];

            // re-render whole body (outside the dom)
            self.defs = [];
            var $newBody = self._renderBody();
            var defs = self.defs;
            delete self.defs;

            return Promise.all(defs).then(function () {
                // All the field widgets have now be recreated, but we don't want the current row's ones.
                // We destroy it and get it back from our reference.
                // This manipulation avoids a memory leak, where field widgets in the current row wouldn't be destroyed and were kept in memory.
                self._destroyFieldWidgets(id);
                self.allFieldWidgets[id] = currentRowFieldWidgets;

                // update registered modifiers to edit 'mode' because the call to
                // _renderBody set baseModeByRecord as 'readonly'
                _.each(self.columns, function (node) {
                    self._registerModifiers(node, record, null, {mode: 'edit'});
                });

                // store the selection range to restore it once the table will
                // be re-rendered, and the current cell re-selected
                var currentRowID;
                var currentWidget;
                var focusedElement;
                var selectionRange;
                if (self.currentRow !== null) {
                    currentRowID = self._getRecordID(self.currentRow);
                    currentWidget = self.allFieldWidgets[currentRowID][self.currentFieldIndex];
                    if (currentWidget) {
                        focusedElement = currentWidget.getFocusableElement().get(0);
                        if (currentWidget.formatType !== 'boolean' && focusedElement) {
                            selectionRange = dom.getSelectionRange(focusedElement);
                        }
                    }
                }

                // remove all data rows except the one being edited, and insert
                // data rows of the re-rendered body before and after it
                var $editedRow = self._getRow(id);
                $editedRow.nextAll('tr').remove();
                $editedRow.prevAll('tr').remove();
                var $newRow = $newBody.find('.o_data_row[data-id="' + id + '"]');
                $newRow.prevAll('tr').get().reverse().forEach(function (row) {
                    $(row).insertBefore($editedRow);
                });
                $newRow.nextAll('tr').get().reverse().forEach(function (row) {
                    $(row).insertAfter($editedRow);
                });

                var reference = self.selected_reference || self.parent_tmp.optional_reference;
                var target = $("a[reference='"+reference+"']").closest('tr');
                if(target && $('.o_selected_row')){
                    $('.o_selected_row').insertBefore(target);
                    self.trigger_up('edited_list', { id: self.parent_tmp.value.id });
                }


                // Call on_attach_callback methods on widgets that implement it
                if (self._isInDom) {
                    for (const handle in self.allFieldWidgets) {
                        if (handle !== id) {
                            self.allFieldWidgets[handle].forEach(widget => {
                                if (widget.on_attach_callback) {
                                    widget.on_attach_callback();
                                }
                            });
                        }
                    }
                }

                if (self.currentRow !== null) {
                    var newRowIndex = $editedRow.prop('rowIndex') - 1;
                    self.currentRow = newRowIndex;
                    return self._selectCell(newRowIndex, self.currentFieldIndex, {force: true})
                        .then(function () {
                            // restore the selection range
                            currentWidget = self.allFieldWidgets[currentRowID][self.currentFieldIndex];
                            if (currentWidget) {
                                focusedElement = currentWidget.getFocusableElement().get(0);
                                if (selectionRange) {
                                    dom.setSelectionRange(focusedElement, selectionRange);
                                }
                            }
                        });
                }
            });
        });
    },


});

var MrpOne2many = relational_field.FieldOne2Many.extend({
    events: _.extend({}, relational_field.FieldOne2Many.prototype.events, {
        'click .bonjour-bonjour': '_set_reference',

    }),
    init: function () {
        this._super.apply(this, arguments);
        this.group = this.nodeOptions.group;
        this.referred = this.nodeOptions.referred;
        this.optional_reference = false;
        this.added_line = [];

    },

    _getRenderer: function () {
        if (this.view.arch.tag === 'tree') {
            return MrpListRenderer;
        }
        else{
            this._super.apply(this, arguments)
        }
    },
    _set_reference: function(ev){
        ev.preventDefault();
        this.optional_reference = $(ev.target).attr('reference')
    },

    _onAddRecord: function (ev) {
        const data = ev.data || {};
        // we don't want interference with the components upstream.
        ev.stopPropagation();
        if (this._canQuickEdit && this.isReadonly) {
            this.trigger_up('quick_edit', {
                fieldName: this.name,
                target: this.el,
                extraInfo: { type: 'add', data },
            });
        } else {
            var context= {};
            context['default_' + this.group] = parseInt(this.optional_reference || false);
            data.context = [];
            data.context.push(context);
            this._addCreateRecordRow(data);
        }
    },

    _render: function () {
        var self = this;
        if (!this.view) {
            return this._super();
        }
        if (this.renderer) {
            this.currentColInvisibleFields = this._evalColumnInvisibleFields();
            return this.renderer.updateState(this.value, {
                addCreateLine: this._hasCreateLine(),
                addTrashIcon: this._hasTrashIcon(),
                columnInvisibleFields: this.currentColInvisibleFields,
                keepWidths: true,
            }).then(() => {
                return this._updateControlPanel({ size: this.value.count });
            });
        }
        var arch = this.view.arch;
        var viewType;
        var rendererParams = {
            arch: arch,
        };

        if (arch.tag === 'tree') {
            viewType = 'list';
            this.currentColInvisibleFields = this._evalColumnInvisibleFields();
            _.extend(rendererParams, {
                editable: this.mode === 'edit' && arch.attrs.editable,
                addCreateLine: this._hasCreateLine(),
                addTrashIcon: this._hasTrashIcon(),
                isMany2Many: this.isMany2Many,
                no_open: ((this.isReadonly && !this.hasReadonlyModifier) &&
                    this._canQuickEdit) || toBoolElse(arch.attrs.no_open || '', false),
                columnInvisibleFields: this.currentColInvisibleFields,
            });
        }

        if (arch.tag === 'kanban') {
            viewType = 'kanban';
            var record_options = {
                editable: false,
                deletable: false,
                read_only_mode: this.isReadonly,
            };
            _.extend(rendererParams, {
                record_options: record_options,
                readOnlyMode: this.isReadonly,
            });
        }

        _.extend(rendererParams, {
            viewType: viewType,
        });

        _.extend(rendererParams,{
            group: this.group,
            referred: _.map(this.__parentedParent.state.data[this.referred].data, function(ref){
                if(ref){
                    return [ref.data.id, ref.data.name]
                }
                return []
            }),

        });

        const Renderer = this._getRenderer();
        this.renderer = new Renderer(this, this.value, rendererParams);

        this.$el.addClass('o_field_x2many o_field_x2many_' + viewType);
        if (this.renderer) {
            return this.renderer.appendTo(document.createDocumentFragment()).then(function () {
                dom.append(self.$el, self.renderer.$el, {
                    in_DOM: self.isInDOM,
                    callbacks: [{widget: self.renderer}],
                });
            });
        } else {
            return this._super();
        }
    },

});

field_registry.add('mrp_one2many', MrpOne2many);

return {
    MrpOne2many: MrpOne2many
};


});
