from django.contrib import admin
from api.models import Genre, Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'created_on')
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
# testUser123