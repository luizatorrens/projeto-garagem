from rest_framework.viewsets import ModelViewSet
from garagem.models import Acessorio
from garagem.serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
