from odoo import api, fields, models

class JadwalBerjalalan(models.Model):
    _name = 'jadwal.berjalan'
    _rec_name = 'name'
    _description = 'Jadwal Berjalan'

    minuteList = []
    hourList = []

    count = 0
    for i in range(61):
        i = str(i)
        if len(i) == 1:
            i = "0" + i

        minuteList.append((count, i))
        count += 1

    count = 0
    for i in range(24):
        i = str(i)
        if len(i) == 1:
            i = "0" + i

        hourList.append((count, i))
        count += 1

    name = fields.Char()

    guru_id = fields.Many2one(comodel_name="guru.guru", string="Guru Id", required=False, )

    tanggal = fields.Date()

    startHour = fields.Selection(hourList)
    startMinute = fields.Selection(minuteList)

    endHour = fields.Selection(hourList)
    endMinute = fields.Selection(minuteList)

    mapel_id = fields.Many2one(comodel_name="mata.pelajaran", string="Mata Pelajaran", required=False, )

    kelas_id = fields.Many2one(comodel_name="kelas.kelas", string="Kelas id", required=False, )
