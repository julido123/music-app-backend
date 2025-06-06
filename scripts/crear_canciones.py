import os
import django
from random import choice
import sys

# Agregar el path del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_api.settings')
django.setup()

from music.models import Song

artists = ["Artist A", "Artist B", "Artist C"]
albums = ["Album X", "Album Y", "Album Z"]

for i in range(1, 31):
    Song.objects.get_or_create(
        title=f"Song {i}",
        artist=choice(artists),
        album=choice(albums)
    )

print("🎶 30 canciones creadas correctamente.")
