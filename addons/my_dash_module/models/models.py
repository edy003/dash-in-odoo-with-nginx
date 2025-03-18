# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DashDashboard(models.Model):
    _name = 'dash.dashboard'
    _description = 'Tableau de bord Dash'

    name = fields.Char('Nom', required=True)
    url_path = fields.Char('Chemin URL', required=True, 
                         help="Chemin relatif vers le tableau de bord Dash (ex: /dash/)")
    is_active = fields.Boolean('Actif', default=True)
    description = fields.Text('Description')
    
    # Relations avec d'autres modèles si nécessaire
    # user_ids = fields.Many2many('res.users', string='Utilisateurs autorisés')
    
    def open_dashboard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': self.url_path,
            'target': 'new',
        }