from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from forms import FormularioDeContato

def contato(request):
    if request.method  == 'POST':
        formulario_contato = FormularioDeContato(request.POST)
        if formulario_contato.is_valid():
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')
            mensagem = request.POST.get('mensagem')
            send_mail(
                assunto,
                mensagem,
                email,
                ['pythoncampus@iff.edu.br'],
                fail_silently=False
            )
            return HttpResponseRedirect('/sucesso_contato/')
        else:
            return render_to_response(
                'contato.html',
                {'form':formulario_contato},
                context_instance=RequestContext(request)
            )
    else:
        form = FormularioDeContato()
        return render_to_response(
            'contato.html',
            {'form':form},
            context_instance=RequestContext(request)
        )

