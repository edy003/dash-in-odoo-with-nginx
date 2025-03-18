# -*- coding: utf-8 -*-
import sys
import os
from addons.my_dash_module.dash_app.app import create_dash_app

if __name__ == '__main__':
    app = create_dash_app()
    app.run_server(debug=False, host='127.0.0.1', port=8050)