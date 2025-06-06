from rest_framework import viewsets
from music.models import Playlist, Song
from .serializers import PlaylistSerializer, SongSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    list=extend_schema(tags=['Playlists']),
    retrieve=extend_schema(tags=['Playlists']),
    create=extend_schema(tags=['Playlists']),
    update=extend_schema(tags=['Playlists']),
    partial_update=extend_schema(tags=['Playlists']),
    destroy=extend_schema(tags=['Playlists']),
)
class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    list=extend_schema(tags=['Songs']),
    retrieve=extend_schema(tags=['Songs']),
    create=extend_schema(tags=['Songs']),
    update=extend_schema(tags=['Songs']),
    partial_update=extend_schema(tags=['Songs']),
    destroy=extend_schema(tags=['Songs']),
)
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer