from event.views import *
from rest_framework.routers import DefaultRouter
from institution.views import *
from user.views import *
from django.urls import path, include
router = DefaultRouter()

router.register(r'facultad',FacultyViewset)
router.register(r'carrera',CareerViewset)
router.register(r'organizacion',OrganizationViewset)
router.register(r'suborganizacion',SubOrganizationViewset)
router.register(r'eventos',EventViewSet, basename='EventosDetalles')
router.register(r'documentos',DocumentViewSet, basename='DocumentosDetalles')
router.register(r'persona',PersonViewset)
router.register(r'estudiante',StudentViewset)
router.register(r'profesor',ProfessorViewset)
router.register(r'miembros', MemberViewset)
router.register(r'rol', MemberRolViewset)
urlpatterns = router.urls
