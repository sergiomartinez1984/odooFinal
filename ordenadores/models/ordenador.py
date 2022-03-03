from odoo import models, fields

class ordenador(models.Model):
    _name='ordenadores.ordenador'
    _description = 'ordenador'

    name= fields.Integer('Codigo del PC', required = True)
    nomPc= fields.Char('Nombre del PC', requiered = True)
    typePc= fields.Many2one('ordenadores.tipos', 'Tipos de PC')
    precio= fields.Char('Precio del Producto', required = True)

def name_get(self):
    res=[]
    for record in self:
        nameC = record.nomPc
        res.append((record.id, nameC))
    return res
