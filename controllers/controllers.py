# -*- coding: utf-8 -*-

# class OpeneducatGplusCore(http.Controller):
#     @http.route('/openeducat_gplus_core/openeducat_gplus_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_gplus_core/openeducat_gplus_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_gplus_core.listing', {
#             'root': '/openeducat_gplus_core/openeducat_gplus_core',
#             'objects': http.request.env['openeducat_gplus_core.openeducat_gplus_core'].search([]),
#         })

#     @http.route('/openeducat_gplus_core/openeducat_gplus_core/objects/<model("openeducat_gplus_core.openeducat_gplus_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_gplus_core.object', {
#             'object': obj
#         })
