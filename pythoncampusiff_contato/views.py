from django.shortcuts import render_to_response
from django.template import RequestContext

def contato(request):
    return render_to_response(
        'contato.html',
        context_instance = RequestContext(request)
    )

