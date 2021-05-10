from institution.models import Career, Faculty, SubOrganization
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
        fields = ['first_name', 'last_name', 'student', 'description',
                  'date_joined', 'actual_role', 'permissions', 'active', 'id_sub_org']


class MemberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRole
        fields = ['id', 'name', 'id_member', 'date_start', 'date_end']


class PersonManagerSerializer(serializers.ModelSerializer):

    signature = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Person
        fields = ['card_id', 'born_date', 'genre', 'signature']

    def create(self, validated_data):
        person = Person(**validated_data)
        try:
            person.save()
        except:
            raise exceptions.APIException()
        return person

    def update(self, instance, validated_data):
        instance.card_id = validated_data.get("card_id", instance.card_id)
        instance.born_date = validated_data.get(
            "born_date", instance.born_date)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.signature = validated_data.get(
            "signature", instance.signature)
        instance.save()
        return instance


class ProfessorManagerSerializer():

    id_faculty = serializers.CharField(
        max_length=6, source="id_faculty.acronym")

    class Meta:
        model = Professor
        fields = [
            'id_person',
            'id_faculty'
        ]

    def create(self, validated_data):
        person = PersonManagerSerializer(data=validated_data.get("id_person"))
        if person.is_valid(raise_exception=True):
            person = person.save()
        validated_data["id_faculty"] = Faculty(
            acronym=validated_data.get("id_faculty"))
        validated_data["id_person"] = person
        professor = Professor(**validated_data)
        try:
            professor.save()
        except:
            person.delete()
            raise exceptions.APIException()
        return professor

    def update(self, instance, validated_data):
        id_person = instance.id_person
        person = PersonManagerSerializer(
            instance=id_person, data=validated_data.get("id_person"))
        if person.is_valid(raise_exception=True):
            person.save()
        faculty = validated_data.get("id_faculty")
        if faculty:
            instance.id_faculty = Faculty(acronym=faculty)
        instance.save()
        return instance


class StudentManagerSerializer(serializers.ModelSerializer):

    id_faculty = serializers.CharField(
        max_length=6, source="id_faculty.acronym")
    id_career = serializers.CharField(max_length=38, source="id_career.name")
    id_person = PersonManagerSerializer()

    class Meta:
        model = Student
        fields = [
            'enrollment_id',
            'id_faculty',
            'id_career',
            'level',
            'photo',
            'id_person'
        ]

    def create(self, validated_data):
        person = PersonManagerSerializer(data=validated_data.get("id_person"))
        if person.is_valid(raise_exception=True):
            person = person.save()
        validated_data["id_person"] = person
        validated_data["id_faculty"] = Faculty(
            acronym=validated_data.get("id_faculty"))
        validated_data["id_career"] = Career(
            name=validated_data.get("id_career"))
        student = Student(**validated_data)
        try:
            student.save()
        except:
            person.delete()
            raise exceptions.APIException()
        return student

    def update(self, instance, validated_data):
        id_person = instance.id_person
        person = PersonManagerSerializer(
            instance=id_person, data=validated_data.get("id_person"))
        if person.is_valid(raise_exception=True):
            person.save()
        instance.enrollment_id = validated_data.get(
            "enrollment_id", instance.enrollment_id)
        faculty = validated_data.get("id_faculty")
        if faculty:
            instance.id_faculty = Faculty(acronym=faculty)
        career = validated_data.get("id_career")
        if career:
            instance.id_career = Career(name=career)
        instance.level = validated_data.get("level", instance.level)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance


class MemberManagerSerializer(serializers.ModelSerializer):

    id_student = StudentManagerSerializer()
    ambassador = serializers.URLField(
        requred=False, validators=[ambassador_valid_url])
    social_links = serializers.JSONField(required=False)
    id_sub_org = serializers.IntegerField(
        source="id_sub_org.sub_org_id", write_only=True)
    role = serializers.ChoiceField(
        choices=ROLES, write_only=True, required=False)

    class Meta:
        model = Member
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'description',
            'id_student',
            'ambassador',
            'social_links',
            'id_sub_org'
        ]

    def create(self, validated_data):
        role = validated_data.pop("role")
        student = StudentManagerSerializer(
            data=validated_data.get("id_student"))
        if student.is_valid(raise_exception=True):
            student = student.save()

        id_sub_org = validated_data.get("id_sub_org")
        if id_sub_org:
            id_sub_org = SubOrganization(sub_org_id=id_sub_org)
            validated_data["id_sub_org"] = id_sub_org

        validated_data["id_student"] = student
        member = Member(**validated_data)
        try:
            member.save()
        except:
            student.delete()
            raise exceptions.APIException()
        if role:
            memberRole = MemberRole(name=role, id_member=member)
            try:
                memberRole.save()
                member.actual_role = memberRole
                member.save()
            except:
                raise exceptions.APIException(
                    detail="No se pudo crear el rol del miembro")
        return member

    def update(self, instance, validated_data):
        student = StudentManagerSerializer(instance=instance.id_student,
                                           data=validated_data.get("id_student"))
        if student.is_valid(raise_exception=True):
            student.save()

        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.ambassador = validated_data.get(
            "ambassador", instance.ambassador)
        instance.social_links = validated_data.get(
            "social_links", instance.social_links)
        instance.save()
        role = validated_data.get("role")
        if role:
            memberRole = MemberRole(name=role, id_member=instance)
            try:
                memberRole.save()
                instance.actual_role = memberRole
                instance.save()
            except:
                raise exceptions.APIException(
                    detail="No se pudo actualizar el rol del miembro")
        return instance
