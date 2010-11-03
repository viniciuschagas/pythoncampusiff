from django.conf.urls.defaults import *

urlpatterns = patterns('pythoncampusiff_inscricao.views',
    (r'^$', 'inscricao'),
    (r'^confirmar$', 'confirmar_inscricao'),
    (r'^buscar_inscrito$','buscar_inscrito'),
    (
        r'^lista_de_presenca_do_minicurso/(?P<minicurso_id>\d+)$',
        'lista_de_presenca_do_minicurso'
    ),
    (r'^listas_de_presenca$','listas_de_presenca'),
    (r'^lista_de_presenca_das_palestras$','lista_de_presenca_das_palestras'),
    (r'^organizacao$','organizacao'),
    (r'^inscricao_login','inscricao_login'),
    (r'^inscricao_logout','inscricao_logout'),
)