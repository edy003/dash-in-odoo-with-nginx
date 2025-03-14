{
    'name': 'Dash Integration',
    'version': '1.0',
    'summary': 'Intégration Dash pour Odoo 18',
    'description': """
        Module permettant d'intégrer une application Dash dans Odoo 18.
        Permet de visualiser des tableaux de bord interactifs directement dans Odoo.
    """,
    'category': 'Reporting',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/dash_template.xml',
        # 'views/menu_views.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'my_dash_module/static/src/js/dash_widget.js',
    #     ],
    # },
    'external_dependencies': {
        'python': ['dash', 'flask'],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
}