from ..models import Candidato, Pleito, Voto
from django.db import models


class Lancamento:


    def __init__(self, request):
        self.request = request

    '''def somarVotos(self):
        post = self.request.POST.copy()
        pleito = Pleito.objects.filter(id=self.id_pleito)
        post.pop('csrfmiddlewaretoken')
        pleito_total_votos = pleito.first().votos

        for id_candidato, votos in post.items():
            try:
                votos = int(votos)
                candidato = Candidato.objects.filter(id=id_candidato)
                votos_candidato = candidato.first().votos + votos
                if votos_candidato < 0: votos_candidato = 0
                candidato.update(votos=votos_candidato)
                candidato.first().atualizarPorcentagem()
                pleito_total_votos += votos

            except Exception as e:
                print('Lancamento somarVotos()', e)

        pleito.update(votos=pleito_total_votos)'''

    def registrarVotos(self):
        post = self.request.POST.copy()
        post.pop('csrfmiddlewaretoken')

        for id_candidato, votos_candidato in post.items():
            try:
                votos_candidato = int(votos_candidato)
                if votos_candidato > 0:
                    candidato = Candidato.objects.get(id=id_candidato)
                    pleito = candidato.pleito
                    Voto.objects.create(candidato=Candidato.objects.get(id=id_candidato), votos=votos_candidato, pleito=pleito)
            except Exception as e:
                print('RegistrarVotos somarVotos()', e)

        self.atualizarVotos()


    def atualizarVotos(self):
        try:
            for pleito in Pleito.objects.all():
                totalVotos = Voto.objects.filter(pleito=pleito).aggregate(models.Sum('votos'))['votos__sum']
                if totalVotos:
                    pleito.votos = totalVotos
                else:
                    pleito.votos = 0

                pleito.save()

            for candidato in Candidato.objects.all():
                total_votos = Voto.objects.filter(candidato=candidato).aggregate(models.Sum('votos'))['votos__sum']

                if total_votos:
                    candidato.votos_porcentagem = float((total_votos * 100) / candidato.pleito.votos)
                    candidato.votos = total_votos
                else:
                    candidato.votos_porcentagem = 0.0
                    candidato.votos = 0

                #print(candidato, candidato.votos, candidato.votos_porcentagem)

                candidato.save()

        except Exception as e:
            print('atualizarVotos()', e)
