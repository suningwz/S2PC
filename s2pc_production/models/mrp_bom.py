# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MrpBomLine(models.Model):
	_inherit = 'mrp.bom.line'

	restricted_operation_id = fields.Many2one('mrp.routing.workcenter')

	@api.model
	def get_operation(self):
		return self.bom_id.operation_ids.read(['id', 'name'])
