from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from event.serializers import *


"""Para poder acceder al orden de los elementos se escribe ?ord=dsc o ?ord=asc al final de la consulta
ejemplo:    http://127.0.0.1:8000/api/eventos/?ord=dsc
En caso de mas variables se usa el operador &
ejemplo:    http://127.0.0.1:8000/api/eventos/?ordering=dsc&search=A0"""


class EventViewSet(viewsets.ModelViewSet):
    serializer_class=EventSerializer
    queryset=Event.objects.all()
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    ordering_fields=['date_start']
    search_fields = ['event_type']


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class=DocumentSerializer
    queryset=Document.objects.all()
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    ordering_fields=['name']
    search_fields=['doc_type']

