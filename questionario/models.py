from django.db import models
from usuario.models import CustomUser

class Classificacao(models.TextChoices):
    SEM_SOFRIMENTO = 'SEM_SOFRIMENTO', 'Sem Sofrimento'
    LEVE = 'LEVE', 'Leve'
    MODERADO = 'MODERADO', 'Moderado'
    GRAVE = 'GRAVE', 'Grave'
    
class Questionario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_resposta = models.DateField()
    pontuacao = models.IntegerField()
    classificacao = models.CharField(
        max_length=20,
        choices=Classificacao.choices,
        default=Classificacao.SEM_SOFRIMENTO
    )

    def __str__(self):
        return f"Questionário de {self.usuario.username} em {self.data_resposta}"
