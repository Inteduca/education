from django.db import models


class DataSheet(models.Model):
    username=models.CharField(max_length=15);
    integrales=models.IntegerField(default=0);
    derivadas=models.IntegerField(default=0);
    matrices=models.IntegerField(default=0);




