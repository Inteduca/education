# Generated by Django 2.0.6 on 2018-07-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20180712_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaturas',
            name='fisica',
            field=models.CharField(default='f', max_length=10),
        ),
        migrations.AddField(
            model_name='asignaturas',
            name='matematicas',
            field=models.CharField(default='f', max_length=10),
        ),
        migrations.AddField(
            model_name='asignaturas',
            name='quimica',
            field=models.CharField(default='f', max_length=10),
        ),
    ]