# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Contacts(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([('f', 'Femenino'), ('m', 'Masculino')], string='Sexo', default='m')
    birthdate = fields.Date(string='Fecha Nacimiento')
    autority_lines = fields.One2many(comodel_name='autority.line', inverse_name='partner_id')
    student = fields.Boolean(default=False)
    teacher = fields.Boolean(default=False, string="Profesor?")
    nacionality = fields.Many2one('res.country', 'Nacionalidad')
    merito_lines = fields.One2many(comodel_name='merito.line', inverse_name='partner_id')
    sancion_lines = fields.One2many(comodel_name='sancion.line', inverse_name='partner_id')
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Grupo Sanguineo')
    emergency_contact = fields.Many2one(
        'res.partner', 'Contacto Emergencia')
    estado_civil = fields.Many2one(
        comodel_name='estado.civil', string='Estado Civil')
    estado_ecles = fields.Many2one(
        comodel_name='estado.ecles', string='Estado Ecleseástico')
    grado_acad = fields.Many2one(
        comodel_name='grado.acad', string='Grado Académico')
    especialidad = fields.Char('Especialidad')

    @api.multi
    def write(self, values):
        """En esta funcion manejo dos cosas>
         1- Si el checkbox teacher se marca o no, crear el profesor si no esta creado
            o activarlo o desactivarlo en caso que ya exista
         2- Si archivo el contacto tengo que archivar al profesor, pero si desarchivo el contacto ver en que
            estado esta el checkbox profesor para saber si archivar o desactivar el Profesor

            Nota: Para las lecturas de los profesores tuve que utilizar SQL porque si esta archivado, la funcion
            search no lo encuentra

            """
        for partner in self:
            res = super(Contacts, self).write(values)
            partner_id = partner.id
            query = (
                'SELECT id AS id FROM op_teacher WHERE partner_id = %s')
            params = tuple([partner_id])
            self.env.cr.execute(query, params)
            teacher = self.env.cr.dictfetchall()  # Tuve que leer con SQL porque con la funcion search()
            # obvia los que esten desactivados
            if len(teacher):
                teacher = self.env['op.teacher'].browse(teacher[0]['id'])
            if 'teacher' in values:
                if self.teacher:
                    if teacher:
                        teacher.active = True
                    else:
                        self.env['op.teacher'].create({'partner_id': partner.id})
                else:
                    if len(teacher):
                        teacher.active = False
            if not partner.active and 'active' in values:
                if teacher:
                    teacher.active = False
            if partner.active and 'active' in values and partner.teacher:
                if teacher:
                    teacher.active = True
            return res

    @api.model
    def create(self, vals):
        """
        Creando el profesor si el contacto es profesor
        """
        res = super(Contacts, self).create(vals)
        if res.teacher:
            self.env['op.teacher'].create({'partner_id': res.id})
        return res

    @api.multi
    def go_teacher_form(self):
        teacher = self.env['op.teacher'].search([('partner_id', '=', self.id)], limit=1)
        if teacher:
            action = self.env.ref('openeducat_gplus_core.action_op_teacher').read()[0]
            view_id = self.env.ref('openeducat_gplus_core.op_teacher_form')
            action.update({
                'res_id': teacher.id,
                'views': [(view_id.id, 'form')]
            })
            return action

    @api.multi
    def go_student_form(self):
        teacher = self.env['op.student'].search([('partner_id', '=', self.id)], limit=1)
        if teacher:
            action = self.env.ref('openeducat_gplus_core.action_op_student').read()[0]
            view_id = self.env.ref('openeducat_gplus_core.op_student_form')
            action.update({
                'res_id': teacher.id,
                'views': [(view_id.id, 'form')]
            })
            return action


class AutorityType(models.Model):
    _name = 'autority.type'  # TODO Poner permisos

    name = fields.Char('Nombre')


class Autority(models.Model):
    _name = 'autority'  # TODO Poner permisos

    name = fields.Char('Nombre')
    type = fields.Many2one(comodel_name='autority.type', required=True, string='Tipo de Autoridad')


class AutorityLine(models.Model):
    _name = 'autority.line'  # TODO Poner permisos
    _order = 'fecha_inicio desc'

    type = fields.Many2one(comodel_name='autority.type', required=True, string='Tipo de Autoridad')
    autority = fields.Many2one(comodel_name='autority', required=True, string='Autoridad')
    fecha_inicio = fields.Date(string='Inicio', required=True)
    fecha_fin = fields.Date(string='Fin')
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)


# Las clases meritos, sanciones, estado civil, estado ecleseastico, grado academico las puse en los contactos,
# aunque se vayan a ver des la ficha de
# profesores y estudiantes para crear un solo modelo que se asocie con el contacto y me sirva para ambos

class MeritosLine(models.Model):
    _name = 'merito.line'  # TODO Poner permisos
    _order = 'fecha desc'

    name = fields.Char('Merito')
    fecha = fields.Date(string='Fecha')
    autority = fields.Char('Autoridad que Aprobó')
    acuerdo = fields.Char('No. Acuerdo')
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)


class SancionesLine(models.Model):
    _name = 'sancion.line'  # TODO Poner permisos
    _order = 'fecha desc'

    name = fields.Char('Sanción')
    fecha = fields.Date(string='Fecha')
    autority = fields.Char('Autoridad que Aprobó')
    acuerdo = fields.Char('No. Acuerdo')
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)


class EstadoCivil(models.Model):
    _name = 'estado.civil'  # TODO Poner permisos

    name = fields.Char('Nombre')
    student = fields.Boolean('Visto en Estudiantes', default=True)
    teacher = fields.Boolean('Visto en Profesores', default=True)


class EstadoEcleseastico(models.Model):
    _name = 'estado.ecles'  # TODO Poner permisos

    name = fields.Char('Nombre')
    student = fields.Boolean('Visto en Estudiantes', default=True)
    teacher = fields.Boolean('Visto en Profesores', default=True)


class GradoAcademico(models.Model):
    _name = 'grado.acad'  # TODO Poner permisos

    name = fields.Char('Nombre')
    student = fields.Boolean('Visto en Estudiantes', default=True)
    teacher = fields.Boolean('Visto en Profesores', default=True)
