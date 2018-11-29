# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Student(models.Model):
    _name = 'op.student'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Contacto', required=True)
    student = fields.Boolean(default=True, related='partner_id.student', store=True)

    @api.multi
    def go_partner_form(self):
        action = self.env.ref('mail.action_contacts').read()[0]
        view_id = self.env.ref('base.view_partner_form')
        action.update({
            'res_id': self.partner_id.id,
            'views': [(view_id.id, 'form')]
        })
        return action
