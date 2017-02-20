from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Usuario
from ..forms import AdicionarPessoaForm, EditarPessoaForm


@login_required
def listar(request):
    pessoas = Usuario.objects.filter()
    return render(request, 'pessoa/listar.html', {'pessoas': pessoas})


@login_required
def detalhar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    return render(request, 'pessoa/detalhar.html', {'pessoa': pessoa})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = AdicionarPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = AdicionarPessoaForm()
    return render(request, 'pessoa/adicionar.html', {'form': form})


@login_required
def editar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditarPessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = EditarPessoaForm(instance=pessoa)
    return render(request, 'pessoa/editar.html', {'form': form})


@login_required
def apagar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect(reverse('pessoa_listar'))
    return render(request, 'pessoa/apagar.html', {'pessoa': pessoa})
