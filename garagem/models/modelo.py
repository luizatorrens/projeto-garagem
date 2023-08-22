from django.db import models


from garagem.models import Marca
from garagem.models import Categoria


class Modelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculo"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculo"
    )
    
    def __str__(self):
        return f"{self.nome} "

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
