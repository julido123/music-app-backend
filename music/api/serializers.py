from rest_framework import serializers
from music.models import Playlist, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    song_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Song.objects.all(), write_only=True, source='songs'
    )

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'songs', 'song_ids', 'created_at']
