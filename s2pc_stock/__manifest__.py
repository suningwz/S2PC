# -*- coding: utf-8 -*-
{
    'name': "s2pc_stock",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Valisoa RAMILIJAONA",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'stock_enterprise', 's2pc_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_type.xml',
        'security/res_groups.xml',

        # views
        'views/templates.xml',
        'views/stock_picking_views.xml',
        'report/stock_report_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
