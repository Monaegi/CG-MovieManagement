from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    USER_TYPE_DJANGO = 'D'
    USER_TYPE_FACEBOOK = 'F'
    USER_TYPE_NAVER = 'N'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
        (USER_TYPE_NAVER, 'Naver'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default="D")
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return self.nickname or self.email