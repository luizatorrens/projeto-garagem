from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca, Categoria, Cor, Acessorio, Modelo, Veiculo
from garagem.serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer, ModeloSerializer, VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer




