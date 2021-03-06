# Generated by Django 2.0.6 on 2018-07-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20180628_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='observaciones_text',
            field=models.CharField(default='¡Vaya! Parece que todavía no tienes ninguna observación.', max_length=100000),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='horario_text',
            field=models.CharField(default='¡Vaya! Parece que todavía no tienes un horario. Contacta con tutor y lo tendrás pronto.', max_length=100000),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='score_text',
            field=models.CharField(default='¡Vaya! Parece que todavía no tienes un seguimiento. Contacta con tutor y lo tendrás pronto.', max_length=100000),
        ),
    ]
