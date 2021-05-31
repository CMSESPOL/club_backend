from user.validators import ambassador_valid_url
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.mail import send_mail
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

GENRES = [
    ('M', 'Masculino'),
    ('F', 'Femenino')
]

LEVELS = [
    ('101', '100-I'),
    ('102', '100-II'),
    ('201', '200-I'),
    ('202', '200-II'),
    ('301', '300-I'),
    ('302', '300-II'),
    ('401', '400-I'),
    ('402', '400-II'),
]

ROLES = [
    ('P', 'Presidente'),
    ('V', 'Vicepresidente'),
    ('S', 'Secretario'),
    ('T', 'Tesorero'),
    ('V', 'Vocal'),
    ('M', 'Miembro'),
    ('N', 'Ninguno'),
    ('A', 'Asesor'),
    ('T', 'Tutor'),
    ('E', 'Externo'),
    ('C', 'Candidato Aspirante'),
]

PERMISSIONS = [
    ('A', 'Presidente'),
    ('B', 'Vicepresidente'),
    ('C', 'Sub Organización'),
    ('D', 'Miembro'),
    ('N', 'Ninguno')
]

class Person(models.Model):
    card_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    born_date = models.DateField(auto_now=False)
    genre = models.CharField(max_length=1, choices=GENRES)
    signature = models.CharField(max_length=100, blank=True, null=True)
    actual_role = models.CharField(max_length=1, choices=ROLES, default='N')

    def __str__(self):
        return f"{self.card_id}"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

class Professor(Person):
    id_faculty = models.ForeignKey('institution.Faculty', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name}"

class Student(Person):
    enrollment_id = models.CharField(max_length=9, primary_key=True)
    id_career = models.ForeignKey('institution.Career', on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=6, choices=LEVELS)
    photo = models.CharField(max_length=100, blank=True, null=True)
    id_member = models.OneToOneField('Member', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"

class Member(AbstractBaseUser, PermissionsMixin):
    description = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now=True)
    permissions = models.CharField(max_length=1, choices=PERMISSIONS, default='N')
    ambassador = models.URLField(max_length=300, blank=True, null=True, unique=True, validators=[ambassador_valid_url])
    social_links = models.JSONField(default=dict, blank=True, null=True)
    active = models.BooleanField(default=True)

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(('email address'), blank=True)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.username}"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class MemberRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1, choices=ROLES, default='M')
    id_member = models.ForeignKey('Member', on_delete=models.CASCADE, blank=True, null=True)
    date_start = models.DateTimeField(auto_now=False)
    date_end = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.id_member} {self.name}"
    