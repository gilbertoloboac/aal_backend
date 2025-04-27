from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GaleriaPresidentesViewSet, HeroViewSet, NoticiaViewSet, DiretoriaViewSet, ArtigoViewSet, AgendaViewSet, MembroViewSet, RevistaViewSet, DocumentoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'hero', HeroViewSet)
router.register(r'noticia', NoticiaViewSet)
router.register(r'diretoria', DiretoriaViewSet)
router.register(r'artigo', ArtigoViewSet)
router.register(r'agenda', AgendaViewSet)
router.register(r'galeria_presidentes', GaleriaPresidentesViewSet)
router.register(r'membro', MembroViewSet )
router.register(r'revistas', RevistaViewSet)
router.register(r'documento', DocumentoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
