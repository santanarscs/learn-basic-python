from rest_framework import serializers
from pacientes.models import Paciente
from agendamentos.api.serializers import AgendamentosDetalhesSerializer


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = [
            'id_paciente',
            'nome',
            'data_nasc',
            'endereco',
            'num_endereco',
            'bairro_endereco',
            'cep',
            'data_cadastro',
            'rg',
            'agendamentos'
        ]
