# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    cnaps_number = fields.Char('Numéro CNAPS', index=1)
