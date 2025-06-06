import os
import django
from random import choice

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
