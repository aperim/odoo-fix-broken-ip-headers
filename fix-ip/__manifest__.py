# -*- coding: utf-8 -*-
{
    'name': "fix-ip",

    'summary': """
        Hack to fix Odoo's broken handling of remote user IP
        address when behind loadbalancers""",

    'description': """
        Odoo is unable to correctly provide the remote users IP address
    """,

    'author': "Aperim",
    'website': "https://github.com/aperim/odoo-fix-broken-ip-headers",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
