from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Usuario
from ..forms import AdicionarUsuarioForm, EditarUsuarioForm


@login_required
def listar(request):
    pessoas = Usuario.objects.exclude(tipo=1)
    return render(request, 'pessoa/listar.html', {'pessoas': pessoas})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = AdicionarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = AdicionarUsuarioForm()
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar usuário'})


@login_required
def editar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = EditarUsuarioForm(instance=pessoa)
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Editar Usuário'})


@login_required
def apagar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
    return redirect(reverse('pessoa_listar'))
