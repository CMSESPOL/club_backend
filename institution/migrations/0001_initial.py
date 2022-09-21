# Generated by Django 3.1.7 on 2022-01-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('name', models.CharField(max_length=38, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('acronym', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=62)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('abbreviation', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('mission', models.CharField(default='', max_length=500)),
                ('vision', models.CharField(default='', max_length=500)),
                ('banner', models.JSONField(default=dict)),
                ('gallery', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SubOrganization',
            fields=[
                ('sub_org_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('gallery', models.JSONField(default=dict)),
            ],
        ),
    ]
