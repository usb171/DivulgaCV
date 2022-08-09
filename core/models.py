from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import *


class Candidato(models.Model):


    ativa = models.BooleanField(verbose_name="Ativar Candidato", default=True)
    pleito = models.ForeignKey(to='core.pleito', verbose_name='pleito', on_delete=models.SET_NULL, blank=False, null=True)
    ordem = models.IntegerField(verbose_name="Ordem", default=0, blank=False, null=False)
    nome = models.CharField(max_length=220, verbose_name='Nome', blank=False, null=False)
    partido = models.ForeignKey(to='core.Partido', verbose_name='Partido', on_delete=models.CASCADE, blank=False, null=False)
    votos = models.IntegerField(verbose_name='Votos', validators=[MinValueValidator(0)], blank=False, null=False, default=0)
    votos_porcentagem = models.FloatField(verbose_name='Votos em Porcentagem',
                                            validators=[MinValueValidator(0.0),
                                                        MaxValueValidator(100.0)],
                                            blank=False, null=False,
                                            default=0.0)
    foto = models.FileField(verbose_name='Foto 160x120', upload_to='candidatos', blank=False, null=True)
    created_at = models.DateTimeField('Registrado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)


    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'


    def save(self, *args, **kwargs):
        super(Candidato, self).save(*args, **kwargs)


    def __str__(self):
        return self.nome


class Partido(models.Model):


    nome = models.CharField(max_length=220, verbose_name='Nome', blank=False, null=False)
    sigla = models.CharField(max_length=220, verbose_name='Sigla', blank=False, null=False)
    created_at = models.DateTimeField('Registrado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)


    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'


    def __str__(self):
        return self.nome


class Pleito(models.Model):


    nome = models.CharField(max_length=220, verbose_name='Nome', blank=False, null=False, unique=True)
    cartela = models.FileField(verbose_name='Cartela 000X000', upload_to='cartelas', blank=False, null=True)
    votos = models.IntegerField(verbose_name='Total de Votos', validators=[MinValueValidator(0)], blank=False, null=False, default=0)

    created_at = models.DateTimeField('Registrado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)


    class Meta:
        verbose_name = 'Pleito'
        verbose_name_plural = 'Pleitos'


    def __str__(self):
        return self.nome


class Voto(models.Model):


    candidato = models.ForeignKey(to='core.Candidato', verbose_name='Candidato', on_delete=models.CASCADE, blank=False, null=False)
    votos = models.IntegerField(verbose_name='N° Votos', validators=[MinValueValidator(0)], blank=False, null=False, default=0)
    pleito = models.ForeignKey(to='core.Pleito', verbose_name='pleito', on_delete=models.SET_NULL, blank=False, null=True)

    created_at = models.DateTimeField('Registrado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)


    class Meta:
        verbose_name = 'Histórico de Voto'
        verbose_name_plural = 'Históricos de Votos'


    def __str__(self):
        return self.candidato.nome