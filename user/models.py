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
    ('A', 'Presidente'),
    ('B', 'Vicepresidente'),
    ('C', 'Secretario'),
    ('D', 'Tesorero'),
    ('E', 'Vocal'),
    ('F', 'Miembro'),
    ('N', 'Ninguno'),
    ('X', 'Asesor'),
    ('Y', 'Tutor'),
    ('Z', 'Externo')
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
        return f"{self.card_id} {self.get_full_name}"

class Professor(models.Model):
    id_person = models.OneToOneField('Person', on_delete=models.CASCADE)
    id_faculty = models.OneToOneField('institution.Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_person.get_full_name}"

class Student(models.Model):
    enrollment_id = models.CharField(max_length=9, primary_key=True)
    id_faculty = models.OneToOneField('institute.Faculty', on_delete=models.CASCADE)
    id_career = models.OneToOneField('institute.Career', on_delete=models.CASCADE)
    level = models.CharField(max_length=6, choices=LEVELS)
    photo = models.CharField(max_length=100, blank=True, null=True)
    id_person = models.OneToOneField('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matricula} {self.id_person.get_full_name}"
    
class Member(AbstractUser):
    id_student = models.OneToOneField('Student', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now=True)
    role = models.CharField(max_length=2, choices=ROLES, default='F')
    permissions = models.CharField(max_length=2, choices=PERMISSIONS, default='N')
    id_sub_org = models.ForeignKey('institution.SubOrganization', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        if self.id_student:
            return f"{self.id_student.id_person.get_full_name}"
        return f"{self.username}"
