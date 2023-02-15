from django.contrib import admin
from .models import Categoria, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email', 'categoria']
    list_display_links = ['id']

admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)