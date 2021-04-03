from django.db import models
from django.contrib.auth.models import AbstractUser
from institute.models import Faculty, Career, SubOrganization

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
    (1, 'Presidente'),
    (2, 'Vicepresidente'),
    (3, 'Secretario'),
    (4, 'Tesorero'),
    (5, 'Vocal'),
    (6, 'Miembro'),
    (0, 'Tutor'),
    (10, 'Asesor'),
]

PERMISSIONS = [
    (1, 'Presidente'),
    (2, 'Vicepresidente'),
    (3, 'Sub Organización'),
    (4, 'Miembro'),
]
class Person(AbstractUser):
    card_id = models.CharField(max_length=10, primary_key=True)
    born_date = models.DateField(auto_now=False)
    genre = models.CharField(max_length=1, choices=GENRES)
    signature = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.card_id} {self.get_full_name}"

class Professor(models.Model):
    id_person = models.OneToOneField(Person, on_delete=models.CASCADE)
    id_faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_person.get_full_name}"

class Student(models.Model):
    enrollment_id = models.CharField(max_length=9, primary_key=True)
    id_faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)
    id_career = models.OneToOneField(Career, on_delete=models.CASCADE)
    level = models.CharField(max_length=6, choices=LEVELS)
    photo = models.CharField(max_length=100, blank=True, null=True)
    id_person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matricula} {self.id_person.get_full_name}"
    
class Member(AbstractUser):
    id_estudiante = models.OneToOneField(Student, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now=True)
    role = models.CharField(max_length=25, choices=ROLES, default=ROLES.Miembro)
    permissions = models.CharField(max_length=25, choices=ROLES, default=PERMISSIONS.Miembro)
    id_sub_org = models.ForeignKey(SubOrganization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_estudiante.id_person.get_full_name}"
