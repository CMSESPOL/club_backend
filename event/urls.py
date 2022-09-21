from django.urls import path, include
from event.views import *
from institution.views import *
from user.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('create',views.DocumentCreate,name="create"),
    path('update/<int:pk>/',views.DocumentUpdate,name="update"),
    path('delete/<int:pk>/',views.DocumentDelete,name="delete"),
    path('documento/<str:pk>/',DocumentCrud.as_view())
]