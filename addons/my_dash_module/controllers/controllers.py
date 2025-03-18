# # -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request

# class DashController(http.Controller):
    
#     @http.route('/dashboard/dash/', type='http', auth='public', website=True)
#     def serve_dash(self, **kwargs):
#         """Affiche la page contenant l'application Dash intégrée dans Odoo"""
#         return request.render('my_dash_module.dashboard_template', {})


# from odoo import http
# from odoo.http import request

# class DashController(http.Controller):
#     @http.route('/dashboard/dash/', auth='user', website=True)
#     def render_dash(self, **kwargs):
#         return request.redirect('http://localhost:8050/dash/')  # Redirige vers l'application Dash

# -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request

# class DashController(http.Controller):

#     @http.route('/dashboard/dash/', type='http', auth='user', website=True)
#     def serve_dash(self, **kwargs):
#         """Affiche la page Odoo contenant un iframe avec Dash"""
#         return request.render('my_dash_module.dashboard_template', {})

# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class DashController(http.Controller):

    @http.route('/dashboard/dash/', type='http', auth='user', website=True)
    def serve_dash(self, **kwargs):
        """Affiche une page avec une iframe pour intégrer Dash dans Odoo"""
        return request.render('my_dash_module.dashboard_template', {
            'dash_url': "http://127.0.0.1:8050/dash/"
        })

