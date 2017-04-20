from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from django.utils.timezone import *
from datetime import *
from ..models import Treino



@login_required
def treinoexpirado(request):
    treinos = Treino.objects.filter(data_fim__lte=now())
    return render(request, 'dashboard.html', {
        'treinos':treinos
    })
   
    
@login_required
def treinoexpirando(request):
    hoje = date.today()
    futuro = (hoje - datetime.timedelta(days=7))
    texpirando = Treino.objects.filter(data_fim__gte=futuro)
    return render(request, 'dashboard.html', {
        'texpirando':texpirando
    })