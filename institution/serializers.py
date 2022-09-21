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
        fields = '__all__'

class SubOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOrganization
        fields = '__all__'


class AllMembersByOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubOrganization
        fields=['sub_org_id','name','members']