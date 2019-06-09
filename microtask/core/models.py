from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    avatar = models.ImageField()

    def __str__(self):
        return self.phone_num

