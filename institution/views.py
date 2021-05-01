from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class FacultyList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Faculty.objects.all()
        serializer = FacultySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CareerList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Career.objects.all()
        serializer = CareerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        queryset = Organization.objects.all()
        serializer = OrganizationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubOrganizationList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        queryset = SubOrganization.objects.all()
        serializer = SubOrganizationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubOrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
