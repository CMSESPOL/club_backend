
from user.serializers import PersonManagerSerializer, PersonSerializer, ProfessorManagerSerializer, ProfessorSerializer, StudentManagerSerializer, StudentSerializer
from user.models import Person, Professor, ROLES, Student
from rest_framework import exceptions


class PersonService:

    roles = [i[0] for i in ROLES]

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
                person = serializer.save()
                return PersonSerializer(person).data
        elif role == 'T':
            data.pop("role")
            serializer = ProfessorManagerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                professor = serializer.save()
                return ProfessorSerializer(professor).data
        elif role not in ('A', 'T', 'E'):
            serializer = StudentManagerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                student = serializer.save()
                return StudentSerializer(student).data

        raise exceptions.ValidationError(detail="This action is not allowed")
    
    def update(self, data: dict):
        id = data.pop("id")
        if not id:
            raise exceptions.ValidationError(detail="Id is required")
        role = data.get("role")
        if not role:
            raise exceptions.ValidationError(detail="Role is required")
        if role not in self.roles:
            raise exceptions.ValidationError(detail="Role don't exist")

        if role == 'E':
            data.pop("role")
            try:
                person = Person.objects.get(card_id=id)
            except Person.DoesNotExist:
                raise exceptions.ValidationError(detail=f"Person with id {id} don't exist")
            serializer = PersonManagerSerializer(person, data=data)
            if serializer.is_valid(raise_exception=True):
                person = serializer.save()
                return PersonSerializer(person).data

        elif role == 'T':
            data.pop("role")
            try:
                professor = Professor.objects.get(pk=id)
            except Professor.DoesNotExist:
                raise exceptions.ValidationError(detail=f"Professor with id {id} don't exist")
            serializer = ProfessorManagerSerializer(professor, data=data)
            if serializer.is_valid(raise_exception=True):
                professor = serializer.save()
                return ProfessorSerializer(professor).data

        elif role not in ('A', 'T', 'E'):
            try:
                student = Student.objects.get(pk=id)
            except Student.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Student with id {id} don't exist")
            serializer = StudentManagerSerializer(student, data=data)
            if serializer.is_valid(raise_exception=True):
                student = serializer.save()
                return StudentSerializer(student).data
        raise exceptions.ValidationError(detail="This action is not allowed")

    def delete(self, data:dict):
        id = data.pop("id")
        if not id:
            raise exceptions.ValidationError(detail="Id is required")
        role = data.get("role")
        if not role:
            raise exceptions.ValidationError(detail="Role is required")
        if role not in self.roles:
            raise exceptions.ValidationError(detail="Role don't exist")

        if role == 'E':
            try:
                person = Person.objects.get(card_id=id)
            except Person.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Person with id {id} don't exist")
            person.delete()
           
        elif role == 'T':
            try:
                professor = Professor.objects.get(pk=id)
            except Professor.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Professor with id {id} don't exist")
            professor.delete()

        elif role not in ('A', 'T', 'E'):
            try:
                student = Student.objects.get(pk=id)
            except Student.DoesNotExist:
                raise exceptions.ValidationError(
                    detail=f"Student with id {id} don't exist")
            student.delete()
        return {"status": "ok"}   
        