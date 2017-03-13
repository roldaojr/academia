from django import forms
from django.forms.models import modelform_factory
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Usuario, Treino, AvaliacaoFisica, RespostaAnamnese

AdicionarPessoaForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo', 'login', 'password'
))

EditarPessoaForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo'
))

class TreinoForm(forms.ModelForm):
     class Meta:
         model = Treino
         exclude = ('pessoa',)
         widgets = {
             'data_inicio': DateTimePicker(
                 options={"format": "DD/MM/YYYY", 'locale': 'pt-br'}),
             'data_fim': DateTimePicker(
                 options={"format": "DD/MM/YYYY", 'locale': 'pt-br'})
         }

AvaliacaoForm = modelform_factory(AvaliacaoFisica, exclude=('pessoa',))
