from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
