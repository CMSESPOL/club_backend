from institution.models import Career, Faculty, SubOrganization
from institution.serializers import CareerSerializer, FacultySerializer
from rest_framework import exceptions, serializers
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
        fields = ['enrollment_id', 'id_faculty',
                  'id_career', 'level', 'person']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
        'username', 
        'password', 
        'description', 
        'ambassador', 
        'social_links',
        'email',
        'id_student'
        ]

    def create(self, validated_data):
        passw = validated_data.get('password')
        member = Member(**validated_data)
        member.set_password(passw)
        try:
            member.save()
        except Exception as e:
            raise exceptions.APIException
        return member
    
    def update(self, instance, validated_data):
        oldp = instance.password
        update_user = super().update(instance,validated_data)
        if not (oldp == validated_data['password']):
            update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class MemberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRole
        fields = ['id', 'name', 'id_member', 'date_start', 'date_end']


class PersonManagerSerializer(serializers.ModelSerializer):

    signature = serializers.CharField(required=False, max_length=100)
    
    class Meta:
        model = Person
        fields = [
            'card_id',
            'first_name',
            'last_name',
            'born_date',
            'genre',
            'signature'
        ]

    def create(self, validated_data):
        person = Person(**validated_data)
        try:
            person.save()
        except Exception as e:
            raise exceptions.APIException()
        return person

    def update(self, instance, validated_data):
        person = super().update(instance,validated_data)
        person.save()
        return person


class ProfessorManagerSerializer(serializers.ModelSerializer):
    
    id_faculty = serializers.CharField(max_length=6, source="id_faculty.acronym")

    class Meta:
        model = Professor
        fields = [
            'card_id',
            'first_name',
            'last_name',
            'born_date',
            'genre',
            'signature',
            'id_faculty'
        ]

    def create(self, validated_data):
        faculty = Faculty(acronym=validated_data.get(
            "id_faculty", {}).get("acronym"))
        validated_data["id_faculty"] = faculty
        professor = Professor(**validated_data)
        try:
            professor.save()
        except:
            raise exceptions.APIException()
        return professor

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.born_date = validated_data.get('born_date', instance.born_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.signature = validated_data.get('signature', instance.signature)
        faculty = validated_data.get("id_faculty", {}).get('acronym')
        if faculty:
            instance.id_faculty = Faculty(acronym=faculty)
        instance.save()
        return instance


class StudentManagerSerializer(serializers.ModelSerializer):
    
    id_career = serializers.CharField(max_length=38, source="id_career.name")

    class Meta:
        model = Student
        fields = [
            'card_id',
            'first_name',
            'last_name',
            'born_date',
            'genre',
            'signature',
            'enrollment_id',
            'id_career',
            'level',
            'photo'
        ]

    def create(self, validated_data):
        career = Career(name=validated_data.get("id_career", {}).get("name"))
        validated_data["id_career"] = career
        student = Student(**validated_data)
        try:
            student.save()
        except:
            raise exceptions.APIException()
        return student

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.born_date = validated_data.get('born_date', instance.born_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.signature = validated_data.get('signature', instance.signature)
        career = validated_data.get("id_career", {}).get("name")
        if career:
            instance.id_career = Career(name=career)
        instance.level = validated_data.get("level", instance.level)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance

