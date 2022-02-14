from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'mrp.bom.line'
    _description = 'Use to add a section and note on bom line'

    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Text(string='Description')
