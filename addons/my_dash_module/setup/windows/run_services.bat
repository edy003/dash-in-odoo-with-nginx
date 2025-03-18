@echo off
echo Starting Odoo and Dash services...

:: Définir les chemins
set ODOO_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\server\
set ADDONS_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\
set DB_NAME=ma_base_de_donnees
set DASH_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\my_dash_module\dash_app\
set NGINX_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\my_dash_module\setup\nginx-1.27.4
set VENV_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\venv\Scripts\activate.bat

:: Vérifier que les chemins existent
if not exist "%ODOO_PATH%" (
    echo Le chemin d'Odoo n'existe pas: %ODOO_PATH%
    goto :error
)
if not exist "%DASH_PATH%" (
    echo Le chemin de Dash n'existe pas: %DASH_PATH%
    goto :error
)
if not exist "%NGINX_PATH%" (
    echo Le chemin de Nginx n'existe pas: %NGINX_PATH%
    goto :error
)

:: Start Odoo avec l'environnement virtuel
start cmd /k "if exist "%VENV_PATH%" (call "%VENV_PATH%" & cd %ODOO_PATH% & python odoo-bin --addons-path=%ADDONS_PATH% -d %DB_NAME%) else (echo Environnement virtuel non trouvé & pause)"

:: Start Dash avec l'environnement virtuel (directement dans le dossier de l'app)
start cmd /k "if exist "%VENV_PATH%" (call "%VENV_PATH%" & cd %DASH_PATH% & python app.py) else (echo Environnement virtuel non trouvé & pause)"

:: Start Nginx if not already running
tasklist /FI "IMAGENAME eq nginx.exe" 2>NUL | find /I /N "nginx.exe">NUL
if "%ERRORLEVEL%"=="1" (
    cd %NGINX_PATH%
    start nginx.exe
)

echo Services started successfully!
echo Odoo: http://localhost:80
echo Dash: http://localhost:80/dash/

:: Informations pour la première connexion
echo.
echo IMPORTANT: Lors de la première connexion à Odoo:
echo 1. Accédez à http://localhost:80
echo 2. Créez votre base de données avec vos identifiants administrateur
echo 3. Utilisez ces mêmes identifiants pour les connexions futures
echo.

goto :end

:error
echo Une erreur s'est produite lors du démarrage des services.
pause
exit /b 1

:end