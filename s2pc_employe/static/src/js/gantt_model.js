odoo.define('s2pc_employe.GanttModel', function (require) {
'use strict';

    const GanttModel = require('web_gantt.GanttModel');

    const HrLeaveTeamModel = GanttModel.extend({

        init: function () {
            var self=this;
            this._super.apply(this, arguments);
            this._rpc({
                model: 'hr.leave',
                method: 'get_current_user_employee_team',
            }).then(function(result) {
                self.team_employees = result;
            });
        },

        _generateRows(params) {
            const { groupedBy, groups, oldRows, parentPath, records } = params;
            if(groupedBy.includes("employee_id")){
                groupedBy.splice(groupedBy.length - 1, 0, groupedBy.splice(groupedBy.indexOf("employee_id"), 1)[0]);
                params.groupedBy = groupedBy;
            }
            var rows = this._super(params);
            if(groupedBy.length == 1 && groupedBy[0] == "employee_id"){
                this._createEmptyRow(rows, params);
            }

            return rows;
        },

        _createEmptyRow: function(rows, params){
            var self = this;
            const { groupedBy, groups, oldRows, parentPath, records } = params;
            const groupLevel = this.ganttData.groupedBy.length - groupedBy.length;
            _.each(this.team_employees, function(emp){
                var existing_row = _.filter(rows, function(row){
                    return row.resId == emp.id
                })
                if(!existing_row.length){
                    const part = {};
                    part['employee_id'] = [emp.id, emp.name];
                    const groupedByField = groupedBy[0];
                    const path = [...parentPath, part];
                    const id = JSON.stringify(path);
                    const resId = emp.id;
                    const minNbGroups = self.collapseFirstLevel ? 0 : 1;
                    const isGroup = groupedBy.length > minNbGroups;
                    const row = {
                        name: self._getRowName(groupedByField, emp.name),
                        groupedBy,
                        groupedByField,
                        groupLevel,
                        id,
                        resId,
                        isGroup: false,
                        fromServer: true,
                        isOpen: true,
                        records: [],
                    };

                    rows.push(row);

                }

            })

        },

    })

    return HrLeaveTeamModel

});

