# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class s2pc_evaluation(models.Model):
#     _name = 's2pc_evaluation.s2pc_evaluation'
#     _description = 's2pc_evaluation.s2pc_evaluation'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
