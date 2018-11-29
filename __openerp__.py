# -*- coding: utf-8 -*-
{
    'name': "openeducat_gplus_core",

    'summary': """
        Modulo para gestion de Escuelas. Incluye Contactos, Estudiantes, Profesores y Pensum.""",

    'description': """
        Modulo para gestion de Escuelas. Incluye Contactos, Estudiantes, Profesores y Pensum.
    """,

    'author': "3C",
    'website': "http://www.grupoconsultor3c.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Educacion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'res_partner_town'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views_contacts.xml',
        'views/views_teacher.xml',
        'views/views_student.xml',
        'data/data_autority.xml',
        'data/data_info2_teacher_student.xml',
        'views/templates.xml',
        'views/views_subject.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
