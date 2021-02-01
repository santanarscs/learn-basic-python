
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentariosViewSet
from enderecos.api.viewsets import EnderecosViewSet
router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'enderecos', EnderecosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
