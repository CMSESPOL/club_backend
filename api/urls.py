from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from institution.views import *

router = routers.DefaultRouter()
router.register(r'facultades', FacultyViewSet)
router.register(r'carreras', CareerViewSet)
router.register(r'organizacion', OrganizationViewSet)
router.register(r'suborganizacion', SubOrganizationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
