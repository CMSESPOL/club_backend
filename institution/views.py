from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .models import *
from .serializers import *
class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticated]

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubOrganizationViewSet(viewsets.ModelViewSet):
    queryset = SubOrganization.objects.all()
    serializer_class = SubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
