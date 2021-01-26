from rest_framework import serializers
from historicos.models import Historico
from imagens.api.serializers import ImagensHistoricoSerializer


class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'


class HistoricosDetalhesSerializer(serializers.ModelSerializer):
    imagens = ImagensHistoricoSerializer(many=True, read_only=True)

    class Meta:
        model = Historico
        fields = [
            'id_historico',
            'data',
            'aparecimento_sintomas',
            'duracao_sintomas',
            'local_dor',
            'tipo_dor',
            'conclusao',
            'id_agendamento',
            'imagens'
        ]
