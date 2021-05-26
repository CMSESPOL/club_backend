from django.urls import path, include
from event.views import *
from institution.views import *
from user.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', include(router.urls)),
    # path('/', .as_view()),
    path('evento/', EventList.as_view()),
    path('evento/<int:pk>/', EventDetail.as_view()),
    path('eventoOrdenado/<str:order>/', EventDetail.as_view()),
    path('eventoTipo/<str:id_organization>/<str:event_type>/', EventDetail.as_view()),
    path('documento/', DocumentList.as_view()),
    path('facultad/', FacultyList.as_view()),
    path('carrera/', CareerList.as_view()),
    path('organizacion/', OrganizationList.as_view()),
    path('organizacion/<str:pk>/', OrganizationDetail.as_view()),
    path('suborganizacion/', SubOrganizationList.as_view()),
    path('suborganizacion/<int:pk>/', SubOrganizationDetail.as_view()),
    path('suborganizacion/<str:id_organization>/', SubOrganizationDetail.as_view()),
    path('persona/', PersonList.as_view()),
    path('persona/manager/', PersonView.as_view()),
    path('profesor/', ProfessorList.as_view()),
    path('estudiante/', StudentList.as_view()),
    path('miembro/', MemberList.as_view()),
    path('rol/', MemberRoleList.as_view()),
    path('auth/login/', AuthToken.as_view()),
    path('auth/login/web/', AuthCookie.as_view()),
    path('documento/', DocumentList.as_view()),
    path('documento/<str:pk>/', DocumentDetail.as_view()),
    path('documento/<str:doc_type>/', DocumentDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
