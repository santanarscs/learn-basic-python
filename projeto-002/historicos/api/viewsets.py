from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from historicos.models import Historico
from historicos.api.serializers import HistoricosSerializer, HistoricosDetalhesSerializer


class HistoricosViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all().order_by('data')
    serializer_class = HistoricosSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Historico.objects.filter(pk=pk)
        self.serializer_class = HistoricosDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
