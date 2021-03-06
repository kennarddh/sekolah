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
        'sekolah',
        'mail'
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/administrasi_view.xml",
        "views/perpustakaan_sekolah_view.xml",
        "data/sequence_administrasi_sekolah.xml",
        "data/sequence_perpustakaan_sekolah.xml",
        "data/email_administrasi_sekolah_template.xml",
        "views/administrasi_menu.xml",
        "views/perpustakaan_sekolah_menu.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
