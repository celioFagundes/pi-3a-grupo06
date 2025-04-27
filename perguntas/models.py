from django.db import models

class Pergunta(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()

    def __str__(self):
        return self.texto