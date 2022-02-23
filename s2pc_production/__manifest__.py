# -*- coding: utf-8 -*-
{
    'name': "s2pc_production",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale', 'hr', 's2pc_product', 'quality_mrp', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production.xml',
        'views/mrp_team.xml',
        'views/mrp_production_views.xml',
        'views/mrp_bom_form_view.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
