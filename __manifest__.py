# -*- coding: utf-8 -*-

{
    'name': 'Sale order signed and sealed',
    'version': '1.0.1.3',
    'author': 'Soft-integration',
    'category': 'Sale',
    'summary': 'Sale order signed and sealed',
    'description': "",
    'depends': [
        'sale','res_user_document_signature'
    ],
    'data': [
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
