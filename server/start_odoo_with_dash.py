#!/usr/bin/env python3
# Fichier: start_odoo_with_dash.py

import sys
import os

# Ajouter le chemin personnalisé des addons au PYTHONPATH
custom_addons_path = r"C:\Users\EDY\Desktop\mon_projet_odoo\addons"
if custom_addons_path not in sys.path:
    sys.path.append(custom_addons_path)

# Importer Odoo
import odoo

# Hook à exécuter après le démarrage d'Odoo
def setup_dash_middleware():
    try:
        # S'assurer que le module est chargé
        from odoo.modules.module import load_openerp_module
        load_openerp_module('my_dash_module')
        
        # Maintenant, nous pouvons importer depuis notre module
        # On utilise une approche plus directe pour l'importation
        sys.path.append(os.path.join(custom_addons_path, 'my_dash_module'))
        from controllers.dash_controller import init_dash_app
        
        # Obtenir l'instance Root d'Odoo
        from odoo.http import root
        
        # Remplacer l'application WSGI par notre middleware
        root.application = init_dash_app()
        
        print("Intégration Dash chargée avec succès!")
    except Exception as e:
        print(f"Erreur lors du chargement de l'intégration Dash: {e}")
        import traceback
        traceback.print_exc()

# Patching du main d'Odoo pour exécuter notre middleware après démarrage
original_main = odoo.cli.main
def patched_main():
    # Exécuter le main original d'Odoo
    result = original_main()
    
    # Configurer notre middleware Dash
    setup_dash_middleware()
    
    return result

# Remplacer le main d'Odoo par notre version patchée
odoo.cli.main = patched_main

if __name__ == "__main__":
    # S'assurer que notre chemin d'addons est dans les options
    odoo_args = sys.argv[1:]
    
    # Vérifier si --addons-path est déjà spécifié
    addons_path_specified = any(arg.startswith('--addons-path=') for arg in odoo_args)
    
    # Ajouter notre chemin d'addons s'il n'est pas déjà spécifié
    if not addons_path_specified:
        odoo_args.append(f'--addons-path={custom_addons_path},C:\\Users\\EDY\\Desktop\\mon_projet_odoo\\server\\odoo\\addons')
    
    # Remplacer les arguments
    sys.argv[1:] = odoo_args
    
    # Exécuter Odoo avec notre patch
    sys.exit(odoo.cli.main())