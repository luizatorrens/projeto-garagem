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

class Acessorio(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=3, default=0, null=True, blank=True)
    modelo = models.CharField(max_length=30, null=False, default=0)
    def __str__(self):
        return f"modelo: {self.modelo}, marca: {self.marca}, ano: {self.ano}, cor: {self.cor}"