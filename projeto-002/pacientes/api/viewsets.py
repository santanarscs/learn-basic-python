from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from pacientes.models import Paciente
from pacientes.api.serializers import PacientesSerializer, PacientesDetalhesSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Paciente.objects.filter(pk=pk)
        self.serializer_class = PacientesDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
