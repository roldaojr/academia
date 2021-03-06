from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from django.utils.timezone import *
from datetime import *
from ..models import Usuario, Treino, AvaliacaoFisica

@login_required
def treinoexpirado(request):
    # redirecionar caso seja aluno
    if request.user.tipo == 1:
        return redirect('aluno_detalhar', pk=request.user.pk)

    #treino expirado
    treinos = Treino.objects.filter(data_fim__lte=now(), ativo=True)

    #treino expirando
    hoje = date.today()
    amanha = (date.today() + timedelta(days=1))
    futuro = (hoje + timedelta(days=7))
    texpirando = Treino.objects.filter(data_fim__gte=amanha, data_fim__lte=futuro)

    #avaliação física expirada
    avaliacoes = AvaliacaoFisica.objects.filter(data_refazer__lte=now())

    #avaliação física expirando
    avaliacaoexpirando = AvaliacaoFisica.objects.filter(data_refazer__gte=amanha, data_refazer__lte=futuro)

    return render(request, 'dashboard.html', {
        'treinos':treinos, 'texpirando':texpirando, 'avaliacoes':avaliacoes, 'avaliacaoexpirando':avaliacaoexpirando
    })
