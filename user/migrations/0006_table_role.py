# Generated by Django 3.1.7 on 2021-04-23 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_member_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'Presidente'), ('B', 'Vicepresidente'), ('C', 'Secretario'), ('D', 'Tesorero'), ('E', 'Vocal'), ('F', 'Miembro'), ('N', 'Ninguno'), ('X', 'Asesor'), ('Y', 'Tutor'), ('Z', 'Externo')], default='F', max_length=2)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('id_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='actual_role',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.memberrole'),
        ),
    ]