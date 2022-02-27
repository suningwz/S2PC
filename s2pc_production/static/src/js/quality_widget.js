odoo.define('s2pc_production.mrp_quality', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var core = require('web.core');
var field_registry = require('web.field_registry');
var field_utils = require('web.field_utils');

var QWeb = core.qweb;
var _t = core._t;

var ShowMrpQualityWidget = AbstractField.extend({
    events: _.extend({
        'click .open_record': '_open_record'
    }, AbstractField.prototype.events),
    supportedFieldTypes: ['char'],

    isSet: function() {
        return true;
    },

    _render: function() {
        var self = this;
        var info = JSON.parse(this.value);
        if (!info) {
            this.$el.html('');
            return;
        }
        this.$el.html(QWeb.render('MrpQualityWidget', {
            header_check: self._get_check_header(),
            header_alert: self._get_alert_header(),
            check_lines: self._get_check_lines(),
            alert_lines: self._get_alert_lines(),
        }));
    },
    _get_check_header: function(){
        var data = JSON.parse(this.value);
        return data.header_check
    },
    _get_alert_header: function(){
        var data = JSON.parse(this.value);
        return data.header_alert
    },
    _get_check_lines: function(){
        var self = this;
        var result = [];
        var data = JSON.parse(this.value);
        var data_check = data.work_check;
        var operation_column = []
        _.each(data_check, function(line, key){
            for(var i = 0; i < line.length; i++){
                result.push({'work': operation_column.indexOf(key) < 0 ? key : '',
                     'measure_on':line[i].measure_on,
                     'workcenter_id': line[i].workcenter_id,
                     'point_id': line[i].point_id,
                     'additional_note': line[i].additional_note,
                     'quality_state': line[i].quality_state,
                     'id': line[i].id,
                })
                operation_column.push(key);
            }
        });
        return result

    },
    _get_alert_lines: function(){
        var self = this;
        var result = [];
        var data = JSON.parse(this.value);
        var data_alert = data.work_alert;
        var operation_column = []
        _.each(data_alert, function(line, key){
            for(var i = 0; i < line.length; i++){
                result.push({'work': operation_column.indexOf(key) < 0 ? key : '',
                     'name':line[i].name,
                     'workcenter_id': line[i].workcenter_id,
                     'user_id': line[i].user_id,
                     'reason_id': line[i].reason_id,
                     'stage_id': line[i].stage_id,
                     'description': line[i].description,
                     'id': line[i].id,
                })
                operation_column.push(key);
            }
        });
        return result

    },
    _open_record: function(ev){
        var self=this;
        this.do_action({
                type: 'ir.actions.act_window',
                res_model: ev.target.getAttribute('model'),
                views: [[false, 'form']],
                res_id: parseInt(ev.target.getAttribute('id')),
                target: 'new',
                flags: {mode: 'edit'},
            },{
                on_close: function () {
                    self.trigger_up('reload');
            }});
    },
});

field_registry.add('mrp_quality_widget', ShowMrpQualityWidget);

return {
    ShowMrpQualityWidget: ShowMrpQualityWidget
};

});
