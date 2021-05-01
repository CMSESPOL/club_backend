from user.validators import ambassador_valid_url
from django.db import models
from django.contrib.auth.models import AbstractUser

GENRES = [
    ('M', 'Masculino'),
    ('F', 'Femenino')
]

LEVELS = [
    ('100', '100-I'),
    ('100', '100-II'),
    ('200', '200-I'),
    ('200', '200-II'),
    ('300', '300-I'),
    ('300', '300-II'),
    ('400', '400-I'),
    ('400', '400-II'),
    ('500', '500-I'),
    ('500', '500-II'),
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
    born_date = models.DateField(auto_now=False)
    genre = models.CharField(max_length=1, choices=GENRES)
    signature = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.card_id}"

class Professor(models.Model):
    id_person = models.OneToOneField('Person', on_delete=models.CASCADE)
    id_faculty = models.OneToOneField('institution.Faculty', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id_person}"

class Student(models.Model):
    enrollment_id = models.CharField(max_length=9, primary_key=True)
    id_faculty = models.OneToOneField('institution.Faculty', on_delete=models.CASCADE, null=True)
    id_career = models.OneToOneField('institution.Career', on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=6, choices=LEVELS)
    photo = models.CharField(max_length=100, blank=True, null=True)
    id_person = models.OneToOneField('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.enrollment_id}"
    
class Member(AbstractUser):
    id_student = models.OneToOneField('Student', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now=True)
    actual_role = models.OneToOneField('MemberRole', on_delete=models.CASCADE, blank=True, null=True)
    permissions = models.CharField(max_length=1, choices=PERMISSIONS, default='N')
    ambassador = models.URLField(max_length=300, blank=True, null=True, unique=True, validators=[ambassador_valid_url])
    social_links = models.JSONField(default=dict, blank=True, null=True)
    active = models.BooleanField(default=True)
    id_sub_org = models.ForeignKey('institution.SubOrganization', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.username}"

class MemberRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1, choices=ROLES, default='M')
    id_member = models.ForeignKey('Member', on_delete=models.CASCADE, blank=True, null=True)
    date_start = models.DateTimeField(auto_now=False)
    date_end = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.id_member} {self.name}"
    
    def save(self, *args, **kwargs):
        try:
            member = Member.objects.get(id=self.id_member.id)
            if member:
                member.actual_role = self
                super().save(*args, **kwargs)
                member.save()
            else: 
                raise Exception("Error al tratar de asignar el rol actual.")
        except Exception as e:
            return f"{e}"
