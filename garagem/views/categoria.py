from rest_framework.viewsets import ModelViewSet
from garagem.models import Categoria
from garagem.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
