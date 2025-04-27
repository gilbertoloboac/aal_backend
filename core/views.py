from rest_framework import viewsets
from .models import (
    Hero,
    Noticia,
    Diretoria,
    Artigo,
    Agenda,
    GaleriaPresidentes,
    Membro,
    Documento,
    Revista,
)
from .serializers import (
    HeroSerializer,
    NoticiaSerializer,
    DiretoriaSerializer,
    ArtigoSerializer,
    AgendaSerializer,
    GaleriaPresidentesSerializer,
    MembroSerializer,
    DocumentoSerializer,
    RevistaSerializer,
)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class DiretoriaViewSet(viewsets.ModelViewSet):
    queryset = Diretoria.objects.all()
    serializer_class = DiretoriaSerializer


class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class GaleriaPresidentesViewSet(viewsets.ModelViewSet):
    queryset = GaleriaPresidentes.objects.all()
    serializer_class = GaleriaPresidentesSerializer


class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by("-criado_em")
    serializer_class = DocumentoSerializer


class RevistaViewSet(viewsets.ModelViewSet):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer
