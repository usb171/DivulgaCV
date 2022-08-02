from ..models import Candidato as ModelCandidato, _PLEITO
from django.template.loader import render_to_string
from django.core.paginator import Paginator


class Candidato:


    def __init__(self, request):
        self.request = request


    def get_lista_html_candidatos(self):
        template = 'core/render/lista_candidatos_final.html'
        context = {}

        try:
            print(self.request.GET)
            page = self.request.GET.get('grupo')
            pleito = self.request.GET.get('pleito')
            paginator = Paginator(ModelCandidato.objects.order_by("-votos").filter(ativa=True, pleito=pleito), 4)
            context['candidatos'] = paginator.get_page(page)
            return render_to_string(template_name=template, context=context, request=self.request)
        except Exception as e:
            print('get_lista_html_candidatos: ', e)
            return "<h1>Erro ao renderizar lista de candidatos !!</h1>"


    def get_formulario_html_candidatos(self, pleito):
        template = 'core/render/formulario_lancamento.html'
        context = {}

        try:
            context['pleito'] = list(filter(lambda c: c[0] == str(pleito), _PLEITO))[0][1]
            context['candidatos'] = ModelCandidato.objects.order_by("ordem").filter(ativa=True, pleito=pleito)
            print(context)
            return render_to_string(template_name=template, context=context, request=self.request)
        except Exception as e:
            print('get_lista_html_lancamento_candidatos: ', e)
            return "<h1>Erro ao renderizar lista de candidatos !!</h1>"