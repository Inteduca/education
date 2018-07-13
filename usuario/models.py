from django.db import models

class Comentarios(models.Model):
    score_text = models.CharField(max_length=100000, default="¡Vaya! Parece que todavía no tienes un seguimiento. Contacta con tutor y lo tendrás pronto.")
    horario_text = models.CharField(max_length=100000, default="¡Vaya! Parece que todavía no tienes un horario. Contacta con tutor y lo tendrás pronto.")
    observaciones_text=models.CharField(max_length=100000, default="¡Vaya! Parece que todavía no tienes ninguna observación.")
    username = models.CharField(max_length=30)

class Asignaturas(models.Model):
    username = models.CharField(max_length=30)
    matematicas = models.CharField(max_length=10, default="f")
    fisica = models.CharField(max_length=10, default="f")
    quimica = models.CharField(max_length=10, default="f")
