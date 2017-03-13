from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Treino, Usuario
from ..forms import TreinoForm


@login_required
def adicionar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = TreinoForm(request.POST, initial={'pessoa': pessoa})
        if form.is_valid():
            treino = form.save(commit=False)
            treino.pessoa_id = pk
            treino.save()
            return redirect(reverse('serie_listar',
                                    kwargs={'pk': treino.pk}))
    else:
        form = TreinoForm(initial={'pessoa': pessoa})
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar treino'})


@login_required
def editar(request, pk):
    treino = Treino.objects.get(pk=pk)
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect(reverse('aluno_detalhar',
                                    kwargs={'pk': treino.pessoa_id}))
    else:
        form = TreinoForm(instance=treino)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar treino', 'tipo': 'treino',
        'delete_url': reverse('treino_apagar', kwargs={'pk': pk})
    })


@login_required
def apagar(request, pk):
    treino = Treino.objects.get(pk=pk)
    if request.method == 'POST':
        treino.delete()
    return redirect(reverse('aluno_detalhar', kwargs={'pk': treino.pessoa.pk}))
