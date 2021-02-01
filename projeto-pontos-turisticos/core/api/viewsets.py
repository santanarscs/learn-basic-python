from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.object.all()
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=nome)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response({'Ok': 123})

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # necessita mandar PK por causa do detail True
    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def importar(self, request):
        pass
