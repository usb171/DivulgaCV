from django.shortcuts import render
from .ferramentas.buscas import Candidato as BuscasCandidato
from .ferramentas.funcoes import Lancamento
from django.http import JsonResponse


class Core():

    def index(request):
        template_name = "core/index.html"
        context = {}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
            

    def governador(request):
        template_name = "core/governador.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'lista_candidatos': buscasCandidato.get_lista_html_candidatos()}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)


    def senador(request):
        template_name = "core/senador.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'lista_candidatos': buscasCandidato.get_lista_html_candidatos()}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)


    def lancamentoGovernador(request):
        template_name = "core/lancamento.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'formulario': buscasCandidato.get_formulario_html_candidatos(1)}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
        elif request.method == 'POST':
            Lancamento(request).somarVotos()
            return render(request=request, template_name=template_name, context=context)


    def lancamentoSenador(request):
        template_name = "core/lancamento.html"
        buscasCandidato = BuscasCandidato(request)
        context = {'formulario': buscasCandidato.get_formulario_html_candidatos(2)}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
        elif request.method == 'POST':
            Lancamento(request).somarVotos()
            return render(request=request, template_name=template_name, context=context)


class CoreAjax():


    def atualizarLista(request):
        return JsonResponse({'lista_candidatos': BuscasCandidato(request).get_lista_html_candidatos()})