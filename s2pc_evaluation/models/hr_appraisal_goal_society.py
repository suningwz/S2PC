# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrAppraisalDepartement(models.Model):
    _name = 'hr.appraisal.goal.society'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Appraisal Goal for society"

    name = fields.Char(required=True)
    society_id = fields.Many2one('res.company', string="Société", required=True)
    manager_id = fields.Many2one('hr.employee', string="Responsable", readonly=False,
                                 store=True, required=True)
    manager_user_id = fields.Many2one('res.users', related='manager_id.user_id')
    progression = fields.Selection(selection=[
        ('0', '0 %'),
        ('25', '25 %'),
        ('50', '50 %'),
        ('75', '75 %'),
        ('100', '100 %')
    ], string="Progression", default="0", required=True)
    description = fields.Html()
    deadline = fields.Date(string="Date limite")

    def action_confirm(self):
        self.write({'progression': '100'})
