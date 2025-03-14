# -*- coding: utf-8 -*-

import dash
from dash import html
import flask
import os

# Variable globale pour stocker l'instance de l'application
_dash_app = None

def get_dash_app(url_base_pathname='/'):
    """
    Obtient ou crée l'instance de l'application Dash
    
    Args:
        url_base_pathname (str): Chemin de base pour l'URL de l'application
        
    Returns:
        dash.Dash: L'application Dash configurée
    """
    global _dash_app
    
    # Si l'application existe déjà, la retourner
    if _dash_app is not None:
        return _dash_app
    
    # Créer une instance Flask
    server = flask.Flask(__name__)
    
    # Obtenir le chemin du dossier des assets
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_dir, 'assets')
    
    # Créer l'application Dash
    app = dash.Dash(
        __name__,
        server=server,
        # Utilisez uniquement url_base_pathname, pas requests_pathname_prefix
        url_base_pathname=url_base_pathname,
        assets_folder=assets_path,
        title='Tableau de bord Odoo-Dash',
        suppress_callback_exceptions=True
    )
    
    # Définir la mise en page simple
    app.layout = html.Div([
        html.H1("Bonjour depuis Dash intégré dans Odoo!", 
                style={"textAlign": "center", "marginTop": "50px", "color": "#875A7B"})
    ])
    
    # Stocker l'application pour ne pas la recréer à chaque appel
    _dash_app = app
    
    return app

# Pour le test direct (sera ignoré lorsqu'importé dans Odoo)
if __name__ == '__main__':
    app = get_dash_app('/')
    app.run_server(debug=True, host='127.0.0.1', port=8050)