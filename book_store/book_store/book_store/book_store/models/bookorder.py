from odoo import api, fields, modedels


class bookorder(models.Model):
    _name = 'book.bookorder'
    _description = 'Data Order Buku'

    jenis = fields.Char(string='judul buku')
    type = fields.Interger(string='category buku')
    harga = fields.Char(string='harga buku')
    nama = fields.Interger(string='pengarang')
    stock = fields.Interger(string='jumlah stok')