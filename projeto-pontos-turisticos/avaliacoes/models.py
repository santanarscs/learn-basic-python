from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.name
