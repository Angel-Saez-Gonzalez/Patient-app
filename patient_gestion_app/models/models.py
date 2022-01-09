# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class patient_gestion_app(models.Model):
#     _name = 'patient_gestion_app.patient_gestion_app'
#     _description = 'patient_gestion_app.patient_gestion_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
