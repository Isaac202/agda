# Generated by Django 4.1 on 2022-08-15 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.clientes'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.colaborador'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.servico'),
        ),
    ]
