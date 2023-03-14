from django.contrib import admin

from .models import Marca, Categoria

admin.site.register(Marca)
admin.site.register(Categoria)

def __str__(self):
    return self.descricao
