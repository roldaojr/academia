from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import ModelForm, inlineformset_factory
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import RespostaAnamnese, PerguntaAnamnese, AvaliacaoFisica


RespostaAnamneseFormSet = inlineformset_factory(
    AvaliacaoFisica, RespostaAnamnese, extra=0, fields=('texto', 'observacao'))


@login_required
def responder(request, pk):
    avaliacao = AvaliacaoFisica.objects.get(pk=pk)
    for pergunta in PerguntaAnamnese.objects.all():
        RespostaAnamnese.objects.get_or_create(
            pergunta=pergunta, avaliacaofisica=avaliacao)

    if request.method == 'POST':
        formset = RespostaAnamneseFormSet(request.POST, request.FILES, instance=avaliacao)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('avaliacao_detalhar', kwargs={'pk': pk}))
    else:
        formset = RespostaAnamneseFormSet(instance=avaliacao)

    return render(request, 'anamnese/responder.html', {'formset': formset})
