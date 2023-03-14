from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()

class Categoria(models.Model):
    descricao= models.CharField(max_length=100)

    def __str__(self):
        return self.descricao