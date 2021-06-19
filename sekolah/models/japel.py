from odoo import api, fields, models

class JadwalPelajaran(models.Model):
    _name = 'jadwal.pelajaran'
    _rec_name = 'name'
    _description = 'Japel'

    name = fields.Char()
    hari = fields.Selection([
        (0, "senin"),
        (1, "selasa"),
        (2, "rabu"),
        (3, "kamis"),
        (4, "jumat"),
        (5, "sabtu"),
        (6, "minggu")
    ])

    kelas_id = fields.Many2one(comodel_name="kelas.kelas", string="Kelas", required=False, )

    jadet_ids = fields.One2many(comodel_name="jadwal.detail", inverse_name="japel_id", string="Detail Jadwal Pelajaran", required=False, )


class JadwalDetail(models.Model):
    _name = 'jadwal.detail'
    _rec_name = 'name'
    _description = 'jadel'

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

    startHour = fields.Selection(hourList)
    startMinute = fields.Selection(minuteList)

    endHour = fields.Selection(hourList)
    endMinute = fields.Selection(minuteList)

    mapel_id = fields.Many2one(comodel_name="mata.pelajaran", string="Mata Pelajaran", required=False, )

    japel_id = fields.Many2one(comodel_name="jadwal.pelajaran", string="Jadwal id", required=False, )
