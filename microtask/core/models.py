from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to="profiles/images/", null=True, blank=True)
    bank_account = models.CharField(max_length=20)

    def __str__(self):
        return self.phone


class Document(models.Model):
    doc_file = models.FileField(upload_to='documents/%Y/%m/%d')


class Dataset(models.Model):
    IMG2TXT = 'I2T'
    VOICE2TXT = 'V2T'
    TXT2TXT = 'T2T'
    TXT2VOICE = 'T2V'
    DATASET_TYPE_CHOICES = (
        (IMG2TXT, 'Image Labeling'),
        (VOICE2TXT, 'Voice To Text'),
        (TXT2TXT, 'Text To Text'),
        (TXT2VOICE, 'Text To Voice')
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
