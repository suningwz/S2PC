# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcEmploye(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_employe/./s2pc-addons/s2pc_employe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_employe/./s2pc-addons/s2pc_employe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_employe.listing', {
#             'root': '/./s2pc-addons/s2pc_employe/./s2pc-addons/s2pc_employe',
#             'objects': http.request.env['./s2pc-addons/s2pc_employe../s2pc-addons/s2pc_employe'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_employe/./s2pc-addons/s2pc_employe/objects/<model("./s2pc-addons/s2pc_employe../s2pc-addons/s2pc_employe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_employe.object', {
#             'object': obj
#         })
