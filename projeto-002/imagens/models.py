from django.db import models
from historicos.models import Historico
# Create your models here.


def imagens_historico(instance, filename):
    return '/'.join(['historico', str(instance.id_historico.id_historico), filename])


class ImagemHistorico(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)
    imagem = models.ImageField(
        blank=True, null=True, upload_to=imagens_historico)
    id_historico = models.ForeignKey(
        Historico, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)
