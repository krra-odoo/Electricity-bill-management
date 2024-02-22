{
    'name': "electricity",
    'version': '1.0',
    'depends': ['base'],
    'author': "krra",
    'data': [
        'security/ir.model.access.csv',
        'views/electricity_bill_view.xml',
        'views/electricity_menu.xml',
    ],
    'application': True,
    'installable': True,
}
