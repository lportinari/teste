from django.contrib import admin

from . models import Produto


# Registrando o modelo Produto na página administrativa
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')

