from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.encoding import smart_text
from django.utils.formats import date_format
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import LineChart

from ..models import Usuario, Treino, AvaliacaoFisica
from ..forms import AdicionarPessoaForm, EditarPessoaForm


def gerar_grafico(avaliacoes):
    linhas = [('Data', '% de Gordura')]
    for av in avaliacoes.values_list('data_realizada', 'dobra__resultado')[:10]:
        linhas.append((
            av[0], round(float(av[1]), 2) if av[1] else 0
        ))
    return linhas


@login_required
@user_passes_test(lambda u: u.tipo > 1)
def listar(request):
    pessoas = Usuario.objects.filter(tipo=1)
    return render(request, 'aluno/listar.html', {'pessoas': pessoas})


@login_required
def detalhar(request, pk):
    if request.user.tipo == 1 and str(request.user.pk) != pk:
        raise PermissionDenied
    pessoa = Usuario.objects.get(pk=pk)
    treinos = Treino.objects.filter(pessoa=pessoa.pk)
    avaliacoes = AvaliacaoFisica.objects.filter(pessoa=pessoa.pk)
    chart_ds = SimpleDataSource(gerar_grafico(avaliacoes))
    chart = LineChart(chart_ds)
    return render(request, 'aluno/detalhar.html', {
        'pessoa': pessoa, 'treinos': treinos, 'avaliacoes': avaliacoes,
        'chart': chart
    })


@login_required
@user_passes_test(lambda u: u.tipo > 1)
def apagar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
    return redirect(reverse('aluno_listar'))


@login_required
@user_passes_test(lambda u: u.tipo > 1)
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
@user_passes_test(lambda u: u.tipo > 1)
def editar(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditarPessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('aluno_detalhar', kwargs={'pk': pk}))
    else:
        form = EditarPessoaForm(instance=pessoa)
    return render(request, 'usuario/form.html', {
        'form': form, 'title': 'Editar Aluno',
        'tipo': 'aluno', 'delete_url': reverse('aluno_apagar', kwargs={'pk': pk})
    })
