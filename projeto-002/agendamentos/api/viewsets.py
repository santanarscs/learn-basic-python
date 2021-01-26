from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from agendamentos.models import Agendamento
from agendamentos.api.serializers import AgendamentosSerializer, AgendamentosDetalhesSerializer


class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, requets, pk=None, *args, **kwargs):
        queryset = Agendamento.objects.filter(pk=pk)
        self.serializer_class = AgendamentosDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
