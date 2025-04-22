from django.contrib import admin
from .models import Hero, Noticia, Diretoria, Artigo, Agenda, GaleriaPresidentes

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('titulo_hero', 'descricao', 'link')
    search_fields = ('titulo_hero', 'descricao', 'link')
    list_filter = ['titulo_hero']
    list_per_page = 10

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo_noticia', 'autor', 'data_publicacao', 'tag')
    search_fields = ('titulo_noticia', 'autor', 'texto', 'tag')
    list_filter = ['titulo_noticia', 'autor', 'data_publicacao', 'tag']
    date_hierarchy = 'data_publicacao'
    list_per_page = 10


@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_diretoria', 'cargo', 'foto_diretoria')
    search_fields = ('nome_diretoria', 'cargo')
    list_filter = ['nome_diretoria']
    list_per_page = 10


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo_artigo', 'categoria', 'foto_artigo', 'credito_foto_artigo', 'autor_artigo', 'data_publicacao_artigo')
    search_fields = ('titulo_artigo', 'categoria', 'autor_artigo')
    list_filter = ['titulo_artigo', 'categoria']
    list_per_page = 10

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dia', 'mes', 'horario', 'local')
    search_fields = ('titulo', 'dia', 'mes', 'horario', 'local')
    list_filter = ['titulo', 'dia', 'mes']
    list_per_page = 10
    
@admin.register(GaleriaPresidentes)
class GaleriaPresidentesAdmin(admin.ModelAdmin):
    list_display = ('nome_presidente', 'periodo_presidencia')
    search_fields = ('nome_presidente', 'periodo_presidencia')
    list_filter = ['nome_presidente', 'periodo_presidencia']
    list_per_page = 10