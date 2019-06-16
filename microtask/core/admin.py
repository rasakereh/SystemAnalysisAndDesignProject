from django.contrib import admin
from core.models import Profile, Document, Dataset
# Register your models here.
admin.site.register([Profile, Dataset, Document])
