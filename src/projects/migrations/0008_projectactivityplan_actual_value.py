# Generated by Django 2.1.5 on 2020-05-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectactivityplan_plan_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectactivityplan',
            name='actual_value',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
