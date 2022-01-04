# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ./s2pc-addons/s2pc_production(models.Model):
#     _name = './s2pc-addons/s2pc_production../s2pc-addons/s2pc_production'
#     _description = './s2pc-addons/s2pc_production../s2pc-addons/s2pc_production'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
