from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.encoding import smart_text
from django.utils.formats import date_format
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.highcharts import LineChart, AreaChart
from ..models import Usuario, Treino, AvaliacaoFisica
from ..forms import AdicionarPessoaForm, EditarPessoaForm


def gerar_grafico_gordura(avaliacoes):
    linhas = [('Data', '% de Gordura')]
    for av in avaliacoes.values_list('data_realizada', 'dobra__resultado'):
        linhas.append((
            date_format(av[0], 'SHORT_DATE_FORMAT'),
            round(float(av[1]), 2) if av[1] else 0
        ))
    print(linhas)
    return linhas

def gerar_grafico_perimetria(avaliacoes):
    linhas = [('Data', 'Peso', 'Pescoco', 'Torax', 'Cintura', 'Abdome', 'Quadril', 'Bicipes Direito', 'Bicipes Esquerdo',
     'Tricipes Direito', 'Tricipes Esquerdo', 'Antebraço Direito', 'Antebraço Esquerdo', 'Coxa Direita', 'Coxa Esquerda', 
     'Panturrilha Direta', 'Panturrilha Esquerda')]
    for av in avaliacoes.values_list('data_realizada',
        'perimetria__peso', 'perimetria__pescoco', 'perimetria__torax', 'perimetria__cintura',
        'perimetria__abdome', 'perimetria__quadril', 'perimetria__bicipesdireito', 'perimetria__bicipesesquedo',
        'perimetria__tricipesdireito', 'perimetria__tricipesesquerdo', 'perimetria__antebracodireito', 'perimetria__antebracoesquerdo', 
        'perimetria__coxadireita', 'perimetria__coxaesquerda', 'perimetria__panturrilhadireta', 'perimetria__panturrilhaesquerda'):
        linhas.append(av)
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
    gordura_chart = LineChart(SimpleDataSource(
        gerar_grafico_gordura(avaliacoes)))
    gordura_chart.options['title'] = '% de gordura'
    perimetria_chart = LineChart(SimpleDataSource(
        gerar_grafico_perimetria(avaliacoes)))
    perimetria_chart.options['title'] = 'Perimetria'
    return render(request, 'aluno/detalhar.html', {
        'pessoa': pessoa, 'treinos': treinos, 'avaliacoes': avaliacoes,
        'gordura_chart': gordura_chart, 'perimetria_chart': perimetria_chart
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
