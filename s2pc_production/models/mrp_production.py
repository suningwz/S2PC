from odoo import fields, models, api
from datetime import timedelta, datetime


class ModelName(models.Model):
    _inherit = 'mrp.production'
    mrp_team = fields.Many2one('mrp.team', string="Equipe de production")
    current_date = fields.Date(string="To days date", default=datetime.now())
    date_planned_start_related = fields.Datetime(string="infos date prevue", related="date_planned_start",
                                                 readonly=True)
    # def show_runing_operation(self):

