from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, ValidationError
import logging
from datetime import date
import ipdb

class SiswaSiswa(models.Model):
    _name = "siswa.siswa"
    _rec_name = 'nama'
    _description = "siswa"

    nama = fields.Char()
    nomer_telepon = fields.Char()
    jenisKelamin = fields.Selection([
        (0, "Pria"),
        (1, "Wanita")
    ])
    tanggal_lahir = fields.Date()
    kelas_id = fields.Many2one(comodel_name="kelas.kelas", string="kelas", required=False)

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Siswa'),
            'template': '/sekolah/static/xls/template-siswa.xls'
        }]
