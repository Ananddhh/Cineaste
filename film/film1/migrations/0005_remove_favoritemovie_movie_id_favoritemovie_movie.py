# Generated by Django 5.0 on 2024-01-02 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("film1", "0004_favoritemovie_delete_favorite"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favoritemovie",
            name="movie_id",
        ),
        migrations.AddField(
            model_name="favoritemovie",
            name="movie",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="film1.movie"
            ),
        ),
    ]
