# -*- coding: utf-8 -*-

from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor.details'
    _description = 'doctor'
    name = fields.Char(string='Doctor name')
    email = fields.Char()
    phone_no = fields.Char()
    specialty = fields.Char(string='Specialty')
    appointment_id = fields.One2many('appointment.details', 'doctor_id', string='Appointment')
