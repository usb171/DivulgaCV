from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('governador', Core.governador, name='governador'),
    path('senador', Core.senador, name='senador'),
    path('lancamento/governador', Core.lancamentoGovernador, name='lancamentoGovernador'),
    path('lancamento/senador', Core.lancamentoSenador, name='lancamentoSenador'),
    path('atualizar/lista', CoreAjax.atualizarLista, name='atualizar_lista'),
]