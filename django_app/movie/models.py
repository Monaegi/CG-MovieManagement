import json

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from config import settings

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    director = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    content = models.TextField()
    link = models.TextField(max_length=255)
    userRating = models.IntegerField()
    poster_image = models.ImageField(upload_to='movie', blank=False)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    rating_by_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Comment',
        related_name='user_rating'
    )


class SelectedMovie(models.Model):
    movie = models.ForeignKey(Movie)
    selector = models.CharField(max_length=10)
    selected_date = models.CharField(max_length=15)
    reviewer = models.ManyToManyField(User)


class Comment(models.Model):
    movie = models.ForeignKey(Movie)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    ratings = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
