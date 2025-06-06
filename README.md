# 🎵 API de Música - Django + DRF

Este es un proyecto de backend para una aplicación de música desarrollado con **Python 3.11.9**, **Django** y **Django REST Framework**, utilizando una base de datos **PostgreSQL**.

## 🚀 Requisitos

- Python 3.11.9
- PostgreSQL
- `virtualenv` (opcional pero recomendado)

---

## ⚙️ Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuración de base de datos

Asegúrate de tener PostgreSQL instalado y en funcionamiento. Crea una base de datos llamada `music_db` con los siguientes datos por defecto:

```python
# settings.py

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

> Si tus datos de conexión son diferentes, actualízalos directamente en el archivo `settings.py`.

---

## 🛠️ Migraciones

Después de configurar la base de datos, corre los siguientes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Usuario administrador

Para acceder al panel de administración:

1. Crear un superusuario:

```bash
python manage.py createsuperuser
```

2. Accede a:  
👉 http://localhost:8000/admin/

Aquí podrás gestionar modelos como usuarios, canciones y playlists (si están registrados).

---

## 🧪 Correr el servidor

```bash
python manage.py runserver
```

---

## 📚 Documentación de la API

La documentación interactiva de la API está disponible en Swagger:

👉 http://localhost:8000/api/docs/

También puedes acceder a Redoc si lo prefieres:

👉 http://localhost:8000/api/redoc/

---

## 🧪 Tests

Para ejecutar los tests unitarios:

```bash
python manage.py test
```

---

## 🧩 Estructura principal

- `music/` → App principal que contiene los modelos `Playlist` y `Song`.
- `account/` → App para la autenticación y gestión de usuarios.
- `music.api.urls` → Define las rutas de la API.
- `drf-spectacular` → Generador de documentación OpenAPI (Swagger/Redoc).

---

## ✅ Notas adicionales

- Recuerda siempre activar tu entorno virtual antes de trabajar en el proyecto.
- Puedes modificar o extender los modelos y serializers para agregar más funcionalidades como autenticación por token, filtros, búsquedas, etc.

---

## 📬 Contacto

Para preguntas o soporte, contacta a [tu_email@ejemplo.com].