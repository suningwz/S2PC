# -*- coding: utf-8 -*-
# from odoo import http


# class S2pcSecurite(http.Controller):
#     @http.route('/s2pc_securite/s2pc_securite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s2pc_securite/s2pc_securite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s2pc_securite.listing', {
#             'root': '/s2pc_securite/s2pc_securite',
#             'objects': http.request.env['s2pc_securite.s2pc_securite'].search([]),
#         })

#     @http.route('/s2pc_securite/s2pc_securite/objects/<model("s2pc_securite.s2pc_securite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s2pc_securite.object', {
#             'object': obj
#         })
