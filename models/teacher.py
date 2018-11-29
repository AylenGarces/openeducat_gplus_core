# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Teacher(models.Model):
    _name = 'op.teacher'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Contacto', required=True)
    active = fields.Boolean(default=True)
    cat_doc_estable = fields.Many2one(
        comodel_name='cat.doc.estable', string='Categoría Docente Estable')
    cat_doc_noestable = fields.Many2one(
        comodel_name='cat.doc.noestable', string='Categoría Docente No Estable')
    cat_doc_type = fields.Selection([('estable', 'Estable'), ('noestable', 'No Estable')], default='estable',
                                    string="Categoría Docente")

    @api.multi
    def go_partner_form(self):
        action = self.env.ref('mail.action_contacts').read()[0]
        view_id = self.env.ref('base.view_partner_form')
        action.update({
            'res_id': self.partner_id.id,
            'views': [(view_id.id, 'form')]
        })
        return action


class CatDocenteEstable(models.Model):
    _name = 'cat.doc.estable'  # TODO Poner permisos

    name = fields.Char('Nombre')


class CatDocenteNoEstable(models.Model):
    _name = 'cat.doc.noestable'  # TODO Poner permisos

    name = fields.Char('Nombre')
