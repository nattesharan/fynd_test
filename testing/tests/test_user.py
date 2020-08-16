import pytest
from django.test import TestCase
from api.models import Movie, Genre
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_data():
    movies = Movie.objects.all().count()
    genres = Genre.objects.all().count()
    assert movies > 0
    assert genres > 1

@pytest.mark.django_db
class TestAdminUserActions:
    client = APIClient()
    @pytest.fixture(autouse=True)
    def admin_user(self, admin_user):
        self.user = admin_user
        token, success = Token.objects.get_or_create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
    def test_get_movies(self):
        response = self.client.get('/api/v1/movies/')
        assert response.status_code == 200
        data = response.json()
        assert len(data)
    
    def test_delete_movie(self):
        movie = Movie.objects.first()
        response = self.client.delete('/api/v1/movies/{}/'.format(movie.pk))
        assert response.status_code == 204

    def test_fetch_genres(self):
        response = self.client.get('/api/v1/genres/')
        assert response.status_code == 200
        data = response.json()
        assert len(data)
    
    def test_edit_genre(self):
        genre = Genre.objects.first()
        url_endpoint = '/api/v1/genres/{}/'.format(genre.pk)
        response = self.client.get(url_endpoint)
        assert response.status_code == 200
        genre = response.json()
        genre['name'] += ' Test'
        response = self.client.put(url_endpoint, data=genre)
        assert response.status_code == 200
        response = self.client.get(url_endpoint)
        assert response.status_code == 200
        genre = response.json()
        assert genre['name'].endswith('Test')

@pytest.mark.django_db
class TestUserActions:
    client = APIClient()
    @pytest.fixture(autouse=True)
    def user(self, user):
        self.user = user
        token, success = Token.objects.get_or_create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
    def test_get_movies(self):
        response = self.client.get('/api/v1/movies/')
        assert response.status_code == 200
        data = response.json()
        assert len(data)
    
    def test_delete_movie(self):
        movie = Movie.objects.first()
        response = self.client.delete('/api/v1/movies/{}/'.format(movie.pk))
        assert response.status_code == 403

    def test_fetch_genres(self):
        response = self.client.get('/api/v1/genres/')
        assert response.status_code == 200
        data = response.json()
        assert len(data)
    
    def test_edit_genre(self):
        genre = Genre.objects.first()
        url_endpoint = '/api/v1/genres/{}/'.format(genre.pk)
        response = self.client.get(url_endpoint)
        assert response.status_code == 200
        genre = response.json()
        genre['name'] += ' Test'
        response = self.client.put(url_endpoint, data=genre)
        assert response.status_code == 403
        
@pytest.mark.django_db
class TestUserWithFixture:
    def test_create_user(self, user, admin_user):
        users = User.objects.all().count()
        assert users
