# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcContact(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_contact/./s2pc-addons/s2pc_contact/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_contact/./s2pc-addons/s2pc_contact/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_contact.listing', {
#             'root': '/./s2pc-addons/s2pc_contact/./s2pc-addons/s2pc_contact',
#             'objects': http.request.env['./s2pc-addons/s2pc_contact../s2pc-addons/s2pc_contact'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_contact/./s2pc-addons/s2pc_contact/objects/<model("./s2pc-addons/s2pc_contact../s2pc-addons/s2pc_contact"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_contact.object', {
#             'object': obj
#         })
