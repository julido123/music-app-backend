@echo off
echo 🚀 Iniciando setup...

REM Crear entorno virtual
python -m venv venv

REM Activar entorno virtual
call venv\Scripts\activate

REM Instalar dependencias
echo 📦 Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

REM Migraciones
echo 🧱 Ejecutando migraciones...
python manage.py makemigrations
python manage.py migrate

REM Crear superusuario
echo 👤 Creando superusuario...
python scripts\crear_superusuario.py

REM Crear canciones
echo 🎵 Creando canciones...
python scripts\crear_canciones.py

echo ✅ Todo listo. Puedes iniciar el servidor con:
echo venv\Scripts\activate && python manage.py runserver
pause
