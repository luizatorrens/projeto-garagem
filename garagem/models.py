from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nome.upper()
    
class Modelo(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    
class Categoria(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural= "Acessórios"

class Cor(models.Model):
    descricao= models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural= "Cores"

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    preco = models.DecimalField(max_digits=7, decimal_places=3, default=0, null=True, blank=True)
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}"
    class Meta:
        verbose_name_plural= "Veículos"