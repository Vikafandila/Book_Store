from urllib.request import HTTPPasswordMgrWithPriorAuth
from odoo import api, fields, modedels


class costumeorder(models.Model):
    _name = 'youre.costumeorder'
    _description = 'Data costume book'

    type = fields.Char(string='category buku')
    harga = fields.Interger(string='harga buku')
    nama = fields.Char(string='pengarang')
    jumlah = fields.Interger(string='jumlah buku')