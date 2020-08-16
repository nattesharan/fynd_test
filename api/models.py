from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    _99_popularity = models.FloatField(validators=[MinValueValidator(0, message='The value should be in between 0 to 100'),
                                                MaxValueValidator(100, message='The value should be in between 0 to 100')], default=0)
    director = models.CharField(max_length=512, blank=False, null=False)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.FloatField(validators=[MinValueValidator(0, message='The value should be in between 0 to 10'),
                                                MaxValueValidator(10, message='The value should be in between 0 to 10')], default=0)
    name = models.CharField(max_length=512, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def movie_genres(self):
        genres = []
        for genre in self.genre.all():
            genres.append(genre.name)
        return genres
    
