# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    demandeur = fields.Many2one('res.users', string='Demandeur', ondelete="restrict")
    reclamation_fournisseur = fields.Text(string='Reclamation fournisseur', index=1)
