# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcMaintenance(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_maintenance/./s2pc-addons/s2pc_maintenance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_maintenance/./s2pc-addons/s2pc_maintenance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_maintenance.listing', {
#             'root': '/./s2pc-addons/s2pc_maintenance/./s2pc-addons/s2pc_maintenance',
#             'objects': http.request.env['./s2pc-addons/s2pc_maintenance../s2pc-addons/s2pc_maintenance'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_maintenance/./s2pc-addons/s2pc_maintenance/objects/<model("./s2pc-addons/s2pc_maintenance../s2pc-addons/s2pc_maintenance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_maintenance.object', {
#             'object': obj
#         })
