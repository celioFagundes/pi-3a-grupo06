from django.db import models
from questionario.models import Questionario
from perguntas.models import Pergunta

class Resposta(models.Model):
    id = models.AutoField(primary_key=True)
    questionario = models.ForeignKey(Questionario, related_name='respostas', on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.BooleanField()

    def __str__(self):
        return f"Resposta da Pergunta '{self.pergunta.texto}' - Questionário {self.questionario.id}"
