# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcProduction(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_production/./s2pc-addons/s2pc_production/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_production/./s2pc-addons/s2pc_production/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_production.listing', {
#             'root': '/./s2pc-addons/s2pc_production/./s2pc-addons/s2pc_production',
#             'objects': http.request.env['./s2pc-addons/s2pc_production../s2pc-addons/s2pc_production'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_production/./s2pc-addons/s2pc_production/objects/<model("./s2pc-addons/s2pc_production../s2pc-addons/s2pc_production"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_production.object', {
#             'object': obj
#         })
