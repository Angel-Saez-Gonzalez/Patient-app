from odoo.exceptions import ValidationError
import re
from datetime import date
from odoo import models, fields, api
import random
import string

class patientModel(models.Model):
    _name = 'patient_gestion_app.patient_model'
    _description = 'Patient Model'

    dni = fields.Char(string="Patient DNI", Required = True,index=True,help="DNI of the patient")
    name = fields.Char(string="Patient Name", Required = True,index=True,help="Name of the Patient")
    surname = fields.Char(string="Patient Surname", Required = True,index=True,help="Surname of the Patient")
    photo = fields.Binary(string="Photo",help="Photo of the Patient")
    phone = fields.Char(string="Patient Phone", Required = True,help="Phone of the Patient")
    birthday = fields.Date(string="Patient Birthday", Required = True,help="Bithday of the Patient")
    email = fields.Char(string="Patient Email", Required = True,help="Email of the Patient")
    visits = fields.One2many("patient_gestion_app.visits_model","patient_id", "Visits")


    @api.constrains("dni")
    def comprNIF(self):
        #import string # no necesario
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = self.dni
        respuesta = "No ha introducido un NIF valido"
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dn = nif[:8]
            if ( len(dn) == len( [n for n in dn if n in numeros] ) ):
                if tabla[int(dn)%23] == letraControl:
                    print("aaaaaaa")
                else:
                    raise ValidationError("The DNI is not valid")
            else:
                raise ValidationError("The DNI is not valid")
                    
        return True

    #@api.constrains("birthday")
    #def comprAge(self):
    #    today = date.today()
    #    a = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
    #    if a == 1:
    #        return True
    #    else:
    #        raise ValidationError("The patient is underage")

    @api.constrains("email")
    def comprEmail(self):
    
        correo = self.email

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    
        if(re.search(regex,correo)):   
            print("Valid Email")  
            return True

        else:   
            raise ValidationError("The patient email is not valid")