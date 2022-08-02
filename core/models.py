from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import *


_PLEITO = [
    ('1', 'GOVERNADOR'),
    ('2', 'SENADO')
]


class Candidato(models.Model):


    ativa = models.BooleanField(verbose_name="Ativar Candidato", default=True)
    pleito = models.CharField(verbose_name='Pleito', choices=_PLEITO, max_length=2, default='2', null=True)
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
        self.atualizarPorcentagem()


    def atualizarPorcentagem(self):
        total_votos = Candidato.objects.filter(ativa=True).aggregate(models.Sum('votos'))['votos__sum']
        for candidato in Candidato.objects.filter(ativa=True):
            votos_porcentagem = 0.0
            if total_votos:
                votos_porcentagem = float((candidato.votos * 100) / total_votos)
            Candidato.objects.filter(id=candidato.id).update(votos_porcentagem=votos_porcentagem)


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