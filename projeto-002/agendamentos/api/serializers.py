from rest_framework import serializers
from agendamentos.models import Agendamento
from historicos.api.serializers import HistoricosDetalhesSerializer


class AgendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class AgendamentosDetalhesSerializer(serializers.ModelSerializer):
    historicos = HistoricosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Agendamento
        fields = [
            'id_agendamento',
            'data_hora',
            'data_criacao',
            'cancelado',
            'obs',
            'tipo',
            'historicos'
        ]
