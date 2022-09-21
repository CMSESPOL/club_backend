from django.shortcuts import render

from event.models import Document
from .models import *
from .serializers import *

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from django.http import Http404
from django.core.exceptions import FieldError
from collections import OrderedDict
from django_filters.rest_framework import DjangoFilterBackend



class FacultyViewset(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
    pagination_class = None


class CareerViewset(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()

class OrganizationViewset(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        params = self.request.query_params
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        only = params.get('only')
        if only is not None:
            try:
                return Response(queryset.values(only))
            except FieldError:
                return Response({"request": "field not found"})
        else:
            return Response(serializer.data)


class AllMembersByOrgViewSet(viewsets.ModelViewSet):
    serializer_class = AllMembersByOrgSerializer
    def retrive(self, request, pk=None):
        queryset=SubOrganization.objects.filter(id_organization=pk).values('sub_org_id','name','members')
        return Response(queryset)


class SubOrganizationViewset(viewsets.ModelViewSet):
    serializer_class = SubOrganizationSerializer
    queryset = SubOrganization.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields = ['id_organization__abbreviation']

