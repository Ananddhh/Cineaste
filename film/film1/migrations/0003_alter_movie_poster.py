# Generated by Django 5.0 on 2023-12-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("film1", "0002_remove_movie_poster_url_movie_poster"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="poster",
            field=models.ImageField(
                default="movie_posters/default_poster.jfif", upload_to="movie_posters/"
            ),
        ),
    ]