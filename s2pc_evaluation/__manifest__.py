# -*- coding: utf-8 -*-
{
    'name': "s2pc_evaluation",

    'summary': """This module is used for hr_appraisal and department appraisal feature""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alpha conseils",
    'website': "http://www.alphamada.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 's2pc_base', 'hr_appraisal', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_appraisal_goal_department_view.xml',
        'views/hr_appraisal_goal_society_view.xml',
        'views/hr_appraisal_goal_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
