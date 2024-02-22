from odoo import fields, models

class queryModel(models.Model):
    _name = "query.property"
    _description = "Query Model"

    ticket_number = fields.Char()
    title = fields.Char()
    description = fields.Char()
    state = fields.Selection(selection=[('received','Received'),
                                       ('in_process','In Process'),
                                       ('resolved','Resolved'),
                                       ('closed','Closed')
                                    ])
