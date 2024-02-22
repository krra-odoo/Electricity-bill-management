from odoo import fields, models

class meterModel(models.Model):
    _name = "meter.property"
    _description = "Meter Model"

    name = fields.Char()
    meter_number = fields.Char(required=True)
    last_reading = fields.Integer()
    current_reading = fields.Integer()
