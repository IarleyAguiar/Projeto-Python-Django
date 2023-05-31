from django.db import models
from django.db.models.signals import post_save


class Mercearia(models.Model):
    nome = models.CharField(max_length=255)
    endereço = models.CharField(max_length=255, blank=True, null=True)
    preco_arroz = models.DecimalField(max_digits=6, decimal_places=2, default=0,
                                      verbose_name="Preco Arroz")
    arroz = models.IntegerField(default=0, null=True)
    preco_feijao = models.DecimalField(max_digits=6, decimal_places=2, default=0,
                                       verbose_name="Preco Feijão")
    feijao = models.IntegerField(default=0, null=True)
    preco_refri = models.DecimalField(max_digits=6, decimal_places=2, default=0,
                                      verbose_name="Preco Refrigerante")
    refri = models.IntegerField(default=0, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.nome


