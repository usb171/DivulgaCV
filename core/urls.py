from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('apuracao/<int:id_pleito>', Core.apuracao, name='apuracao'),
    path('lancamento/<int:id_pleito>', Core.lancamento, name='lancamento'),
    path('atualizar/lista', CoreAjax.atualizarLista, name='atualizar_lista'),
]