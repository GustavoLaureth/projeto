from django.contrib import admin
from .models import Categoria, Empresa, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'nome', 'cnpj', 'categoria', 'empresa', 'empenho', 'valor', 'email']
    list_display_links = ['id']

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)