# -*- coding: utf-8 -*-

{
    'name': 'Sale order signed and sealed',
    'version': '1.0.1.2',
    'author': 'Soft-integration',
    'category': 'Sale',
    'summary': 'Sale order signed and sealed',
    'description': "",
    'depends': [
        'sale'
    ],
    'data': [
        'views/res_users_views.xml',
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
