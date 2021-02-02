from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import PontoTuristico
from atracoes.models import Atracao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
            'nome',
            'descricao',
            'aprovado',
            'atracoes',
            'comentarios',
            'avaliacoes',
            'endereco',
            'foto',
            'descricao_completa',
            'descricao_completa2'
        ]
        read_only_fields = ['comentarios', 'avaliacoes']

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
