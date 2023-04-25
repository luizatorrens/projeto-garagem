from rest_framework.serializers import ModelSerializer

from garagem.models import Marca, Categoria, Cor, Acessorio

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"