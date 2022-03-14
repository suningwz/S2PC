# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    cnaps_number = fields.Char('Numero CNAPS', index=1)
    team_employee_ids = fields.Many2many('hr.employee', 'hr_employee_team_rel', 'manager_id', 'employee_id', 'Team')
    langue = fields.Selection(
        [('english', 'Anglais'),
         ('french', 'Français'),
         ('malgace', 'Malagasy')],
        'Langue')


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'
    cnaps_number = fields.Char(readonly=True)
    langue = fields.Selection(
        [('english', 'Anglais'),
         ('french', 'Français'),
         ('malgace', 'Malagasy')],
        'Langue')
