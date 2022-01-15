# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcStock(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_stock/./s2pc-addons/s2pc_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_stock/./s2pc-addons/s2pc_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_stock.listing', {
#             'root': '/./s2pc-addons/s2pc_stock/./s2pc-addons/s2pc_stock',
#             'objects': http.request.env['./s2pc-addons/s2pc_stock../s2pc-addons/s2pc_stock'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_stock/./s2pc-addons/s2pc_stock/objects/<model("./s2pc-addons/s2pc_stock../s2pc-addons/s2pc_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_stock.object', {
#             'object': obj
#         })
