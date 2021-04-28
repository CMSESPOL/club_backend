# Generated by Django 3.1.7 on 2021-04-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('abbreviation', models.CharField(default='NONAME', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=38)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubOrganization',
            fields=[
                ('sub_org_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=38)),
                ('description', models.CharField(max_length=100)),
                ('id_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('name', models.CharField(max_length=38, primary_key=True, serialize=False)),
                ('id_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.faculty')),
            ],
        ),
    ]
