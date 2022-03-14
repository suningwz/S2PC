	# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpWorcenter(models.Model):
	_inherit = 'mrp.workcenter'

	conditioning_center = fields.Boolean('Poste de conditionnement')
