import pytest

from django.conf import settings
import os
import json
from api.models import Movie, Genre
pytest_plugins = [
   "fixtures.user"
]

def get_or_create_genre(genre_name):
    return Genre.objects.get_or_create(name=genre_name)

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        handle = os.path.join(settings.BASE_DIR, 'scripts/data.json')
        with open(handle) as json_flie:
            data = json.load(json_flie)
            total_movies_count = len(data)
            for index, movie in enumerate(data):
                print("Adding {} of {} movies".format(index+1, total_movies_count))
                movie_instance = Movie.objects.create(name=movie['name'], _99_popularity=movie['99popularity'],
                                                director=movie['director'], imdb_score=movie['imdb_score'])
                for genre in movie['genre']:
                    movie_genre, status = get_or_create_genre(genre.strip())
                    movie_instance.genre.add(movie_genre)