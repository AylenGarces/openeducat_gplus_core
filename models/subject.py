# -*- coding: utf-8 -*-

from openerp import models, fields


class OpSubject(models.Model):
    _name = 'op.subject'

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=256, required=True)
    course_id = fields.Many2one('op.course', 'Course')
    grade_weightage = fields.Float('Grade Weightage')
    type = fields.Char(name='Tipo', size=128, required=True)
