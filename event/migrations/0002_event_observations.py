# Generated by Django 3.1.7 on 2021-04-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='observations',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
