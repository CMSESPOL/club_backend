# Generated by Django 3.1.7 on 2021-05-31 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institution', '0006_suborg_dep'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborganization',
            name='members',
            field=models.ManyToManyField(related_name='list_of_branch_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
