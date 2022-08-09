from django.shortcuts import render
from .ferramentas.buscas import Candidato as BuscasCandidato
from .ferramentas.funcoes import Lancamento
from .models import Pleito
from django.http import JsonResponse
    
class Core():

    def index(request):
        template_name = "core/index.html"
        context = {'pleitos': Pleito.objects.all()}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)


    def apuracao(request, id_pleito):
        template_name = "core/apuracao.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'lista_candidatos': buscasCandidato.get_lista_html_candidatos(id_pleito),
                   'pleito': Pleito.objects.get(id=id_pleito)
                  }
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)


    def lancamento(request, id_pleito):
        template_name = "core/lancamento.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'formulario': buscasCandidato.get_formulario_html_candidatos(id_pleito)}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
        elif request.method == 'POST':
            Lancamento(request).registrarVotos()
            return render(request=request, template_name=template_name, context=context)


class CoreAjax():

    def atualizarLista(request):
        return JsonResponse({'lista_candidatos': BuscasCandidato(request).get_lista_html_candidatos()})