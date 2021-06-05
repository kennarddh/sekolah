# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sekolah',
    'version': '1.1',
    'category': 'General',
    'summary': 'Sekolah',
    'author':'admin',
    'description': """
    ...
    """,
    'depends': [],
    'data': [
        "views/guru_view.xml",
        "views/kelas_view.xml",
        "views/menu_sekolah.xml",
        "security/ir.model.access.csv"
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
