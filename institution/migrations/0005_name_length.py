# Generated by Django 3.1.7 on 2021-05-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20210508_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='suborganization',
            name='sub_org_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
