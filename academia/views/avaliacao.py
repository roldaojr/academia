from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ..models import AvaliacaoFisica, Usuario
from ..forms import AvaliacaoForm


@login_required
def detalhar(request, pk):
    avaliacao = AvaliacaoFisica.objects.get(pk=pk)
    return render(request, 'avaliacao/detalhar.html', {'avaliacao': avaliacao})


@login_required
def adicionar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.pessoa = pessoa
            avaliacao.save()
            return redirect(reverse('avaliacao_detalhar',
                                    kwargs={'pk': avaliacao.pk}))
    else:
        form = AvaliacaoForm()
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar Avaliação física'})


@login_required
def editar(request, pk):
    avaliacao = AvaliacaoFisica.objects.get(pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect(reverse('avaliacao_detalhar', kwargs={'pk': pk}))
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Avalição física',
        'tipo': 'avaliação física',
        'delete_url': reverse('avaliacao_apagar', kwargs={'pk': pk})
    })


@login_required
def apagar(request, pk):
    avaliacao = AvaliacaoFisica.objects.get(pk=pk)
    pessoa_id = avaliacao.pessoa_id
    if request.method == 'POST':
        avaliacao.delete()
    return redirect(reverse('aluno_detalhar', kwargs={'pk': pessoa_id}))
