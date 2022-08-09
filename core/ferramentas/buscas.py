from ..models import Candidato as ModelCandidato, Pleito
from django.template.loader import render_to_string
from django.core.paginator import Paginator


class Candidato:


    def __init__(self, request):
        self.request = request


    def get_lista_html_candidatos(self, id_pleito=-1):
        template = 'core/render/lista_candidatos_final.html'
        context = {}

        try:
            page = self.request.GET.get('grupo')
            id_pleito = self.request.GET.get('pleito') if id_pleito == -1 else id_pleito
            paginator = Paginator(ModelCandidato.objects.order_by("-votos").filter(ativa=True, pleito=id_pleito), 4)
            context['candidatos'] = paginator.get_page(page)
            return render_to_string(template_name=template, context=context, request=self.request)
        except Exception as e:
            print('get_lista_html_candidatos: ', e)
            return "<h1>Erro ao renderizar lista de candidatos !!</h1>"


    def get_formulario_html_candidatos(self, id_pleito):
        template = 'core/render/formulario_lancamento.html'
        context = {}
        try:
            context['pleito'] = Pleito.objects.get(id=id_pleito).nome
            context['candidatos'] = ModelCandidato.objects.order_by("ordem").filter(ativa=True, pleito=id_pleito)
            return render_to_string(template_name=template, context=context, request=self.request)
        except Exception as e:
            print('get_lista_html_lancamento_candidatos: ', e)
            return "<h1>Erro ao renderizar lista de candidatos !!</h1>"