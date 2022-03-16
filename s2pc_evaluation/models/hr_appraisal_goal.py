from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'hr.appraisal.goal'
    _description = 'Description'
    departement_goal_id = fields.Many2one(
        comodel_name='hr.appraisal.goal.department',
        string='Objectif du département associé',
        required=True)
    society_goal_id = fields.Many2one(
        comodel_name='hr.appraisal.goal.society',
        string='Objectif de la société associé',
        required=True)


