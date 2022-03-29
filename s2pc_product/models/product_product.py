# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductproductInherit(models.Model):
    _inherit = 'product.product'
    ref_agir = fields.Char(
        string='Référence AGIR')
