from django.db import models

class Comentarios(models.Model):
    score_text = models.CharField(max_length=100000)
    horario_text = models.CharField(max_length=100000)
    username = models.CharField(max_length=100000)