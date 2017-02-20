from django.forms.models import modelform_factory
from .models import Usuario, Treino, AvaliacaoFisica, RespostaAnamnese

AdicionarPessoaForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo', 'login', 'password'
))

EditarPessoaForm = modelform_factory(Usuario, fields=(
    'nome', 'idade', 'sexo'
))

TreinoForm = modelform_factory(Treino, exclude=('pessoa',))

AvaliacaoForm = modelform_factory(AvaliacaoFisica, exclude=('pessoa',))
