# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcQualite(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_qualite/./s2pc-addons/s2pc_qualite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_qualite/./s2pc-addons/s2pc_qualite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_qualite.listing', {
#             'root': '/./s2pc-addons/s2pc_qualite/./s2pc-addons/s2pc_qualite',
#             'objects': http.request.env['./s2pc-addons/s2pc_qualite../s2pc-addons/s2pc_qualite'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_qualite/./s2pc-addons/s2pc_qualite/objects/<model("./s2pc-addons/s2pc_qualite../s2pc-addons/s2pc_qualite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_qualite.object', {
#             'object': obj
#         })
