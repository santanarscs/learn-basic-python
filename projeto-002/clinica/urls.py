from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from pacientes.api.viewsets import PacientesViewSet
from agendamentos.api.viewsets import AgendamentosViewSet
from historicos.api.viewsets import HistoricosViewSet
from imagens.api.viewsets import ImagensHistoricoViewSet

router = DefaultRouter()
router.register(r'pacientes', PacientesViewSet, basename='Pacientes')
router.register(r'agendamentos', AgendamentosViewSet, basename='Agendamentos')
router.register(r'historicos', HistoricosViewSet, basename='Historicos')
router.register(r'imagens_historicos', ImagensHistoricoViewSet,
                basename='Imagens_Historicos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
