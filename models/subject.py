# -*- coding: utf-8 -*-

from openerp import models, fields


class OpSubject(models.Model):
    _name = 'subject'

    name = fields.Char(string='Nombre', size=128, required=True)
    code = fields.Char(string='Código', size=256, required=True)
    # course_id = fields.Many2one(comodel_name='op.course', string='Curso')
    grade_weightage = fields.Float('Grade Weightage')

    type = fields.Many2one(string='Tipo', comodel_name='type.subject')
