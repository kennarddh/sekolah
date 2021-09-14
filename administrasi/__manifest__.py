# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Administrasi',
    'version': '1.1',
    'category': 'General',
    'summary': 'Administrasi',
    'author':'admin',
    'description': """
    ...
    """,
    'depends': [
        'sekolah'
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/administrasi_view.xml",
        "views/administrasi_menu.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
