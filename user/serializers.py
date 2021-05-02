from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['card_id', 'born_date', 'genre']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id_person', 'person']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['enrollment_id', 'id_faculty', 'id_career', 'level', 'person']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'student', 'description', 'date_joined', 'actual_role', 'permissions', 'active', 'id_sub_org']


class MemberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRole
        fields = ['id', 'name', 'id_member', 'date_start', 'date_end']
