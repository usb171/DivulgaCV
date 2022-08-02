from django.contrib import admin
from .models import Candidato, Partido


class CandidatoAdmin(admin.ModelAdmin):
    list_display = [ 'nome', 'ativa', 'pleito', 'votos', 'votos_porcentagem', 'ordem']
    list_filter = ['nome', 'pleito']
    readonly_fields = ['votos_porcentagem']


class PartidoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    list_filter = ['nome', 'sigla']


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Partido, PartidoAdmin)