# -*- coding: utf-8 -*-
{
    'name': "Intégration Dash",
    'summary': """
        Intégration de Dash pour la visualisation de données dans Odoo
    """,
    'description': """
        Ce module permet d'intégrer des tableaux de bord Dash dans l'interface d'Odoo.
        Les visualisations sont accessibles via un menu dédié et peuvent être intégrées
        dans différentes vues.
    """,
    'author': "EDY",
    'website': "",
    'category': 'Outils',
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/dashboard_views.xml',
        'views/dashboard_template.xml',
        'views/menu_views.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/dashboard_templates.xml',
    # ],
    'installable': True,
    'application': True,
}