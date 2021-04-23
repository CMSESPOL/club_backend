from django.core.exceptions import ValidationError
import re

ambassador_regex = r'.*studentambassadors.*'

def ambassador_valid_url(value):
    regex = re.compile(ambassador_regex)
    if not regex.match(value):
        raise ValidationError("Url don't match with studentambassadors")

