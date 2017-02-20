from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ..models import Usuario, Treino, AvaliacaoFisica
from ..forms import AdicionarPessoaForm, EditarPessoaForm


@login_required
def listar(request):
    pessoas = Usuario.objects.filter(tipo=1)
    return render(request, 'aluno/listar.html', {'pessoas': pessoas})


@login_required
def detalhar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    treinos = Treino.objects.filter(pessoa=pessoa.pk)
    avaliacoes = AvaliacaoFisica.objects.filter(pessoa=pessoa.pk)
    return render(request, 'aluno/detalhar.html', {
        'pessoa': pessoa, 'treinos': treinos, 'avaliacoes': avaliacoes
    })


@login_required
def apagar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
    return redirect(reverse('aluno_listar'))


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = AdicionarPessoaForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.tipo = 1
            aluno.save()
            return redirect(reverse('aluno_listar'))
    else:
        form = AdicionarPessoaForm()
    return render(request, 'change_form.html',
                  {'form': form, 'title': 'Adicionar Aluno'})


@login_required
def editar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditarPessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('aluno_detalhar', kwargs={'pk': pk}))
    else:
        form = EditarPessoaForm(instance=pessoa)
    return render(request, 'change_form.html', {
        'form': form, 'title': 'Editar Aluno',
        'tipo': 'aluno', 'delete_url': reverse('pessoa_apagar', kwargs={'pk': pk})
    })
