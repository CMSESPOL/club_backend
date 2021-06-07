from rest_framework.authentication import SessionAuthentication
from user.services import PersonService
from user.auth.services import AuthService
from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth import login
from user.auth.BearerAuthentication import BearerAuthentication
from rest_framework import exceptions

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes


auth_service = AuthService()
person_service = PersonService()

class PersonList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberRoleList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = MemberRole.objects.all()
        serializer = MemberRoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthToken(APIView):

    def post(self, request):
        user = auth_service.get_user_by_credentials(request.data)
        return Response(data=auth_service.generate_auth_token(user)) 

class AuthCookie(APIView):

    def post(self, request):
        user = auth_service.get_user_by_credentials(request.data)
        data = auth_service.generate_auth_token(user) 
        login(request, user)
        return Response(data=data["user"])

class PersonView(APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        return Response(data=person_service.get_by_id(pk))

    def post(self, request):
        return Response(data=person_service.create(request.data))
    
    def put(self, request):
        return Response(data=person_service.update(request.data))
    
    def delete(self, request, pk):
        return Response(data=person_service.delete(pk))

@api_view(["POST"])
@authentication_classes([BearerAuthentication, SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_member_organization(request):
    member = request.user
    return Response(data=person_service.get_organization(member))
