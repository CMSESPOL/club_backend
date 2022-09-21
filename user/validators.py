from rest_framework import exceptions
from django.core.exceptions import ValidationError
import re

ambassador_regex = r'.*studentambassadors.*'

def ambassador_valid_url(value):
    regex = re.compile(ambassador_regex)
    if not regex.match(value):
        raise ValidationError("Url don't match with studentambassadors")


def username_valid(value: str):
    if not value or len(value) == 0:
        raise exceptions.AuthenticationFailed(detail="Usuario es requerido.")

def password_valid(value: str):
    if not value or len(value) == 0:
        raise exceptions.AuthenticationFailed(detail="Contraseña es requerida.")


