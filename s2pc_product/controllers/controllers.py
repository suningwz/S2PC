# -*- coding: utf-8 -*-
# from odoo import http


# class S2pcProduct(http.Controller):
#     @http.route('/s2pc_product/s2pc_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s2pc_product/s2pc_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s2pc_product.listing', {
#             'root': '/s2pc_product/s2pc_product',
#             'objects': http.request.env['s2pc_product.s2pc_product'].search([]),
#         })

#     @http.route('/s2pc_product/s2pc_product/objects/<model("s2pc_product.s2pc_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s2pc_product.object', {
#             'object': obj
#         })
