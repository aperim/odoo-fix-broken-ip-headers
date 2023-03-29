# -*- coding: utf-8 -*-
# from odoo import http


# class Fix-ip(http.Controller):
#     @http.route('/fix-ip/fix-ip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fix-ip/fix-ip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fix-ip.listing', {
#             'root': '/fix-ip/fix-ip',
#             'objects': http.request.env['fix-ip.fix-ip'].search([]),
#         })

#     @http.route('/fix-ip/fix-ip/objects/<model("fix-ip.fix-ip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fix-ip.object', {
#             'object': obj
#         })
