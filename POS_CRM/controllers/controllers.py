# -*- coding: utf-8 -*-
from odoo import http

# class Poscrm(http.Controller):
#     @http.route('/poscrm/poscrm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/poscrm/poscrm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('poscrm.listing', {
#             'root': '/poscrm/poscrm',
#             'objects': http.request.env['poscrm.poscrm'].search([]),
#         })

#     @http.route('/poscrm/poscrm/objects/<model("poscrm.poscrm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('poscrm.object', {
#             'object': obj
#         })
