# -*- coding: utf-8 -*-
{
    'name': "s2pc_maintenance",

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
    'depends': ['base', 'maintenance', 'mrp_maintenance', 'hr_maintenance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/maintenance_equipment.xml',
        'views/maintenance_request.xml',
        'views/templates.xml',
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
