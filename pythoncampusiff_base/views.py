from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response(
        'index.html',
        context_instance = RequestContext(request)
    )

def local(request):
    return render_to_response(
        'local.html',
        context_instance = RequestContext(request)
    )

def equipe(request):
    return render_to_response(
        'equipe.html',
        context_instance = RequestContext(request)
    )

def equipe_do_site(request):
    return render_to_response(
        'equipe_do_site.html',
        context_instance = RequestContext(request)
    )