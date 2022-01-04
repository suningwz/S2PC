# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcVente(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_vente/./s2pc-addons/s2pc_vente/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_vente/./s2pc-addons/s2pc_vente/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_vente.listing', {
#             'root': '/./s2pc-addons/s2pc_vente/./s2pc-addons/s2pc_vente',
#             'objects': http.request.env['./s2pc-addons/s2pc_vente../s2pc-addons/s2pc_vente'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_vente/./s2pc-addons/s2pc_vente/objects/<model("./s2pc-addons/s2pc_vente../s2pc-addons/s2pc_vente"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_vente.object', {
#             'object': obj
#         })
