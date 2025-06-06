from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from account.models import Account
from music.models import Song, Playlist

class LoginViewTestCase(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            nombre="prueba",
            apellido="prueba",
            username="prueba",
            email="prueba@gmail.com",
            password="prueba",
        )

    def test_login_successful(self):
        url = reverse('login')  # Asegúrate de que esta ruta esté nombrada como 'login'
        data = {
            "username": "prueba",
            "password": "prueba"
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)




class PlaylistTestCase(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            nombre="prueba",
            apellido="prueba",
            username="prueba",
            email="prueba@example.com",
            password="prueba"
        )
        self.song1 = Song.objects.create(
            title="Song A",
            artist="Artist A"
        )
        self.song2 = Song.objects.create(
            title="Song B",
            artist="Artist B"
        )
        self.login_url = reverse('login')

    def authenticate(self):
        response = self.client.post(self.login_url, {
            "username": "prueba",
            "password": "prueba"
        }, format='json')
        self.token = response.data['token']['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        

    def test_create_playlist(self):
        self.authenticate()
        url = reverse('playlist-list')  # Usa el nombre del router
        data = {
            "name": "Mi Playlist Test",
            "description": "Descripción de prueba",
            "song_ids": [self.song1.id, self.song2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Mi Playlist Test")
        
        
    def test_create_playlist_unauthenticated(self):
        url = reverse('playlist-list')
        data = {
            "name": "Mi Playlist",
            "description": "No autorizado",
            "song_ids": [self.song1.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
