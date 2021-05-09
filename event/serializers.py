from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'event_type', 'date_start', 'date_end', 'observations', 'link', 'participants', 'gallery', 'id_organizer', 'id_suborg_in_charge']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['document_id', 'name', 'description', 'doc_type', 'id_writer', 'id_event', 'link']
