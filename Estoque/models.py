from django.db import models
from Estoque.views import calculopedidos

class Arroz(models.Model):
    nome_arroz = models.CharField(default='Arroz', editable=False, max_length=255, verbose_name="Nome do produto")
    qtd_arroz = models.IntegerField(verbose_name="Quantidade em estoque:")
    preco_arroz = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Preco arroz:")

    class Meta:
        verbose_name_plural = 'Arroz'

    def __str__(self):
        return self.nome_arroz

class Feijao(models.Model):
    nome_feijao = models.CharField(max_length=20, default="Feijão", editable=False, verbose_name="Feijao")
    qtd_feijao = models.IntegerField(verbose_name="Quantidade em estoque:")
    preco_feijao = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Preco feijao:")

    class Meta:
        verbose_name_plural = 'Feijao'

    def __str__(self):
        return self.nome_feijao

class Refri(models.Model):
    nome_refri = models.CharField(max_length=20, default="Refri", editable=False, verbose_name="Refrigerante")
    qtd_refri = models.IntegerField(verbose_name="Quantidade em estoque:")
    preco_refri = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Preco refrigerante:")

    class Meta:
        verbose_name_plural = 'Refrigerante'

    def __str__(self):
        return self.nome_refri
# Atualizar um valor direto de um objeto já existente
# Arroz.objects.filter(nome_arroz="Arroz").update(preco_arroz=3.12)
# Receber um valor de dentro de um objeto específico
# print(Arroz.objects.values_list("preco_arroz")[0][0])
# Quantidade de objetos de Arroz existem
# print(len(Arroz.objects.values_list("nome_arroz")))
calculopedidos()