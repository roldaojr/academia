from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Dobra


DobraForm = modelform_factory(Dobra, exclude=('avaliacaofisica', 'resultado'))


@login_required
def adicionar(request, pk):
    if request.method == 'POST':
        form = DobraForm(request.POST, request.FILES)
        if form.is_valid():
            dobra = form.save(commit=False)
            dobra.avaliacaofisica_id = pk
            dobra.save()
            return redirect(reverse('avaliacao_detalhar', kwargs={'pk': pk}))
    else:
        form = DobraForm()
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Cadastrar Dobra'
    })


@login_required
def editar(request, pk):
    dobra = Dobra.objects.get(pk=pk)
    if request.method == 'POST':
        form = DobraForm(request.POST, instance=dobra)
        if form.is_valid():
            form.save()
            return redirect(reverse('avaliacao_detalhar',
                                    kwargs={'pk': dobra.avaliacaofisica_id}))
    else:
        form = DobraForm(instance=dobra)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Dobra'
    })
