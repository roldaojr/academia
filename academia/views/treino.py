from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Treino, Usuario
from ..forms import TreinoForm, ModeloTreinoForm, AdicionarTreinoForm
from ..utils import copiar_treino_series


@login_required
def listar(request):
    treinos = Treino.objects.filter(pessoa=None)
    return render(request, 'treino/listar.html', {'treinos': treinos})


@login_required
def adicionar(request, pk=None):
    pessoa = Usuario.objects.get(pk=pk) if pk else None
    if pessoa:
        form_class = AdicionarTreinoForm
    else:
        form_class = ModeloTreinoForm
    if request.method == 'POST':
        form = form_class(request.POST, initial={'pessoa': pessoa})
        if form.is_valid():
            treino = form.save(commit=False)
            treino.pessoa_id = pk
            treino.save()
            if pessoa and form.cleaned_data['modelo']:
                copiar_treino_series(form.cleaned_data['modelo'], treino)
            return redirect(reverse('serie_listar',
                                    kwargs={'pk': treino.pk}))
    else:
        form = form_class(initial={'pessoa': pessoa})
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar treino'})


@login_required
def editar(request, pk):
    treino = Treino.objects.get(pk=pk)
    if treino.pessoa_id:
        form_class = TreinoForm
    else:
        form_class = ModeloTreinoForm
    if request.method == 'POST':
        form = form_class(request.POST, instance=treino)
        if form.is_valid():
            treino.save()
            if treino.pessoa_id:
                return redirect(reverse('aluno_detalhar',
                                        kwargs={'pk': treino.pessoa_id}))
            else:
                return redirect(reverse('treino_listar'))
    else:
        form = form_class(instance=treino)
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
