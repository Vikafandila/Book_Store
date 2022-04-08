from odoo import api, fields, modedels


class customer(models.Model):
    _name = 'book.customer'
    _description = 'Data customer'

    nama = fields.Char(string='nama customer')
    jenis = fields.Interger(string='judul buku')
    type = fields.Interger(string='category buku')
    harga = fields.Interger(string='harga buku')