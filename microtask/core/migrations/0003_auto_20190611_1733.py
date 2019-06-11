# Generated by Django 2.2.1 on 2019-06-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190609_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bank_account',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/images/'),
        ),
    ]
