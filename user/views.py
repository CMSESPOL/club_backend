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
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes


auth_service = AuthService()
person_service = PersonService()



class PersonViewset(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonManagerSerializer
    queryset = Person.objects.all()

class ProfessorViewset(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfessorManagerSerializer
    queryset = Professor.objects.all()

class StudentViewset(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentManagerSerializer
    queryset = Student.objects.all()

class MemberViewset(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class MemberRolViewset(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = MemberRoleSerializer
    queryset = MemberRole.objects.all()


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

