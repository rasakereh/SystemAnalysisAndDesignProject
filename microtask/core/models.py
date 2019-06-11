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

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Dataset(models.Model):
    IMG2TXT = 'I2T'
    VOICE2TXT = 'V2T'
    TXT2TXT = 'T2T'
    DATASET_TYPE_CHOICES = (
        (IMG2TXT, 'images'),
        (VOICE2TXT, 'voices'),
        (TXT2TXT, 'texts'),
    )
    root = models.CharField(max_length=250)
    dataType = models.CharField(
        max_length=3,
        choices=DATASET_TYPE_CHOICES,
    )

'''
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    for_all = models.BooleanField()
    image_name = models.ImageField()
    answer_options = models.CharField(max_length=4096)

class Answer(models.Model):
    qid = models.AutoField(primary_key=True)
'''
