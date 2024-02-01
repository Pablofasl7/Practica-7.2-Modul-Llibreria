from odoo import models, fields

class Categoria(models.Model):
    _name = 'llibreria.categoria'
    _description = 'Categoria'

    name = fields.Char(string='Nom', required=True, help="Introduïx el nom de la categoria")
    descripcio = fields.Text(string='Descripció')