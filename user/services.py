
from institution.serializers import OrganizationSerializer
from user.serializers import PersonManagerSerializer, PersonSerializer, ProfessorManagerSerializer, ProfessorSerializer, StudentManagerSerializer, StudentSerializer
from user.models import Member, Person, Professor, ROLES, Student
from rest_framework import exceptions


class PersonService:

    roles = [i[0] for i in ROLES]

    def get_by_id(self, id):
        try:
            person = Person.objects.get(card_id=id)
        except Person.DoesNotExist:
            raise exceptions.ValidationError(
                    detail=f"Person with id {id} don't exist")
        if person.actual_role == 'E':
            return PersonManagerSerializer(person).data
        elif person.actual_role == 'T':
            try:
                professor = Professor.objects.prefetch_related(
                    "id_faculty").get(card_id=id)
            except Professor.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Professor with id {id} don't exist")
            return ProfessorManagerSerializer(professor).data
        elif person.actual_role not in ('A', 'T', 'E'):
            try:
                student = Student.objects.prefetch_related(
                    "id_faculty").prefetch_related("id_career").get(card_id=id)
            except Student.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Student with id {id} don't exist")
            return StudentManagerSerializer(student).data

    def create(self, data: dict):
        role = data.get("role")
        if not role:
            raise exceptions.ValidationError(detail="Role is required")

        if role not in self.roles:
            raise exceptions.ValidationError(detail="Role don't exist")
        if role == 'E':
            data.pop("role")
            serializer = PersonManagerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                person = serializer.save(actual_role=role)
                return PersonManagerSerializer(person).data
        elif role == 'T':
            data.pop("role")
            serializer = ProfessorManagerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                professor = serializer.save(actual_role=role)
                return ProfessorManagerSerializer(professor).data
        elif role not in ('A', 'T', 'E'):
            serializer = StudentManagerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                student = serializer.save(actual_role=role)
                return StudentManagerSerializer(student).data

        raise exceptions.ValidationError(detail="This action is not allowed")

    def update(self, data: dict):
        id = data.get("card_id", None)
        if not id:
            raise exceptions.ValidationError(detail="card id is required")
        try:
            person = Person.objects.get(card_id=id)
        except Person.DoesNotExist:
            raise exceptions.ValidationError(
                detail=f"Person with id {id} don't exist")

        if person.actual_role == 'E':
            serializer = PersonManagerSerializer(person, data=data)
            if serializer.is_valid(raise_exception=True):
                person = serializer.save()
                return PersonSerializer(person).data

        elif person.actual_role == 'T':
            try:
                professor = Professor.objects.get(card_id=id)
            except Professor.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Professor with id {id} don't exist")
            serializer = ProfessorManagerSerializer(professor, data=data)
            if serializer.is_valid(raise_exception=True):
                professor = serializer.save()
                return ProfessorSerializer(professor).data

        elif person.actual_role not in ('A', 'T', 'E'):
            try:
                student = Student.objects.get(card_id=id)
            except Student.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Student with id {id} don't exist")
            serializer = StudentManagerSerializer(student, data=data)
            if serializer.is_valid(raise_exception=True):
                student = serializer.save()
                return StudentSerializer(student).data
        raise exceptions.ValidationError(detail="This action is not allowed")

    def delete(self, id):
        if not id:
            raise exceptions.ValidationError(detail="Id is required")
        
        try:
            person = Person.objects.get(card_id=id)
        except Person.DoesNotExist:
            raise exceptions.ValidationError(
                detail=f"Person with id {id} don't exist")

        if person.actual_role == 'E':
            person.delete()

        elif person.actual_role == 'T':
            try:
                professor = Professor.objects.get(card_id=id)
            except Professor.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Professor with id {id} don't exist")
            professor.delete()

        elif person.actual_role not in ('A', 'T', 'E'):
            try:
                student = Student.objects.get(card_id=id)
            except Student.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Student with id {id} don't exist")
            student.delete()
        return {"status": "ok"}

    def get_organization(self, member: Member):
        serializer = OrganizationSerializer(member.id_sub_org.id_organization)
        return serializer.data
