from odoo import fields, models

class billModel(models.Model):
    _name = "bill.property"
    _description = "Bill Model"

    bill_number = fields.Char(required=True)
    total_usage = fields.Integer()
    due_date = fields.Date()
    total_amount = fields.Float()
