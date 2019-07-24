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
    qid = models.IntegerField(default=0)
    category = models.CharField(max_length=250)
    cost = models.IntegerField(default=0)
    requester = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='requester')
    worker = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker')
    report_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Image(models.Model):
    name = models.CharField(max_length=250)
    contentPath = models.ImageField(upload_to='images/', max_length=512)

    def __str__(self):
        return self.name

class ImageLabelingTask(Task):
    content = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Voice(models.Model):
    name = models.CharField(max_length=250)
    contentPath = models.FileField(upload_to='voices/', max_length=512)

    def __str__(self):
        return str(self.name)


class VoiceToTextTask(Task):
    content = models.ForeignKey(Voice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Text(Task):
    name = models.CharField(max_length=250)
    contentPath = models.FileField(upload_to='texts/', max_length=250)

class TextToVoiceTask(Task):
    content = models.ForeignKey(Text, on_delete=models.CASCADE)

class TextToTextTask(Task):
    content = models.ForeignKey(Text, on_delete=models.CASCADE)

class JobDone(models.Model):
    doer = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    verified = models.BooleanField(default = False)
    answerText = models.CharField(max_length=250, blank=True, null=True)
    answerFile = models.FileField(upload_to='answers/', blank=True, null=True)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)

 