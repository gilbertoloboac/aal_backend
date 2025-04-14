from rest_framework import serializers
from .models import Hero, Noticia, Diretoria, Artigo, Agenda

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'titulo_hero', 'descricao', 'link', 'imagem']


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo_noticia', 'autor', 'texto', 'foto_noticia', 'legenda_foto', 'credito_foto', 'olho', 'tag', 'data_publicacao']
        

class DiretoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretoria
        fields = ['id', 'nome_diretoria', 'cargo', 'foto_diretoria']


class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = ['id', 'titulo_artigo', 'categoria', 'foto_artigo', 'credito_foto_artigo', 'autor_artigo', 'data_publicacao_artigo', 'texto_artigo']


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'titulo', 'dia', 'mes', 'horario', 'local']