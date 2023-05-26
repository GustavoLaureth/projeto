from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    numero = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    empenho = models.FileField(upload_to='empenhos/', max_length=500)
    nfe = models.FileField(upload_to='notas/', max_length=500, default='0', blank=True)
    n_nfe = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        self.empenho.delete()
        self.nfe.delete()
        super().delete(*args, **kwargs)