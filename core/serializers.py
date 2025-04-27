from rest_framework import serializers
from .models import Hero, Noticia, Diretoria, Artigo, Agenda, GaleriaPresidentes, Membro, Documento, Revista
from django.utils.html import linebreaks

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'titulo_hero', 'descricao', 'link', 'imagem']
    
    def get_conteudo_formatado(self, obj):
        return linebreaks(obj.conteudo)


class NoticiaSerializer(serializers.ModelSerializer):
    texto_formatado = serializers.SerializerMethodField()

    class Meta:
        model = Noticia
        fields = [
            'id',
            'titulo_noticia',
            'autor',
            'texto',
            'foto_noticia',
            'legenda_foto',
            'credito_foto',
            'olho',
            'tag',
            'data_publicacao',
            'texto_formatado',  # esse campo precisa estar aqui
        ]

    def get_texto_formatado(self, obj):
        return linebreaks(obj.texto)
        

class DiretoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretoria
        fields = ['id', 'nome_diretoria', 'cargo', 'foto_diretoria']


class ArtigoSerializer(serializers.ModelSerializer):
    texto_formatado = serializers.SerializerMethodField()

    class Meta:
        model = Artigo
        fields = [
            'id', 'titulo_artigo', 'categoria', 'foto_artigo',
            'credito_foto_artigo', 'autor_artigo',
            'data_publicacao_artigo', 'texto_artigo',
            'texto_formatado'  # campo novo
        ]

    def get_texto_formatado(self, obj):
        return linebreaks(obj.texto_artigo)


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'titulo', 'dia', 'mes', 'horario', 'local']
        
        
        
class GaleriaPresidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaleriaPresidentes
        fields = ['id', 'foto_presidente', 'nome_presidente', 'ordem_presidencia', 'periodo_presidencia']
        
        
class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = ['id', 'nome_membro', 'fotografia', 'biografia']
        

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ['id', 'titulo', 'arquivo', 'criado_em']
        

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revista
        fields = ['id', 'titulo', 'descricao', 'arquivo_pdf', 'criado_em']