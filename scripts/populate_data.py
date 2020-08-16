import json
import os
from api.models import Genre, Movie

def get_or_create_genre(genre_name):
    return Genre.objects.get_or_create(name=genre_name)

def run(*args):
    file_handle = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
    with open(file_handle) as json_flie:
        data = json.load(json_flie)
    total_movies_count = len(data)
    for index, movie in enumerate(data):
        print("Adding {} of {} movies".format(index+1, total_movies_count))
        movie_instance = Movie.objects.create(name=movie['name'], _99_popularity=movie['99popularity'],
                                        director=movie['director'], imdb_score=movie['imdb_score'])
        for genre in movie['genre']:
            movie_genre, status = get_or_create_genre(genre.strip())
            movie_instance.genre.add(movie_genre)
