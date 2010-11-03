# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import Atividade

def retornar_minicursos():
    todos_os_minicursos = Atividade.objects.filter(tipo='Minicurso')
    return todos_os_minicursos
    
def gerar_minicursos_da_manha(request):
    todos_os_minicursos = retornar_minicursos()
    minicursos_da_manha = []
    
    for minicurso in todos_os_minicursos:
        if minicurso.hora.isoformat()[:5] < '12:00':
            minicursos_da_manha.append(minicurso)

    html = ''
    
    if len(minicursos_da_manha) > 0:
        html += u'Minicurso da manhã: '
        html += '<select id="id_minicurso_da_manha" name="minicurso_da_manha">'
        html += '<option selected="selected" value="">---------</option>'

        for minicurso in minicursos_da_manha:
            html += '<option value="%s">%s</option>' %(
                minicurso.id, minicurso.titulo
            )

        html += '</select>'

    return HttpResponse(html)

def gerar_minicursos_da_tarde(request):
    todos_os_minicursos = retornar_minicursos()
    minicursos_da_tarde = []
    
    for minicurso in todos_os_minicursos:
        if (minicurso.hora.isoformat()[:5] > '12:00') and\
            (minicurso.hora.isoformat()[:5] < '18:00'):
            minicursos_da_tarde.append(minicurso)

    html = ''
    
    if len(minicursos_da_tarde) > 0:
        html += u'Minicurso da tarde: '
        html += '<select id="id_minicurso_da_tarde" name="minicurso_da_tarde">'
        html += '<option selected="selected" value="">---------</option>'

        for minicurso in minicursos_da_tarde:
            html += '<option value="%s">%s</option>' %(
                minicurso.id, minicurso.titulo
            )

        html += '</select>'

    return HttpResponse(html)