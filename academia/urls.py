from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import (index, pessoa, exercicio, treino, serie, aluno, avaliacao,
                    perimetria, dobra, anamnese_pergunta, anamnese_resposta)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pessoa/adicionar$', pessoa.adicionar, name='pessoa_adicionar'),
    url(r'^pessoa/editar/(?P<pk>\d+)$', pessoa.editar, name='pessoa_editar'),
    url(r'^pessoa/apagar/(?P<pk>\d+)$', pessoa.apagar, name='pessoa_apagar'),
    url(r'^pessoa$', pessoa.listar, name='pessoa_listar'),

    url(r'^exercicio/adicionar$', exercicio.adicionar, name='exercicio_adicionar'),
    url(r'^exercicio/editar/(?P<pk>\d+)$', exercicio.editar, name='exercicio_editar'),
    url(r'^exercicio/apagar/(?P<pk>\d+)$', exercicio.apagar, name='exercicio_apagar'),
    url(r'^exercicio/detalhar/(?P<pk>\d+)$', exercicio.detalhar, name='exercicio_detalhar'),
    url(r'^exercicio/listar$', exercicio.listar, name='exercicio_listar'),

    url(r'^anamnese/adicionar$', anamnese_pergunta.adicionar, name='anamnese_adicionar'),
    url(r'^anamnese/editar/(?P<pk>\d+)$', anamnese_pergunta.editar, name='anamnese_editar'),
    url(r'^anamnese/apagar/(?P<pk>\d+)$', anamnese_pergunta.apagar, name='anamnese_apagar'),
    url(r'^anamnese/listar$', anamnese_pergunta.listar, name='anamnese_listar'),
    url(r'^anamnese/responder/(?P<pk>\d+)$', anamnese_resposta.responder,
        name='anamnese_responder'),

    url(r'^aluno/adicionar$', aluno.adicionar, name='aluno_adicionar'),
    url(r'^aluno/editar/(?P<pk>\d+)$', aluno.editar, name='aluno_editar'),
    url(r'^aluno/detalhar/(?P<pk>\d+)$', aluno.detalhar,name='aluno_detalhar'),
    url(r'^aluno/listar$', aluno.listar, name='aluno_listar'),

    url(r'^treino/adicionar/(?P<pk>\d+)$', treino.adicionar, name='treino_adicionar'),
    url(r'^treino/editar/(?P<pk>\d+)$', treino.editar, name='treino_editar'),
    url(r'^treino/apagar/(?P<pk>\d+)$', treino.apagar, name='treino_apagar'),

    url(r'^serie/apagar/(?P<pk>\d+)$', serie.apagar, name='serie_apagar'),
    url(r'^serie/listar/(?P<pk>\d+)$', serie.listar, name='serie_listar'),

    url(r'^avaliacao/adicionar/(?P<pk>\d+)$', avaliacao.adicionar, name='avaliacao_adicionar'),
    url(r'^avaliacao/editar/(?P<pk>\d+)$', avaliacao.editar, name='avaliacao_editar'),
    url(r'^avaliacao/apagar/(?P<pk>\d+)$', avaliacao.apagar, name='avaliacao_apagar'),
    url(r'^avaliacao/detalhar/(?P<pk>\d+)$', avaliacao.detalhar, name='avaliacao_detalhar'),

    url(r'^perimetria/adicionar/(?P<pk>\d+)$', perimetria.adicionar, name='perimetria_adicionar'),
    url(r'^perimetria/editar/(?P<pk>\d+)$', perimetria.editar, name='perimetria_editar'),

    url(r'^dobra/adicionar/(?P<pk>\d+)$', dobra.adicionar, name='dobra_adicionar'),
    url(r'^dobra/editar/(?P<pk>\d+)$', dobra.editar, name='dobra_editar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
