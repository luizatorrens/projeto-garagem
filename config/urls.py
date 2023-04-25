from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, ModeloViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"marca", MarcaViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"acessorio", AcessorioViewSet)
router.register(r"modelo", ModeloViewSet)
router.register(r"veiculo", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]