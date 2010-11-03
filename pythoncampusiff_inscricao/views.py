# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from pythoncampusiff_atividades.models import Atividade
from forms import FormularioDeInscrito
from models import Inscrito


def inscricao(request):
    formulario = FormularioDeInscrito()
    if request.method == 'POST':
        formulario = FormularioDeInscrito(request.POST)
        if formulario.is_valid():
            inscrito = formulario.save(commit=False)
            inscrito_em_minicurso = False
            minicurso_da_manha = request.POST.get('minicurso_da_manha','')
            minicurso_da_tarde = request.POST.get('minicurso_da_tarde','')
            if minicurso_da_manha != '':
                inscrito.inscrever(minicurso_da_manha,'manha')
                inscrito_em_minicurso = True
            if minicurso_da_tarde != '':
                inscrito.inscrever(minicurso_da_tarde,'tarde')
                inscrito_em_minicurso = True
            inscrito.save()
            return render_to_response(
                'sucesso_na_inscricao.html',
                {
                    'inscrito':inscrito,
                    'inscrito_em_minicurso': inscrito_em_minicurso
                },
                context_instance = RequestContext(request)
            )
    return render_to_response(
        'inscricao.html',
        {'formulario': formulario},
        context_instance = RequestContext(request)
    )
@login_required
def confirmar_inscricao(request):
    minicursos = Atividade.objects.filter(tipo='Minicurso')
    if request.method == 'POST':
        id_inscrito = request.POST.get('id_inscrito')
        inscrito = Inscrito.objects.get(id=id_inscrito)
        inscrito.estado = 'confirmado'
        inscrito.save()
        return render_to_response(
            'confirmar_inscricao.html',
            {
                'minicursos': minicursos,
                'mensagem': u'Confirmação Realizada Com Sucesso!'
            },
            context_instance = RequestContext(request)
        )
    return render_to_response(
        'confirmar_inscricao.html',
        {'minicursos': minicursos},
        context_instance = RequestContext(request)
    )

def buscar_inscrito(request):
    identificacao = request.GET.get('identificacao')
    try:
        identificacao_int = int(identificacao)
        try:
            inscrito = Inscrito.objects.get(id=identificacao_int)
        except Inscrito.DoesNotExist:
            inscrito = None
    except ValueError:
        try:
            inscrito = Inscrito.objects.get(nome=identificacao.upper())
        except Inscrito.DoesNotExist:
            inscrito = None
    
    if inscrito is not None:
        minicurso_da_manha = inscrito.minicurso_da_manha
        minicurso_da_tarde = inscrito.minicurso_da_tarde
        
        status_minicurso_da_manha = ''
        status_minicurso_da_tarde = ''
        
        if minicurso_da_manha is not None:
            minicurso_da_manha_titulo = minicurso_da_manha.titulo
            if minicurso_da_manha.vagas_disponiveis > 0:
                status_minicurso_da_manha = u'Disponível'
            else:
                status_minicurso_da_manha = 'Esgotado'
        else:
            minicurso_da_manha_titulo = 'Nenhum'
            status_no_minicurso_da_manha = ''
        
        if minicurso_da_tarde is not None:
            minicurso_da_tarde_titulo = minicurso_da_tarde.titulo
            if minicurso_da_tarde.vagas_disponiveis > 0:
                status_minicurso_da_tarde = u'Disponível'
            else:
                status_minicurso_da_tarde = 'Esgotado'
        else:
            minicurso_da_tarde_titulo = 'Nenhum'
            status_no_minicurso_da_tarde = ''
        
        resposta = simplejson.dumps(
            [{
                'inscritoEncontrado': 'True',
                'idInscrito': inscrito.id,
                'nomeInscrito': inscrito.nome,
                'estadoInscrito': inscrito.estado,
                'minicurso_da_manha': minicurso_da_manha_titulo,
                'minicurso_da_tarde': minicurso_da_tarde_titulo,
                'status_minicurso_da_manha': status_minicurso_da_manha,
                'status_minicurso_da_tarde': status_minicurso_da_tarde,
            }],
            ensure_ascii = False
        )
    else:
        resposta = simplejson.dumps(
            [{
                'inscritoEncontrado': 'False',
                'identificacao': identificacao,
            }]
        )

    return HttpResponse(resposta, mimetype = "aplication/json")

@login_required
def lista_de_presenca_do_minicurso(request, minicurso_id):
    minicurso = Atividade.objects.get(id=minicurso_id)
    if minicurso.hora.isoformat()[:5] < '12:00':
        inscritos =\
    minicurso.minicurso_da_manha.filter(estado='confirmado').order_by('nome')
    elif minicurso.hora.isoformat()[:5] > '12:00':
        inscritos =\
    minicurso.minicurso_da_tarde.filter(estado='confirmado').order_by('nome')
    
    return render_to_response(
        'lista_de_presenca_do_minicurso.html',
        {
            'minicurso': minicurso,
            'inscritos': inscritos
        },
        context_instance = RequestContext(request)
    )

@login_required
def lista_de_presenca_das_palestras(request):
    inscritos = Inscrito.objects.all().order_by('nome')
    return render_to_response(
        'lista_de_presenca_das_palestras.html',
        {'inscritos': inscritos},
        context_instance = RequestContext(request)
    )

@login_required
def listas_de_presenca(request):
    minicursos = Atividade.objects.filter(tipo='Minicurso')
    return render_to_response(
        'listas_de_presenca.html',
        {'minicursos': minicursos},
        context_instance = RequestContext(request)
    )

def organizacao(request):
    return render_to_response(
        'organizacao.html',
        context_instance = RequestContext(request)
    )
#Login e Logout
def inscricao_login(request):
    nome_de_usuario = request.POST['nome_de_usuario']
    senha = request.POST['senha']
    usuario = authenticate(username=nome_de_usuario, password=senha)
    if usuario is not None:
        if usuario.is_active:
            login(request, usuario)
            return HttpResponseRedirect('/inscricao/organizacao')
        else:
            return render_to_response(
                'organizacao.html',
                {'mensagem_de_erro':u'Sua conta está inativa!'},
                context_instance = RequestContext(request)
            )
    else:
        return render_to_response(
            'organizacao.html',
            {'mensagem_de_erro':u'Login ou Senha inválido!'},
            context_instance = RequestContext(request)
        )

def inscricao_logout(request):
    logout(request)
    return HttpResponseRedirect('/inscricao/organizacao')
