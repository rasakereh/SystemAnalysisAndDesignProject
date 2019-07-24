# Generated by Django 2.2.1 on 2019-07-24 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Task')),
                ('name', models.CharField(max_length=250)),
                ('contentPath', models.FileField(blank=True, null=True, upload_to='texts/')),
            ],
            bases=('core.task',),
        ),
        migrations.RemoveField(
            model_name='imagelabelingtask',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='texttotexttask',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='texttovoicetask',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='voicetotexttask',
            name='answer',
        ),
        migrations.AlterField(
            model_name='texttotexttask',
            name='content',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Text'),
        ),
        migrations.AlterField(
            model_name='texttovoicetask',
            name='content',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Text'),
        ),
    ]