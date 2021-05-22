from odoo import api, fields, models

class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'
    _rec_name = 'name'
    _description = 'Mapel'

    name = fields.Char()
