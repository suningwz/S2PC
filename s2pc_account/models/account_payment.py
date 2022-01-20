# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountPayment(models.Model):
	_inherit = 'account.payment'

	need_validation = fields.Boolean('Need validation', default=False, tracking=True, copy=False)

	def action_need_validation(self):
		for rec in self:
			rec.need_validation = True

	def action_post(self):
		res = super(AccountPayment, self).action_post()
		for rec in self:
			rec.need_validation = False
		return res
