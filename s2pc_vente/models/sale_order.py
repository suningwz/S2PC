# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.addons.s2pc_base.models.tools import amount_to_text_fr


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    amount_total_text = fields.Char('Amount total text', compute='compute_amount_to_text')

    def compute_amount_to_text(self):
        for rec in self:
            rec.amount_total_text = amount_to_text_fr(rec.amount_total, rec.currency_id.currency_unit_label)
