# -*- coding: utf-8 -*-

from openerp import models, fields


class TypeSubject(models.Model):
    _name = 'type.subject'

    name = fields.Char(String='Tipo', size=128, required=True)
    sequence = fields.Char(string='Secuencia', size=128)
    is_required = fields.Boolean(string='Obligatorio')
    is_application = fields.Boolean(string='Se muestra en Aplicacion?')
    note = fields.Text(string='Notas')
