from odoo import fields, models, api
import dateutil.parser


class MaintenanceRequestInherit(models.Model):
    _inherit = 'maintenance.request'
    _description = 'Description'
    request_check = fields.Boolean('Maintenance respectée ', compute='_compare_date', store=True)

    @api.depends('close_date', 'schedule_date')
    def _compare_date(self):
        for record in self:
            if record.close_date and record.schedule_date:
                if record.close_date == record.schedule_date.date():
                    record.request_check = True
                else:
                    record.request_check = False
            else:
                record.request_check = False
