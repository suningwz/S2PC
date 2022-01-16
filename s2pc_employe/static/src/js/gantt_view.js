odoo.define('s2pc_employe.GanttView', function (require) {
'use strict';

    const view_registry = require('web.view_registry');
    const HrLeaveTeamGanttModel = require('s2pc_employe.GanttModel')
    const HrGantt = require('hr_gantt.GanttView');

    const HrLeaveTeamGanttView = HrGantt.extend({
        config: Object.assign({}, HrGantt.prototype.config, {
            Model: HrLeaveTeamGanttModel,
        }),

        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            console.log(this.controllerParams);
        }
    });

    view_registry.add('hr_leave_team_gantt', HrLeaveTeamGanttView);

    return HrLeaveTeamGanttView;
});