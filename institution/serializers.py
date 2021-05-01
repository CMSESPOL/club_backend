from rest_framework import serializers
from .models import *

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['acronym', 'name']    

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['name', 'id_faculty']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['abbreviation', 'name', 'description']

class SubOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOrganization
        fields = ['name', 'description', 'id_organization']
