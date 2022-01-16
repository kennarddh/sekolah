from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, ValidationError
import logging
from datetime import date
import ipdb

from odoo.addons.sekolah.models.api import Api

class SiswaSiswa(models.Model):
    _name = "siswa.siswa"
    _rec_name = 'nama'
    _description = "siswa"

    nama = fields.Char()
    alamat = fields.Char()
    api_external_id = fields.Integer()
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

    @api.model
    def get_import_nama_siswa(self):
        api = Api()

        data = api.name()['data']

        for line in data:
            if self.search([('api_external_id', '=', int(line['id']))]):
                continue

            self.create({
                'nama': line['name'],
                'alamat': line['alamat'],
                'api_external_id': int(line['id']),
            })