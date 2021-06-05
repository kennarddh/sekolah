from odoo import api, fields, models

class GuruGuru(models.Model):
    _name = 'guru.guru'
    _rec_name = 'name'
    _description = 'Guru'

    name = fields.Char()
    foto_ids = fields.Many2many(comodel_name="ir.attachment", relation="guru_foto_rel", column1="guru_id",
                                column2="foto_id", string="pas Foto", )
    mapel_ids = fields.Many2many(comodel_name="mata.pelajaran", relation="guru_guru_mata_pelajaran_rel",
                                 column1="guru_id", column2="mapel_id", string="Mapel", )
