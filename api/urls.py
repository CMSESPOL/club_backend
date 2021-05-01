from django.urls import path, include
from event.views import *
from institution.views import *
from user.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', include(router.urls)),
    # path('/', .as_view()),
    path('evento/', EventList.as_view()),
    path('documento/', DocumentList.as_view()),
    path('facultad/', FacultyList.as_view()),
    path('carrera/', CareerList.as_view()),
    path('organizacion/', OrganizationList.as_view()),
    path('suborganizacion/', SubOrganizationList.as_view()),
    path('persona/', PersonList.as_view()),
    path('profesor/', ProfessorList.as_view()),
    path('estudiante/', StudentList.as_view()),
    path('miembro/', MemberList.as_view()),
    path('rol/', MemberRoleList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
