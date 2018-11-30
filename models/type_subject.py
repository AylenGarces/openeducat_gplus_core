# -*- coding: utf-8 -*-

from openerp import models, fields


class TypeSubject(models.Model):
    _name = 'op.type.subject'

    type = fields.Selection(
        [
            ('required', 'Obligatoria'),
            ('optional', 'Optativa'),
            ('seminar', 'Seminario'),
            ('intensive', 'Intensiva'),
            ('extradocente_activities', 'Actividades Extradocentes'),
            ('end_cycle', 'Fin de Ciclo'),
        ],
        string="Tipo",
    )
    sequence = fields.Char(string='Secuencia', size=128, required=True)
    is_required = fields.Boolean(string='Obligatorio')
    is_application = fields.Boolean(string='Se muestra en Aplicacion?')
    note = fields.Text(string='Notas')
