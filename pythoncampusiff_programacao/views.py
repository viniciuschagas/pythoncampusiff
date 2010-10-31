from django.shortcuts import render_to_response
from django.template import RequestContext
from pythoncampusiff_atividades.models import Atividade

def programacao(request):
    atividades = Atividade.objects.all()
    return render_to_response(
        'programacao.html',
        {'atividades': atividades},
        context_instance = RequestContext(request)
    )

