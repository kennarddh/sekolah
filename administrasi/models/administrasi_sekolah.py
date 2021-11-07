from odoo import api, fields, models, _
from datetime import datetime

class AdministrasiSekolah(models.Model):
    _name = 'administrasi.sekolah'
    _rec_name = 'name'
    _description = 'Administrasi Sekolah'

    name = fields.Char(default="New")
    state = fields.Selection(default="new", string="State", selection=[('new', 'New'), ('confirm', 'Confirm'), ], required=False, )
    siswa_id = fields.Many2one(comodel_name="siswa.siswa", string="Siswa", required=False, )
    confirmation_date = fields.Datetime(readonly=True)
    total = fields.Float(compute="compute_total")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", required=False, default=lambda self: self.env.ref('base.IDR'))
    administrasi_sekolah_line_ids = fields.One2many(
        comodel_name="administrasi.sekolah.line",
        inverse_name="administrasi_sekolah_id",
        string="Line",
        required=False)
    perpustakaan_count = fields.Integer(string='Perpustakaan', compute='compute_perpustakaan_count')

    def compute_total(self):
        total = sum(x.nominal for x in self.administrasi_sekolah_line_ids)

        self.update({"total": total})

        return

    def compute_perpustakaan_count(self):
        for me in self:
            perpustakaan_count = self.env["perpustakaan.sekolah"].search_count([(
                "siswa_id", "=", me.siswa_id.id
            )])

            me.update({"perpustakaan_count": perpustakaan_count})
        return

    def action_confirm(self):
        if self.name.lower() == "new":
            newName = self.env.ref('administrasi.seq_administrasi_sekolah').next_by_id()
        else:
            newName = self.name

        self.update({
            'state': 'confirm',
            'name': newName,
            'confirmation_date': datetime.today()
        })
        return

    def action_new(self):
        self.update({'state': 'new'})
        return

    def action_perpustakaan_sekolah(self):
        return {
            'name': _('Perpustakaan Sekolah'),
            'view_mode': 'tree,form',
            'view_id': False,
            'res_model': 'perpustakaan.sekolah',
            'context': '',
            'type': 'ir.actions.act_window',
            'domain': [
                (
                    "siswa_id",
                    "=",
                    self.siswa_id.id
                )
            ]
        }


class AdministrasiSekolahLine(models.Model):
    _name = 'administrasi.sekolah.line'
    _rec_name = 'name'
    _description = 'Administrasi Sekolah Line'

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
    administrasi_sekolah_id = fields.Many2one(comodel_name="administrasi.sekolah", string="Administrasi Sekolah", required=False, )
