# Generated by Django 2.2.1 on 2019-07-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190718_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='answerChoices',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='qid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='question',
            field=models.CharField(default='', max_length=250),
        ),
    ]
