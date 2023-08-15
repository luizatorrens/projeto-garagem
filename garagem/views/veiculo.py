from rest_framework.viewsets import ModelViewSet
from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo
from garagem.serializers import ModeloSerializer, MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer, VeiculoDetailSerializer, VeiculoListSerializer, VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer