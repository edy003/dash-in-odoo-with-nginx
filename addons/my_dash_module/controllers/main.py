# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, Response
import dash
from dash import html
import flask
import threading
import time
import logging

_logger = logging.getLogger(__name__)

# Variable globale pour stocker l'application Dash
_dash_server = None
_dash_thread = None

def start_dash_server():
    """Démarre le serveur Dash dans un thread séparé"""
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1("Bonjour depuis Dash intégré dans Odoo!", 
                style={"textAlign": "center", "marginTop": "50px", "color": "#875A7B"})
    ])
    
    # Démarrer le serveur sur un port différent
    app.run_server(debug=False, host='127.0.0.1', port=8050)

class DashController(http.Controller):
    
    @http.route('/my_dash_module/dash/', auth='public', type='http', website=True)
    def dash_page(self, **kwargs):
        """Affiche la page du tableau de bord avec l'iframe"""
        global _dash_thread
        
        # Démarrer le serveur Dash s'il n'est pas déjà en cours d'exécution
        if _dash_thread is None or not _dash_thread.is_alive():
            _logger.info("Démarrage du serveur Dash...")
            _dash_thread = threading.Thread(target=start_dash_server)
            _dash_thread.daemon = True
            _dash_thread.start()
            
            # Attendre que le serveur démarre
            time.sleep(2)
        
        return request.render("my_dash_module.dash_template", {})