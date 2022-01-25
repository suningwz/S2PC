# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    STAT = fields.Char('STAT', index=1)
    RCS = fields.Char('RCS', index=1)
    CIF = fields.Char('CIF', index=1)
    advised_pricelist_id = fields.Many2one('product.pricelist', 'Advised Pricelist')

    @api.model
    def get_parent(self):
        self.ensure_one()
        if not self.parent_id:
            return self
        return self.get_parent()
