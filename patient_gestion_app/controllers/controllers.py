# -*- coding: utf-8 -*-
# from odoo import http


# class PatientGestionApp(http.Controller):
#     @http.route('/patient_gestion_app/patient_gestion_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patient_gestion_app/patient_gestion_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('patient_gestion_app.listing', {
#             'root': '/patient_gestion_app/patient_gestion_app',
#             'objects': http.request.env['patient_gestion_app.patient_gestion_app'].search([]),
#         })

#     @http.route('/patient_gestion_app/patient_gestion_app/objects/<model("patient_gestion_app.patient_gestion_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patient_gestion_app.object', {
#             'object': obj
#         })
