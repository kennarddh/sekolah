from odoo import api, fields, models
from datetime import datetime


class PerpustakaanSekolah(models.Model):
    _name = 'perpustakaan.sekolah'
    _rec_name = 'name'
    _description = 'Perpustakaan Sekolah'

    name = fields.Char(default="New")
    state = fields.Selection(default="new", string="State", selection=[('new', 'New'), ('confirm', 'Confirm'), ],
                             required=False, )
    siswa_id = fields.Many2one(comodel_name="siswa.siswa", string="Siswa", required=False, )
    confirmation_date = fields.Datetime(readonly=True)
    total = fields.Float(compute="compute_total")
    currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency", required=False,
        default=lambda self: self.env.ref('base.IDR')
    )

    perpustakaan_sekolah_line_ids = fields.One2many(comodel_name="perpustakaan.sekolah.line", inverse_name="perpustakaan_sekolah_id", string="Perpustakaan Sekolah", required=False, )

    def compute_total(self):
        total = sum(x.nominal for x in self.perpustakaan_sekolah_line_ids)

        self.update({"total": total})

        return

    def action_confirm(self):
        if self.name.lower() == "new":
            newName = self.env.ref('administrasi.seq_perpustakaan_sekolah').next_by_id()
        else:
            newName = self.name

        self.update({
            'state': 'confirm',
            'name': newName,
            'confirmation_date': datetime.today()
        })
        return

    def action_new(self):
        self.update({
            'state': 'new'
        })

        return

class PerpustakaanSekolahLine(models.Model):
    _name = 'perpustakaan.sekolah.line'
    _rec_name = 'name'
    _description = 'Perpustakaan Sekolah Line'

    name = fields.Char()
    bulan = fields.Selection(string="Bulan", selection=[
        ('januari', 'Januari'),
        ('febuari', 'Febuari'),
        ('maret', 'Maret'),
        ('april', 'April'),
        ('mei', 'Mei'),
        ('juni', 'Juni'),
        ('juli', 'Juli'),
        ('agustus', 'Agustus'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('desember', 'Desember')
    ], required=False, )

    tahun = state = fields.Selection(string="", selection=[
        ('2021', '2021'), ('2022', '2022')
    ], required=False, )

    nominal = fields.Float()
    perpustakaan_sekolah_id = fields.Many2one(comodel_name="perpustakaan.sekolah", string="Perpustakaan Sekolah", required=False, )
