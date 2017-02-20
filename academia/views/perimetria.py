from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from ..models import Perimetria


PerimetriaForm = modelform_factory(Perimetria, exclude=('avaliacaofisica',))


@login_required
def adicionar(request, pk):
    if request.method == 'POST':
        form = PerimetriaForm(request.POST, request.FILES)
        if form.is_valid():
            perimetria = form.save(commit=False)
            perimetria.avaliacaofisica_id = pk
            perimetria.save()
            return redirect(reverse('avaliacao_detalhar', kwargs={'pk': pk}))
    else:
        form = PerimetriaForm()
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Cadastrar Perimetria'
    })


@login_required
def editar(request, pk):
    perimetria = Perimetria.objects.get(pk=pk)
    if request.method == 'POST':
        form = PerimetriaForm(request.POST, instance=perimetria)
        if form.is_valid():
            form.save()
            return redirect(reverse('avaliacao_detalhar',
                                    kwargs={'pk': perimetria.avaliacaofisica_id}))
    else:
        form = PerimetriaForm(instance=perimetria)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Perimetria'
    })
