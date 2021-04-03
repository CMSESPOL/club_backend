from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'NAME', VIEWSET_NAME)

urlpatterns = [
    path('', include(router.urls)),
]
