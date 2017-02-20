from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Exercicio


@login_required
def listar(request):
    exercicios = Exercicio.objects.all()
    return render(request, 'exercicio/listar.html', {'exercicios': exercicios})


@login_required
def detalhar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    return render(request, 'exercicio/detalhar.html', {'exercicio': exercicio})


ExercicioForm = modelform_factory(Exercicio, fields=('__all__'))


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = ExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('exercicio_listar'))
    else:
        form = ExercicioForm()
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Adicionar Exercicio'
    })


@login_required
def editar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExercicioForm(request.POST, instance=exercicio)
        if form.is_valid():
            form.save()
            return redirect(reverse('exercicio_listar'))
    else:
        form = ExercicioForm(instance=exercicio)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Exercicio', 'tipo': 'exercício',
        'delete_url': reverse('exercicio_apagar', kwargs={'pk': pk})
    })


@login_required
def apagar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    if request.method == 'POST':
        exercicio.delete()
    return redirect(reverse('exercicio_listar'))
