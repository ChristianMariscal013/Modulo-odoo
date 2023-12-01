from odoo import models, fields

class Usuario(models.Model):
    _name = "lis.usuarios"
    _description = "Modelo de Usuarios"

    name = fields.Char(string="Nombre")
    numero = fields.Char(string="Numero de telefono")
    sexo = fields.Selection(
        selection=[("hombre", "Hombre"), ("mujer", "Mujer")],
        string="Sexo"
    )
    estado = fields.Selection(
        selection=[("casado", "Casado"), ("soltero", "Soltero"),("otros","Otros")],
        string="Estado Civil"
    )