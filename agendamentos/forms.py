from dataclasses import field
from django.forms import ModelForm
from agendamentos.models.horarios import Horario


class HorarioForm(ModelForm):
    class Meta:
        model= Horario
        exclude = ['criado_em',"atualizado_em"]