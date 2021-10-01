# -*- coding: utf-8 -*-
# from odoo import http


# class TestAnh(http.Controller):
#     @http.route('/test_anh/test_anh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_anh/test_anh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_anh.listing', {
#             'root': '/test_anh/test_anh',
#             'objects': http.request.env['test_anh.test_anh'].search([]),
#         })

#     @http.route('/test_anh/test_anh/objects/<model("test_anh.test_anh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_anh.object', {
#             'object': obj
#         })
