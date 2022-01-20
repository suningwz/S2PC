# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
	_inherit = 'stock.picking'

	need_validation = fields.Boolean('Need validation', default=False, tracking=True, copy=False)

	def action_need_validation(self):
		for rec in self:
			rec.need_validation = True

	def action_done(self):
		super(StockPicking, self).action_done()
		for rec in self:
			if rec.state == 'done':
				rec.need_validation = False

	@api.depends('state')
	def _compute_show_validate(self):
		super(StockPicking, self)._compute_show_validate()
		for picking in self:
			if not self.env.user.has_group('s2pc_stock.group_confirm_picking') and picking.picking_type_code in ['internal', 'incoming'] and picking.state == 'assigned':
				picking.show_validate = False

