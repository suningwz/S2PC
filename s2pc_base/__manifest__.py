# -*- coding: utf-8 -*-
{
    'name': "s2pc_base",

    'summary': """ S2PC Base""",

    'description': """

    """,

    'author': "Alpha conseils",
    'website': "https://www.alphamada.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/res_groups_category.xml',

        # views
        'views/company_external_layout.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
