from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, ValidationError
import logging
from datetime import date

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


class KelasKelas(models.Model):
    _name = 'kelas.kelas'
    _rec_name = 'name'
    _description = 'kelas'

    name = fields.Char()
    siswa_ids = fields.One2many(comodel_name="siswa.siswa", inverse_name="kelas_id", string="siswa terdaftar", required=False)
    jadwal_berjalan_ids = fields.One2many(comodel_name="jadwal.berjalan", inverse_name="kelas_id", string="Jadwal Berjalan", required=False, )

    def generate_jadwal_berjalan(self):
        dateNow = date.today().weekday()

        logging.info(dateNow)
        raise UserError(dateNow)
