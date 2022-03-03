from odoo import models, fields, api

class Ofertas (models.Model):
    _name= 'ordenadores.ofertas'
    codOferta = fields.Integer('Codigo Oferta', required = True)
    newPrecio = fields.Float('Precio en Oferta', required = True)
    descrip = fields.Char('Descripcion de la Oferta', required = False)
    ordenador = fields.Many2one('ordenadores.ordenador', 'Nombre del Producto')
    activo = fields.Boolean('Esta activa la oferta?')

    
    def limpiar(self):
	    self.activo = False

