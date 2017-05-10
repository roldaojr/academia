from django import forms
from django.forms.models import modelform_factory
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Usuario, Treino, AvaliacaoFisica, RespostaAnamnese


AdicionarUsuarioForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo', 'tipo', 'login', 'password'
))

EditarUsuarioForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo', 'tipo', 'login'
))

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

class AdicionarTreinoForm(TreinoForm):
    modelo = forms.ModelChoiceField(queryset=Treino.objects.filter(
        pessoa=None, ativo=True), required=False)


class ModeloTreinoForm(forms.ModelForm):
     class Meta:
         model = Treino
         exclude = ('pessoa', 'data_inicio', 'data_fim')


AvaliacaoForm = modelform_factory(AvaliacaoFisica, exclude=('pessoa',))
