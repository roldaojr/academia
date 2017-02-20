from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import PerguntaAnamnese


PerguntaAnamneseForm = modelform_factory(PerguntaAnamnese, fields=('__all__'))


@login_required
def listar(request):
    perguntas = PerguntaAnamnese.objects.all()
    return render(request, 'anamnese/listar.html', {'perguntas': perguntas})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PerguntaAnamneseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('anamnese_listar'))
    else:
        form = PerguntaAnamneseForm()
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Adicionar Pergunta',
    })


@login_required
def editar(request, pk):
    pergunta = PerguntaAnamnese.objects.get(pk=pk)
    if request.method == 'POST':
        form = PerguntaAnamneseForm(request.POST, instance=pergunta)
        if form.is_valid():
            form.save()
            return redirect(reverse('anamnese_listar'))
    else:
        form = PerguntaAnamneseForm(instance=pergunta)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Pergunta', 'tipo': 'pergunta',
        'delete_url': reverse('anamnese_apagar', kwargs={'pk': pk})
    })


@login_required
def apagar(request, pk):
    pergunta = PerguntaAnamnese.objects.get(pk=pk)
    if request.method == 'POST':
        pergunta.delete()
    return redirect(reverse('anamnese_listar'))

