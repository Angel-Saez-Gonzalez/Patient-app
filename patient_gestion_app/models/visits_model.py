from datetime import datetime
from odoo import models, fields, api

class visitsModel(models.Model):
    _name = 'patient_gestion_app.visits_model'
    _description = 'Visits Model'

    patient_id = fields.Many2one("patient_gestion_app.patient_model",string="Patients")
    date =fields.Datetime("Last Change", compute="_createDate", help="Date of the visit")
    detail = fields.Html(string="Visits detail", Required = True,help="Detail of the Visit")


    @api.depends("date")     
    def _createDate(self):         
        self.date = datetime.now()          
        return True