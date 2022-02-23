# -*- coding: utf-8 -*-
# from odoo import http


# class S2pcConge(http.Controller):
#     @http.route('/s2pc_conge/s2pc_conge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s2pc_conge/s2pc_conge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s2pc_conge.listing', {
#             'root': '/s2pc_conge/s2pc_conge',
#             'objects': http.request.env['s2pc_conge.s2pc_conge'].search([]),
#         })

#     @http.route('/s2pc_conge/s2pc_conge/objects/<model("s2pc_conge.s2pc_conge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s2pc_conge.object', {
#             'object': obj
#         })
