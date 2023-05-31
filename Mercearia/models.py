from django.db import models




class Mercearia(models.Model):
    nome = models.CharField(max_length=255)
    entrega = models.BooleanField(default=False)
    endereço = models.CharField(max_length=255, blank=True, default='Se não for entrega, ignore essa caixa')
    arroz = models.IntegerField(default=0, null=True)
    feijao = models.IntegerField(default=0, null=True)
    refri = models.IntegerField(default=0, null=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.nome
