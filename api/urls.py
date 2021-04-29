from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from institution.views import *
from user.views import *

router = routers.DefaultRouter()
router.register(r'facultades', FacultyViewSet)
router.register(r'carreras', CareerViewSet)
router.register(r'organizacion', OrganizationViewSet)
router.register(r'suborganizacion', SubOrganizationViewSet)
router.register(r'persona', PersonViewSet)
router.register(r'profesor', ProfessorViewSet)
router.register(r'estudiante', StudentViewSet)
router.register(r'miembro', MemberViewSet)
router.register(r'rol de miembro', MemberRoleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
