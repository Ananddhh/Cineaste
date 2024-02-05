from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    plot = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', default='movie_posters/Walter Mitty.jfif')
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1) 

    def __str__(self):
        return f"{self.user.username}'s favorite - {self.movie.title}"
