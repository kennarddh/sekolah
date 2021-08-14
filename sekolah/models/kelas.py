from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, ValidationError
import logging
from datetime import date
import ipdb

class KelasKelas(models.Model):
    _name = 'kelas.kelas'
    _rec_name = 'name'
    _description = 'kelas'

    name = fields.Char()
    siswa_ids = fields.One2many(comodel_name="siswa.siswa", inverse_name="kelas_id", string="siswa terdaftar", required=False)
    jadwal_berjalan_ids = fields.One2many(comodel_name="jadwal.berjalan", inverse_name="kelas_id", string="Jadwal Berjalan", required=False, )

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Kelas'),
            'template': '/sekolah/static/xls/template-kelas.xls'
        }]

    def generate_jadwal_berjalan(self):
        exist = self.jadwal_berjalan_ids.filtered(lambda x: x.tanggal == date.today())

        if exist:
            raise UserError("Jadwal Ada")

        dateNow = date.today().weekday()

        template = self.env["jadwal.detail"].search([("japel_id.hari", "=", dateNow)])

        for row in template:
            guru = self.env["guru.guru"].search([("mapel_ids", "like", row.mapel_id.id)])

            data = row.read()[0]
            data["guru_id"] = guru[0].id  # otomatis pilih guru yang masih kosong
            data["tanggal"] = date.today()
            self.update({"jadwal_berjalan_ids": [(0, 0, data)]})

    def generate_jadwal_berjalan_task(self):
        search = self.search([])

        for row in search:
            row.generate_jadwal_berjalan()
