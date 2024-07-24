
from odoo import models, fields

class Appointment(models.Model):
    _name = 'appointment.details'
    _description = 'display appointment details'
    appointment_date = fields.Date(string='Date')
    doctor_id = fields.Many2one(comodel_name='doctor.details')
    patient_id = fields.Many2one(comodel_name='patient.details')
