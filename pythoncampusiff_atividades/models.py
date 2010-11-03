# -*- coding: utf-8 -*-
from django.db import models

TIPO_ATIVIDADE = (
    ('Dojo','Dojo'),
    ('Minicurso','Minicurso'),
    ('OpenSpace','Open Space'),
    ('Palestra','Palestra'),
    ('Outros','Outros')
)

class Responsavel(models.Model):
    
    
    class Meta:
        verbose_name_plural = 'Responsáveis'


    nome = models.CharField(verbose_name = 'nome', max_length = 100)
    minicurriculo = models.TextField(verbose_name = 'mini-curriculo')
    telefone = models.CharField(verbose_name='telefone', max_length=14)
    instituicao = models.CharField(
        verbose_name = 'instituição/empresa',
        max_length = 100
    )
    cidade = models.CharField(verbose_name='cidade', max_length=200)
    uf = models.CharField(verbose_name='UF', max_length=2)
    foto = models.ImageField(
        verbose_name = 'Foto',
        upload_to = 'imagens/fotos_dos_responsaveis',
        default='imagens/pythoncampusiff_base/responsavel_default.png'
    )
    
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
    vagas_disponiveis = models.IntegerField(
        verbose_name='vagas disponíveis',
        default=0
    )
    
    def __unicode__(self):
        return self.titulo

    def decrementar_vaga(self):
        if self.tipo == 'Minicurso':
            if self.vagas_disponiveis >= 1:
                self.vagas_disponiveis -= 1
                self.save()