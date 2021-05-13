from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class EventList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventOrderedList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_order_objects(self, order):
        try:
            if(order=='dsc'):
                return Event.objects.order_by('-date_start')
            else:
                return Event.objects.order_by('date_start')
 
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, order, format=None):
        events = self.get_order_objects(order)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventByTypeList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_Bytype_objects(self, event_type):
        try:
            return Event.objects.filter(event_type=event_type)
 
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, event_type, format=None):
        events = self.get_Bytype_objects(event_type)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Document.objects.all()
        serializer = DocumentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DocumentCrud(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def DocumentViewList(self,request,pk):
        docs = Document.objects.get(id=pk)
        serializer= DocumentSerializer(docs,many=False)
        return Response(serializer.data)

    def DocumentDetail(self,request,pk):
        doc=Document.objects.get(id=pk)
        serializer=DocumentSerializer(doc,many=False)
        return Response(serializer.data)
        
    def DocumentCreate(self,request):
        serializer=DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def DocumentUpdate(self,request,pk):
        doc=Document.objects.get(id=pk)
        serializer=DocumentSerializer(instance=doc,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def DocumentDelete(self,request,pk):
        doc=Document.objects.get(id=pk)
        doc.delete()
        return Response("Eliminado")