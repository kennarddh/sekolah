from odoo import api, fields, models, _
from datetime import datetime

class AdministrasiSekolah(models.Model):
    _name = 'administrasi.sekolah'
    _rec_name = 'name'
    _description = 'Administrasi Sekolah'

    _inherit = ['mail.thread', 'mail.activity.mixin']

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

        self.send_email(
            email_to='kennardphp@gmail.com',
            msg="<h1 style='margin: 10px; background-color: blue; padding: 20px;'>Judul</h1><h2>Sub</h2>",
            email_cc='kenodoo2@gmail.com',
            subject='Subject'
        )

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

    def send_email(self, email_to, msg, email_cc, subject):
        res = self.message_post(body=msg, message_type="email")

        servers = self.env['ir.mail_server'].sudo().search([])

        for server in servers:
            # set mail server
            res.mail_server_id = server.id
            mail = self.env['mail.mail'].create({
                'subject': subject,
                'email_to': email_to,
                'email_cc': email_cc,
                'body_html': msg,
                'mail_message_id': res.id,
            })
            mail.send()

            if mail.state == 'sent':
                break

        return



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
