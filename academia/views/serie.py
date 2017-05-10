from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Serie, Treino, Exercicio


@login_required
def listar(request, pk):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('serie_listar', kwargs={'pk': pk}))
    else:
        form = SerieForm()

    treino = Treino.objects.get(pk=pk)
    series = Serie.objects.filter(treino_id=pk).order_by('dia')
    exercicios = Exercicio.objects.all()
    return render(request, 'serie/listar.html', {
        'series': series, 'exercicios': exercicios, 'treino': treino,
        'tipo': 'serie','delete_url': reverse('serie_apagar', kwargs={'pk': 0}),
        'treino_id': pk, 'form': form
    })


SerieForm = modelform_factory(Serie, fields=('__all__'))


@login_required
def apagar(request, pk):
    serie = Serie.objects.get(pk=pk)
    if request.method == 'POST':
        serie.delete()

    return redirect(reverse('serie_listar', kwargs={'pk': serie.treino_id}))
