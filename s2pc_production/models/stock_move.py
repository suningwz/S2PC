# <<<<<<< HEAD
# # from odoo import fields, models, api
# #
# # class ModelName(models.Model):
# #     _inherit = 'stock.move'
# #     _description = 'Herited for bom of mrp'
# #
# #     display_type = fields.Selection([
# #         ('line_section', "Section"),
# #         ('line_note', "Note")], default=False, related="bom_line_id.display_type")
# #     bom_name = fields.Text(string='Description', related="bom_line_id.name", readonly=False)
# #
# #     @api.model_create_multi
# #     def create(self, vals_list):
# #         for values in vals_list:
# #             print(self.env["product.product"].search([], limit=1))
# #             if values.get('display_type', self.default_get(['display_type'])['display_type']):
# #                 print("ato le for bom")
# #                 temp = self.env["product.product"].search([('name', '=', 'OPERATION')])
# #                 values.update({'product_id': temp.id, 'product_uom_qty': 0})
# #         lines = super().create(vals_list)
# #         return lines
# =======
# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    restricted_workorder_id = fields.Many2one('mrp.workorder', copy=False)
