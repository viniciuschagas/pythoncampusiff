# -*- coding: utf-8 -*-
from django.db import models

TIPO_ATIVIDADE = (
    ('Dojo','Dojo'),
    ('Minicurso','Minicurso'),
    ('Palestra','Palestra')
)

class Responsavel(models.Model):
    nome = models.CharField(verbose_name = 'nome', max_length = 100)
    descricao = models.TextField(verbose_name = 'Descrição')
    instituicao = models.CharField(
        verbose_name = 'instituição',
        max_length = 100
    )
    foto = models.ImageField(
        verbose_name = 'Foto',
        upload_to = 'imagens/fotos_dos_responsaveis'
    )
    
    def __unicode__(self):
        return self.nome


class Atividade(models.Model):
    titulo = models.CharField(verbose_name = 'título', max_length = 300)
    resumo = models.TextField(verbose_name = 'resumo')
    tipo = models.CharField(
        verbose_name = 'tipo',
        max_length = 9,
        choices = TIPO_ATIVIDADE
    )
    responsavel = models.ForeignKey(Responsavel)
    local = models.CharField(verbose_name = 'local', max_length = 100)
    hora = models.TimeField(verbose_name = 'hora')
    
    def __unicode__(self):
        return self.titulo