from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to="profiles/images/", null=True, blank=True)
    bank_account = models.CharField(max_length=20, default=-1)

    def __str__(self):
        return self.phone


class Document(models.Model):
    doc_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.doc_file.name

class Dataset(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE, null=True, blank=True)
    dataType = models.CharField(max_length=250)

    def __str__(self):
        return self.document.doc_file.name

class Task(models.Model):
    question = models.CharField(max_length=250, default="")
    answerChoices = models.CharField(max_length=250, blank=True, null=True)
    qid = models.IntegerField()
    cost = models.IntegerField(default=0)
    requester = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='requester')
    worker = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker')
    report_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Image(models.Model):
    name = models.CharField(max_length=250)
    contentPath = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class ImageLabelingTask(Task):
    content = models.OneToOneField(Image, on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Voice(models.Model):
    name = models.CharField(max_length=250)
    contentPath = models.FileField(upload_to='voices/', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class VoiceToTextTask(Task):
    content = models.OneToOneField(Voice, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)

class TextToVoiceTask(Task):
    content = models.CharField(max_length=250)
    answer = models.FileField(upload_to='voices/')


class TextToTextTask(Task):
    content = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)

 