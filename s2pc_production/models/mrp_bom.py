# <<<<<<< HEAD
# from odoo import fields, models, api
#
#
# class ModelName(models.Model):
#     _inherit = 'mrp.bom.line'
#     _description = 'Use to add a section and note on bom line'
#
#     display_type = fields.Selection([
#         ('line_section', "Section"),
#         ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
#     name = fields.Text(string='Description')
#
#     product_id = fields.Many2one('product.product', 'Component', required=False, check_company=False)
#
#     @api.model_create_multi
#     def create(self, vals_list):
#         for values in vals_list:
#             print(self.env["product.product"].search([], limit=1))
#             if values.get('display_type', self.default_get(['display_type'])['display_type']):
#                 print("ato le for bom")
#                 temp = self.env["product.product"].search([('name', '=', 'OPERATION')])
#                 values.update({'product_id': temp.id, 'product_qty': 0})
#         lines = super().create(vals_list)
#         return lines
# =======
# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.tools.float_utils import float_compare

class MrpBomLine(models.Model):
	_inherit = 'mrp.bom.line'

	restricted_operation_id = fields.Many2one('mrp.routing.workcenter', copy=False)

	@api.model
	def get_operation(self):
		return self.bom_id.operation_ids.read(['id', 'name'])


class MrpBom(models.Model):
	_inherit = 'mrp.bom'

	def copy(self, default=None):
		res = super(MrpBom, self).copy(default)
		for bom_line in self.bom_line_ids:
			if bom_line.restricted_operation_id:
				operation = self.env['mrp.routing.workcenter'].search([('name', '=', bom_line.restricted_operation_id.name),
				                                                       ('id', 'in', res.operation_ids.ids)], limit=1)
				new_bom_line = fields.first(res.bom_line_ids.filtered(
					lambda l: l.product_id == bom_line.product_id
					          and float_compare(l.product_qty, bom_line.product_qty, precision_rounding=l.product_uom_id.rounding) == 0
					          and l.product_uom_id == bom_line.product_uom_id
							  and not l.restricted_operation_id

				))
				if operation and new_bom_line:
					new_bom_line.restricted_operation_id = operation.id
		return res
