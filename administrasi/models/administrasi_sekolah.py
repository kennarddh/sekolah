from odoo import api, fields, models

class AdministrasiSekolah(models.Model):
    _name = 'administrasi.sekolah'
    _rec_name = 'name'
    _description = 'Administrasi Sekolah'

    name = fields.Char(default="New")
    siswa_id = fields.Many2one(comodel_name="siswa.siswa", string="Siswa", required=False, )
    confirmation_date = fields.Datetime()
    administrasi_sekolah_line_ids = fields.One2many(
        comodel_name="administrasi.sekolah.line",
        inverse_name="administrasi_sekolah_id",
        string="Line",
        required=False)

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
