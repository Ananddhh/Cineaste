from django.contrib import admin
from .models import Movie, FavoriteMovie, Genre

admin.site.register(Movie)
admin.site.register(FavoriteMovie)
admin.site.register(Genre)
