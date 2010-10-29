from django.shortcuts import render_to_response
from django.template import RequestContext

def inscricao(request):
    return render_to_response(
        'inscricao.html',
        context_instance = RequestContext(request)
    )
