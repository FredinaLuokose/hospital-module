
from odoo import models, fields


class Patient(models.Model):
    _name = 'patient.details'
    _description = 'Display details of patients'

    name = fields.Char(string='Patient name')
    disease_name = fields.Char(string='Disease name')
    age = fields.Integer(string='Age')
    phone_no = fields.Char(string='Mobile no')
    address = fields.Text(string='Address')
    appointment_id = fields.One2many(comodel_name='appointment.details', inverse_name='patient_id',
                                     string='Appointment')