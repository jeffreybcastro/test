# -*- coding: utf-8 -*-
{
    'name': 'HN Checks Layout',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Print HN Checks',
    'description': """
This module allows to print your payments on pre-printed check paper.
You can configure the output (layout, stubs informations, etc.) in company settings, and manage the
checks numbering (if you use pre-printed checks without numbers) in journal settings.
    """,
    'website': 'http://www.d2i-solutions.com',
    'depends' : ['account_check_printing', 'l10n_hn'],
    'data': [
        'data/hn_check_printing.xml',
        'report/print_check.xml',
        'report/print_check_top.xml',
        'report/print_check_middle.xml',
        'report/print_check_bottom.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
