from ..models import Candidato


class Lancamento:


    def __init__(self, request):
        self.request = request


    def somarVotos(self):
        post = self.request.POST.copy()
        post.pop('csrfmiddlewaretoken')
        for id_candidato, votos in post.items():
            try:
                candidato = Candidato.objects.filter(id=id_candidato)
                votos = candidato.first().votos + int(votos)
                if votos < 0:
                    votos = 0
                candidato.update(votos=votos)
                candidato.first().atualizarPorcentagem()
            except Exception as e:
                print('Lancamento somarVotos()', e)
