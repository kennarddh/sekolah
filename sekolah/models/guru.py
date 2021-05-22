from odoo import api, fields, models

class GuruGuru(models.Model):
    _name = 'guru.guru'
    _rec_name = 'name'
    _description = 'Guru'

    name = fields.Char()
