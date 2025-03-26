@echo off
echo Starting Odoo and Dash services...

:: Définir les chemins
set ODOO_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\server\
set ADDONS_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\
set DB_NAME=ma_base_de_donnees
set DASH_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\my_dash_module\dash_app\
set NGINX_PATH=C:\Users\EDY\Desktop\mon_projet_odoo\addons\my_dash_module\setup\nginx-1.27.4
set PYTHON_EXE=C:\Users\EDY\Desktop\mon_projet_odoo\venv\Scripts\python.exe

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
if not exist "%PYTHON_EXE%" (
    echo Python du venv introuvable: %PYTHON_EXE%
    goto :error
)

:: Démarrer Odoo avec Python du venv
start cmd /k "cd /d %ODOO_PATH% && %PYTHON_EXE% odoo-bin --addons-path=%ADDONS_PATH% -d %DB_NAME%"

:: Démarrer Dash avec Python du venv
start cmd /k "cd /d %DASH_PATH% && %PYTHON_EXE% app.py"

:: Démarrer Nginx si ce n'est pas déjà fait
tasklist /FI "IMAGENAME eq nginx.exe" 2>NUL | find /I /N "nginx.exe">NUL
if "%ERRORLEVEL%"=="1" (
    cd /d %NGINX_PATH%
    start nginx.exe
)

echo Services started successfully!
echo Odoo: http://localhost:80
echo Dash: http://localhost:80/dash/

goto :end

:error
echo Une erreur s'est produite lors du démarrage des services.
pause
exit /b 1

:end
