# Generated by Django 3.1.7 on 2021-05-31 02:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('permissions', models.CharField(choices=[('A', 'Presidente'), ('B', 'Vicepresidente'), ('C', 'Sub Organización'), ('D', 'Miembro'), ('N', 'Ninguno')], default='N', max_length=1)),
                ('ambassador', models.URLField(blank=True, max_length=300, null=True, unique=True, validators=[user.validators.ambassador_valid_url])),
                ('social_links', models.JSONField(blank=True, default=dict, null=True)),
                ('active', models.BooleanField(default=True)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('card_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('born_date', models.DateField()),
                ('genre', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('signature', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_role', models.CharField(choices=[('P', 'Presidente'), ('V', 'Vicepresidente'), ('S', 'Secretario'), ('T', 'Tesorero'), ('V', 'Vocal'), ('M', 'Miembro'), ('N', 'Ninguno'), ('A', 'Asesor'), ('T', 'Tutor'), ('E', 'Externo'), ('C', 'Candidato Aspirante')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('P', 'Presidente'), ('V', 'Vicepresidente'), ('S', 'Secretario'), ('T', 'Tesorero'), ('V', 'Vocal'), ('M', 'Miembro'), ('N', 'Ninguno'), ('A', 'Asesor'), ('T', 'Tutor'), ('E', 'Externo'), ('C', 'Candidato Aspirante')], default='M', max_length=1)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('id_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='user.person')),
                ('enrollment_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('level', models.CharField(choices=[('101', '100-I'), ('102', '100-II'), ('201', '200-I'), ('202', '200-II'), ('301', '300-I'), ('302', '300-II'), ('401', '400-I'), ('402', '400-II')], max_length=6)),
                ('photo', models.CharField(blank=True, max_length=100, null=True)),
                ('id_career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institution.career')),
                ('id_member', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('user.person',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.person')),
                ('id_faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institution.faculty')),
            ],
            bases=('user.person',),
        ),
    ]
