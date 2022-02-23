# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class s2pc_conge(models.Model):
#     _name = 's2pc_conge.s2pc_conge'
#     _description = 's2pc_conge.s2pc_conge'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
