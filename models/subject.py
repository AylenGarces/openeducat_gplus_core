# -*- coding: utf-8 -*-

from openerp import models, fields


class OpSubject(models.Model):
    _name = 'op.subject'

    name = fields.Char(string='Nombre', size=128, required=True)
    code = fields.Char(string='Siglas', size=256, required=True)
    # course_id = fields.Many2one(comodel_name='op.course', string='Curso')
    grade_weightage = fields.Float('Grade Weightage')

    type = fields.Many2one(string='Tipo', comodel_name='op.type.subject')

    approved_note = fields.Integer(string='Nota de Aprobado')
    credits = fields.Integer(string='Créditos')
    meetings = fields.Integer(string='Número de encuentros')
    teachers_lines = fields.Many2one(string='Tipo', comodel_name='op.teacher')
    # TODO falta or programr la lista de profesores
