from django.db import models
from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo
from uploader.models import Image

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    preco = models.DecimalField(max_digits=7, decimal_places=3, default=0, null=True, blank=True)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}"
    class Meta:
        verbose_name_plural= "Veículos"
