from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def index(request):
    if request.user.tipo == 1:
        return redirect('aluno_detalhar', request.user.pk)
    else:
        return redirect('aluno_listar')
