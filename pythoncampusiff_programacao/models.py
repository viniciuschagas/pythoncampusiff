# -*- coding: utf-8 -*-
from django.db import models

TIPO_ATIVIDADE = (
    ('Dojo','Dojo'),
    ('Minicurso','Minicurso'),
    ('OpenSpace','Open Space'),
    ('Palestra','Palestra')
)

class Responsavel(models.Model):
    
    
    class Meta:
        verbose_name_plural = 'Responsáveis'


    nome = models.CharField(verbose_name = 'nome', max_length = 100)
    descricao = models.TextField(verbose_name = 'Descrição')
    instituicao = models.CharField(
        verbose_name = 'instituição',
        max_length = 100
    )
    foto = models.ImageField(
        verbose_name = 'Foto',
        upload_to = 'imagens/fotos_dos_responsaveis',
        default='imagens/pythoncampusiff_base/responsavel_default.png'
    )
    site = models.CharField(verbose_name="site", max_length=300)
    
    def __unicode__(self):
        return self.nome


class Atividade(models.Model):
    
    class Meta:
        ordering = ('hora','tipo')


    titulo = models.CharField(verbose_name = 'título', max_length = 300)
    resumo = models.TextField(verbose_name = 'resumo', blank=True, null=True)
    tipo = models.CharField(
        verbose_name = 'tipo',
        max_length = 9,
        choices = TIPO_ATIVIDADE,
        blank=True,
        null=True
    )
    responsavel = models.ForeignKey(Responsavel, blank=True, null=True)
    local = models.CharField(
        verbose_name = 'local',
        max_length = 100,
        blank=True,
        null=True
    )
    hora = models.TimeField(verbose_name = 'hora')
    
    def __unicode__(self):
        return self.titulo