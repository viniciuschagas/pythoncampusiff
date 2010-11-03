# -*- coding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail
from pythoncampusiff_atividades.models import Atividade

class Inscrito(models.Model):
    ESTADOS = (('pendente', 'Pendente'),
              ('confirmado', 'Confirmado'),
              ('espera', 'Espera'))
    
    nome = models.CharField(verbose_name='nome',max_length=100)
    instituicao = models.CharField(verbose_name='instituição',max_length=100)
    cpf = models.CharField(verbose_name='CPF',max_length=11,unique=True)
    email = models.EmailField(verbose_name='E-mail')
    minicurso_da_manha = models.ForeignKey(
        Atividade,
        null=True,
        blank=True,
        related_name='minicurso_da_manha',
        verbose_name='minicurso da manhã'
    )
    minicurso_da_tarde = models.ForeignKey(
        Atividade,
        null=True,
        blank=True,
        related_name='minicurso_da_tarde',
        verbose_name='minicurso da tarde'
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendente'
    )
    
    def __unicode__(self):
        return self.nome

    def inscrever(self, minicurso_id, periodo):
        minicurso = Atividade.objects.get(id=minicurso_id)
        if periodo == 'manha':
            self.minicurso_da_manha = minicurso
        elif periodo == 'tarde':
            self.minicurso_da_tarde = minicurso
        # Adicionar id de inscricao no e-mail
        #send_mail(u'[PythOnCampus IFF] Confirme sua presença!', u'Atenção! Para assegurar sua vaga nos minicursos, traga 1kg de arroz, feijão ou macarrão para cada minicurso no qual você estiver inscrito até 10/11/2009. O local de confirmação e arrecadação é o NSI - Núcleo de Pesquisa em Sistemas de Informação (Sala 104, Bloco F), localizado no IFF Campus Campos-Centro (Antigo Cefet Campos), das 14:00 às 19:00 hs. Importante: Será respeitada a ordem de entrega do alimento para o preenchimento das vagas!', 'pythoncampus@iff.edu.br', [self.email,], fail_silently=True)

    def confirmar_inscricao(self):
        try:
            self.minicurso_da_manha.decrementar_vaga()
        except AttributeError:
            pass

        try:
            self.minicurso_da_tarde.decrementar_vaga()
        except AttributeError:
            pass

    def save(self,*args,**kwargs):
        super(Inscrito, self).save(*args,**kwargs)
        if self.estado == 'confirmado':
            self.confirmar_inscricao()
