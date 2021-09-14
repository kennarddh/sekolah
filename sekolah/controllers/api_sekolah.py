from odoo.http import Controller, request, route
from datetime import datetime

class SekolahController(Controller):
    @route('/sekolah/test', type='json', auth='public', method=["post"], csrf=False)
    def test(self):
        return "ok"

    @route(['/sekolah/siswa/create', '/sekolah/siswa/update'], type='json', auth='public', method=["post"], csrf=False)
    def import_siswa(self):
        # date format : mm/dd/yyyy

        data = request.jsonrequest

        try:
            obj = request.env.ref(data["externalId"])
        except:
            obj = None

        dataInput = {
            "nama":data["nama"],
            "nomer_telepon":data["noTelp"],
            "jenisKelamin":data["jenisKelamin"],
            "tanggal_lahir":datetime.strptime(data["tanggalLahir"], "%m/%d/%Y"),
            "kelas_id":data["kelas"]
        }

        if obj:
            obj.sudo().update(dataInput)
        else:
            obj = request.env["siswa.siswa"].sudo().create(dataInput)

        return obj
