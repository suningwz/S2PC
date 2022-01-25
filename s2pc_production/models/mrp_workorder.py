# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'
    # _rec_name = 'qty_producing'
    # workorder_name = fields.one2many()

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         rec_name = "%s" % (record.working_state,)
    #     result.append((record.id, rec_name))
    #     return result