# Generated by Django 4.1.3 on 2022-11-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_alter_suborganization_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborganization',
            name='description',
            field=models.TextField(),
        ),
    ]
