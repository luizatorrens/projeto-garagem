from django.db import models
from garagem.models import Acessorio, Cor, Modelo
from uploader.models import Image

class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
        )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True, default=0)
    descricao = models.CharField(max_length=100)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    preco = models.DecimalField(max_digits=7, decimal_places=3, default=0, null=True, blank=True)
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
        # on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    def __str__(self):
        return f"{self.modelo}- {self.ano}"
    
    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"