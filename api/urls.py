from django.urls import path, include
from event.views import *
from institution.views import *
from user.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', include('api.routers')),
    path('organizacion/<str:pk>/miembros', AllMembersByOrgViewSet.as_view({'get': 'retrive'})),
    path('auth/login/', AuthToken.as_view()),
    path('auth/login/web/', AuthCookie.as_view()),
]

 