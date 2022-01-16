# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
	_inherit = "account.move"

	advised_pricelist_id = fields.Many2one('product.pricelist', 'Advised pricelist', compute='_compute_advised_pricelist')

	def _compute_advised_pricelist(self):
		for rec in self:
			partner = rec.partner_id.get_parent()
			if partner.advised_pricelist_id:
				rec.advised_pricelist_id = rec.partner_id.advised_pricelist_id.id
			else:
				rec.advised_pricelist_id = False


class AccountMoveLine(models.Model):
	_inherit = 'account.move.line'

	advised_price_unit = fields.Monetary('Advised price unit', digits='Product Price', compute='_compute_advised_price_unit')
	advised_ratio = fields.Float('Advised price ratio', digits='Discount', compute='_compute_advised_ratio')

	def _compute_advised_price_unit(self):
		for rec in self:
			advised_pricelist = rec.move_id.advised_pricelist_id
			if advised_pricelist:
				rec.advised_price_unit = advised_pricelist.price_get(rec.product_id.id, rec.quantity).get(advised_pricelist.id)
			else:
				rec.advised_price_unit = 0

	def _compute_advised_ratio(self):
		for rec in self:
			if rec.price_unit and rec.advised_price_unit:
				rec.advised_ratio = rec.price_unit * 100 / rec.advised_price_unit
			else:
				rec.advised_ratio = 0
