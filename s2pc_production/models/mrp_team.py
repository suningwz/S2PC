from odoo import fields, models, api


class ProductionTeam(models.Model):
    _name = 'mrp.team'
    _description = 'Production Team'

    name = fields.Char("Nom de l'équipe", required=True, translate=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)
    member_ids = fields.Many2many(
        'hr.employee', string="Membre de l'équipe")
    color = fields.Integer("Color Index", default=0)
