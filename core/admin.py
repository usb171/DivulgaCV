from django.contrib import admin
from .models import Candidato, Partido, Pleito, Voto
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .ferramentas.funcoes import Lancamento 


class CandidatoAdmin(admin.ModelAdmin):
    list_display = [ 'nome', 'ativa', 'partido', 'pleito', 'votos', 'votos_porcentagem', 'ordem']
    list_filter = ['nome', 'partido']
    readonly_fields = ['votos_porcentagem']


class PartidoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    list_filter = ['nome', 'sigla']


class PleitoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'votos']
    list_filter = ['nome']

class VotoAdmin(admin.ModelAdmin):
    list_display = ['candidato', 'votos', 'pleito','update_at', 'created_at']
    list_filter = ['candidato', 'pleito']
    readonly_fields = ['votos', 'candidato', 'pleito']

    @receiver(post_delete, sender=Voto)
    def _voto_delete(sender, instance, **kwargs):
        print("Deletando Voto", instance)
        Lancamento(None).atualizarVotos()
        print('Deletado com sucesso!')


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Pleito, PleitoAdmin)
admin.site.register(Voto, VotoAdmin)

