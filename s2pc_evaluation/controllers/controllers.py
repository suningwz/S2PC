# -*- coding: utf-8 -*-
# from odoo import http


# class S2pcEvaluation(http.Controller):
#     @http.route('/s2pc_evaluation/s2pc_evaluation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s2pc_evaluation/s2pc_evaluation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s2pc_evaluation.listing', {
#             'root': '/s2pc_evaluation/s2pc_evaluation',
#             'objects': http.request.env['s2pc_evaluation.s2pc_evaluation'].search([]),
#         })

#     @http.route('/s2pc_evaluation/s2pc_evaluation/objects/<model("s2pc_evaluation.s2pc_evaluation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s2pc_evaluation.object', {
#             'object': obj
#         })
