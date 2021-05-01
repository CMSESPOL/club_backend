from django.urls import path, include
from institution.views import *
from user.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', include(router.urls)),
    # path('/', .as_view()),
    path('facultad/', FacultyList.as_view()),
    path('carrera/', CareerList.as_view()),
    path('organizacion/', OrganizationList.as_view()),
    path('suborganizacion/', SubOrganizationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
