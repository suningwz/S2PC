# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
	_inherit = 'stock.move'

	restricted_workorder_id = fields.Many2one('mrp.workorder')
