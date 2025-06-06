# 🎵 API de Música - Django + DRF

Este es un proyecto de backend para una aplicación de música desarrollado con **Python 3.11.9**, **Django** y **Django REST Framework**, utilizando una base de datos **PostgreSQL**.

---

## 🚀 Requisitos

- Python 3.11.9  
- PostgreSQL 13

---

## ⚙️ Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/julido123/music-app-backend
cd music-app-backend
```

### 2. Crear base de datos en PostgreSQL

Antes de correr el proyecto, asegúrate de tener PostgreSQL instalado y crea una base de datos vacía. Por defecto se espera que sea:

- **Nombre**: `music_db`
- **Usuario**: `postgres`
- **Contraseña**: `12345`
- **Host**: `localhost`
- **Puerto**: `5432`

Si tus datos son distintos, actualízalos en el archivo `settings.py` en la línea **89**, que contiene la siguiente configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'music_db',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🧰 Opción 1: Usar el script automático `setup.bat` (solo en Windows)

Si estás en Windows, puedes ejecutar el script `setup.bat` desde una consola PowerShell con el siguiente comando:

```powershell
.\setup.bat
```

Este script realizará los siguientes pasos por ti:

1. Crea un entorno virtual (`venv`)
2. Activa el entorno virtual
3. Instala las dependencias de `requirements.txt`
4. Ejecuta las migraciones necesarias
5. Crea un usuario administrador por defecto:
   - **Usuario**: `admin`
   - **Contraseña**: `admin123`
6. Crea canciones de ejemplo para probar la app
7. Inicia automáticamente el servidor local

✅ Luego de esto, puedes empezar a usar la app desde el frontend, desde el panel de administración (`/admin`) o desde la documentación Swagger.

🔁 En futuras ocasiones, solo debes activar el entorno virtual y correr el servidor con:

```bash
venv\Scripts\activate
python manage.py runserver
```

---

## 🛠️ Opción 2: Instalación paso a paso manual

Si prefieres hacerlo manualmente o estás en un sistema que no sea Windows, sigue estos pasos:

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

- En **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- En **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Crear canciones de ejemplo (opcional)

```bash
python scripts/crear_canciones.py
```

### 7. Correr el servidor

```bash
python manage.py runserver
```

---

## 📚 Documentación de la API

Documentación Swagger (interactiva):

👉 [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

Documentación Redoc (más detallada):

👉 [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---

## 👤 Acceso al panel de administración

Accede a:  
👉 [http://localhost:8000/admin/](http://localhost:8000/admin/)

Puedes usar el usuario creado por el `setup.bat` (`admin` / `admin123`) o el que hayas creado manualmente.

---

## 🧪 Tests

Para ejecutar los tests unitarios:

```bash
python manage.py test
```

---

## 🧩 Estructura principal
- `music_api/` → Módulo principal que contiene los archivos `setting.py` y `urls.py`.
- `music/` → App principal que contiene los modelos `Playlist` y `Song`.
- `account/` → App para autenticación y gestión de usuarios.
- `scripts/crear_superusuario.py` → Script para crear un superusuario por defecto.
- `scripts/crear_canciones.py` → Script para crear canciones de prueba.
- `setup.bat` → Automatiza la configuración del entorno en Windows.
- `drf-spectacular` → Generador de documentación OpenAPI (Swagger/Redoc).

---

## ✅ Notas adicionales

- Siempre activa tu entorno virtual antes de ejecutar comandos de Django.
- Puedes modificar los scripts en `scripts/` si deseas crear datos personalizados para pruebas.
- El backend está preparado para integrarse con un frontend en Angular o cualquier otro framework.

---
