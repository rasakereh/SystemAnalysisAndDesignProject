from django.contrib import admin
from core.models import Profile, Document, Dataset, Task, JobDone, Image, ImageLabelingTask, Transaction, Wallet, TextToTextTask, TextToVoiceTask, VoiceToTextTask, Voice
# Register your models here.
admin.site.register([Profile,
                    Dataset,
                    Task,
                    JobDone,
                    Document,
                    Image,
                    ImageLabelingTask,
                    Transaction,
                    Wallet,
                    TextToTextTask,
                    TextToVoiceTask,
                    VoiceToTextTask,
                    Voice ])
