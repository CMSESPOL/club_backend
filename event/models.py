from django.db import models

EVENT_TYPES = [
    ('A0', 'Asamblea'),
    ('A1', 'Admisión de Aspirantes'),
    ('C0', 'Cumpleaños'),
    ('C1', 'Charla'),
    ('C2', 'Conferencia'),
    ('C3', 'Convenio'),
    ('N0', 'Novatada'),
    ('P0', 'Proyecto'),
    ('R0', 'Reunión'),   
]

DOC_TYPES = [
    ('C1', 'Carta'),
    ('C2', 'Constitución'),
    ('C3', 'Convenio'),
    ('E0', 'Evidenia de reunión'),
    ('P0', 'Propuesta de proyecto'),
    ('S0', 'Solicitud'),
]

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=38)
    description = models.CharField(max_length=100)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPES)
    date_start = models.DateTimeField(auto_now=False)
    date_end = models.DateTimeField(auto_now=False)
    observations = models.CharField(max_length=100, null=True)
    link = models.URLField(blank=True, null=True, default='NO LINK')
    participants = models.JSONField(default=dict)
    gallery = models.JSONField(default=dict, blank=True, null=True)
    id_organizer = models.ForeignKey('user.Member', on_delete=models.CASCADE) 
    id_suborg_in_charge = models.ForeignKey('institution.SubOrganization', on_delete=models.CASCADE) 
    id_professor = models.ForeignKey('user.Professor', on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.name

class Document(models.Model):
    document_id = models.CharField(max_length=10, primary_key=True) 
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    doc_type = models.CharField(max_length=2, choices=DOC_TYPES)
    id_writer = models.OneToOneField('user.Member', on_delete=models.CASCADE)
    id_event = models.OneToOneField('Event', on_delete=models.CASCADE, blank=True, null=True) 
    link = models.URLField(blank=True, null=True, default='NO LINK')
    
    def __str__(self):
        return self.name
