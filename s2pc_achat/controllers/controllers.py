# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcAchat(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_achat/./s2pc-addons/s2pc_achat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_achat/./s2pc-addons/s2pc_achat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_achat.listing', {
#             'root': '/./s2pc-addons/s2pc_achat/./s2pc-addons/s2pc_achat',
#             'objects': http.request.env['./s2pc-addons/s2pc_achat../s2pc-addons/s2pc_achat'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_achat/./s2pc-addons/s2pc_achat/objects/<model("./s2pc-addons/s2pc_achat../s2pc-addons/s2pc_achat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_achat.object', {
#             'object': obj
#         })
