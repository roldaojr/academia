from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Usuario
from ..forms import AdicionarUsuarioForm, EditarUsuarioForm


@login_required
def listar(request):
    usuarios = Usuario.objects.exclude(tipo=1)
    return render(request, 'usuario/listar.html', {'usuarios': usuarios})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = AdicionarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario_listar'))
    else:
        form = AdicionarUsuarioForm()
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar Usuário'})


@login_required
def editar(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario_listar'))
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Editar Usuário'})


@login_required
def apagar(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
    return redirect(reverse('usuario_listar'))
