# Generated by Django 4.1 on 2022-09-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0004_horario_disponivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segunda', models.BooleanField(default=True)),
                ('terca', models.BooleanField(default=True)),
                ('quarta', models.BooleanField(default=True)),
                ('quinta', models.BooleanField(default=True)),
                ('sexta', models.BooleanField(default=True)),
                ('sabado', models.BooleanField(default=True)),
                ('domingo', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='horario',
            name='domingo',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='quarta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='quinta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='sabado',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='segunda',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='sexta',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='terca',
        ),
        migrations.AddField(
            model_name='horario',
            name='dia_da_semana',
            field=models.ManyToManyField(to='agendamentos.diasemana'),
        ),
    ]
