# -*- coding: utf-8 -*-
# from odoo import http


# class ./s2pc-addons/s2pcPaie(http.Controller):
#     @http.route('/./s2pc-addons/s2pc_paie/./s2pc-addons/s2pc_paie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./s2pc-addons/s2pc_paie/./s2pc-addons/s2pc_paie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./s2pc-addons/s2pc_paie.listing', {
#             'root': '/./s2pc-addons/s2pc_paie/./s2pc-addons/s2pc_paie',
#             'objects': http.request.env['./s2pc-addons/s2pc_paie../s2pc-addons/s2pc_paie'].search([]),
#         })

#     @http.route('/./s2pc-addons/s2pc_paie/./s2pc-addons/s2pc_paie/objects/<model("./s2pc-addons/s2pc_paie../s2pc-addons/s2pc_paie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./s2pc-addons/s2pc_paie.object', {
#             'object': obj
#         })
