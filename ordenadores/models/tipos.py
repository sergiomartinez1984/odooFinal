from odoo import models, fields

class tipos(models.Model):
    _name='ordenadores.ordenador'
    codTip = fields.Integer('Codigo del Tipo de PC', required = True)
    nomTip = fields.Char('Nombre del Tipo', requiered = True)

def name_get(self):
    resT=[]
    for record in self:
        nameT = record.nomTip
        resT.append((record.id, nameT))
    return resT
