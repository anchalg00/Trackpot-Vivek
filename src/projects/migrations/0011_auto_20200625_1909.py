# Generated by Django 2.1.5 on 2020-06-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_scheduleinfo_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledocument',
            name='cover',
        ),
        migrations.AddField(
            model_name='scheduledocument',
            name='file_url',
            field=models.FileField(default=None, upload_to='schedule_files/'),
            preserve_default=False,
        ),
    ]
