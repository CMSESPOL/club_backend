# Generated by Django 3.1.7 on 2021-04-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.JSONField(default=[]),
        ),
    ]
