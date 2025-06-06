from django.contrib.auth import get_user_model
import os
import django
import sys

# Agregar el path del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_api.settings')
django.setup()

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        nombre="Admin",
        apellido="User",
        username="admin",
        email="admin@example.com",
        password="admin123",
        cedula="1234567890"
    )
    print("✅ Superusuario creado.")
else:
    print("⚠️  El superusuario ya existe.")
