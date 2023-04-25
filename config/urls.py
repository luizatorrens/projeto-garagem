from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet

router = DefaultRouter()
router.register(r"marca", MarcaViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"cor", CorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]