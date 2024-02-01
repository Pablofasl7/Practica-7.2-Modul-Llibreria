from odoo import models, fields, api

class Llibre(models.Model):
    _name = 'llibreria.llibre'
    _description = 'Llibre'

    name = fields.Char(string='Nom', required=True)
    preu = fields.Float(string='Preu')
    exemplars = fields.Integer(string='Exemplars')
    data = fields.Date(string='Data')
    segonama = fields.Boolean(string='Segonama')
    estat = fields.Selection([
        ('bo', 'Bo'),
        ('regular', 'Regular'),
        ('dolent', 'Dolent')
    ], string='Estat', default='bo')
    rotura_estoc = fields.Boolean(string='Rotura Estoc', compute='_compute_rotura_estoc')

    @api.depends('exemplars')
    def _compute_rotura_estoc(self):
        for record in self:
            record.rotura_estoc = record.exemplars < 10
