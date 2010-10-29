from django.shortcuts import render_to_response
from django.template import RequestContext

def programacao(request):
    return render_to_response(
        'programacao.html',
        context_instance = RequestContext(request)
    )

