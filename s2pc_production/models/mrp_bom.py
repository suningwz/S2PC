from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'mrp.bom.line'
    _description = 'Use to add a section and note on bom line'

    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    name = fields.Text(string='Description')

    product_id = fields.Many2one('product.product', 'Component', required=False, check_company=False)

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            print(self.env["product.product"].search([], limit=1))
            if values.get('display_type', self.default_get(['display_type'])['display_type']):
                print("ato le for bom")
                temp = self.env["product.product"].search([('name', '=', 'OPERATION')])
                values.update({'product_id': temp.id, 'product_qty': 0})
        lines = super().create(vals_list)
        return lines
