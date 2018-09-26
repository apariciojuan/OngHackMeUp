# Generated by Django 2.1.1 on 2018-09-26 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voluntario', '0005_auto_20180926_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Domingo',
            field=models.ManyToManyField(blank=True, related_name='domingo_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Jueves',
            field=models.ManyToManyField(blank=True, related_name='jueves_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Lunes',
            field=models.ManyToManyField(blank=True, related_name='lunes_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Martes',
            field=models.ManyToManyField(blank=True, related_name='martes_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Miercoles',
            field=models.ManyToManyField(blank=True, related_name='miercoles_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Sabado',
            field=models.ManyToManyField(blank=True, related_name='sabado_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='diasdisponibles',
            name='Viernes',
            field=models.ManyToManyField(blank=True, related_name='viernes_set', to='voluntario.horario'),
        ),
        migrations.AlterField(
            model_name='person',
            name='disponibilidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voluntario.DiasDisponibles'),
        ),
    ]
