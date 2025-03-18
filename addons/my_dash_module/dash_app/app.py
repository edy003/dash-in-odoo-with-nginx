# -*- coding: utf-8 -*-
import dash
from dash import html
import logging

_logger = logging.getLogger(__name__)

def create_dash_app():
    
    """Créer et configurer l'application Dash"""
    app = dash.Dash(
        __name__,
        requests_pathname_prefix='/dash/',  # Corrige les erreurs de chemin derrière Nginx
        routes_pathname_prefix='/dash/',    # Corrige le loading infini
        assets_url_path='/dash/assets'      # Corrige le chargement des fichiers statiques
    )

    # Layout simple
    app.layout = html.H1(
        "Bonjour depuis Dash intégré dans Odoo!",
        style={"textAlign": "center", "marginTop": "50px", "color": "#875A7B"}
    )

    return app

# Démarrage de l'application
if __name__ == '__main__':
    app = create_dash_app()
    app.run_server(debug=True, host='127.0.0.1', port=8050, dev_tools_ui=True)
