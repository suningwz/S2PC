from odoo import fields, models, api


class HrChildren(models.Model):
    _name = 'hr.child'
    _description = 'Description'
    employe_id = fields.Many2one('hr.employee')
    name = fields.Char(string="Nom")
    child_age = fields.Float(string="Age")
