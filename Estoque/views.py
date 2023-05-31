from django.db.models.signals import post_save

from Mercearia.models import Mercearia


def precoprodutos(nomeproduto):
    from Estoque.models import Arroz, Feijao, Refri
    if nomeproduto == "arroz":
        print(Arroz.objects.values_list("preco_arroz")[0][0])
        return Arroz.objects.values_list("preco_arroz")[0][0]
    elif nomeproduto == "feijao":
        print(Feijao.objects.values_list("preco_feijao")[0][0])
        return Feijao.objects.values_list("preco_feijao")[0][0]
    elif nomeproduto == "refri":
        print(Refri.objects.values_list("preco_refri")[0][0])
        return Refri.objects.values_list("preco_refri")[0][0]
    else:
        return 0


def calculopedidos(sender, created, **kwargs):
    from Estoque.models import Arroz, Feijao, Refri
    from Mercearia.models import Mercearia
    if created:
        ultimopedido = len(Mercearia.objects.all())
        quantidadepedido_arroz = Mercearia.objects.values_list("arroz")[ultimopedido][0]
        quantidadepedido_feijao = Mercearia.objects.values_list("feijao")[ultimopedido][0]
        quantidadepedido_refri = Mercearia.objects.values_list("refri")[ultimopedido][0]
        preco_arroz = Arroz.objects.values_list("preco_arroz")[0][0]
        preco_feijao = Feijao.objects.values_list("preco_feijao")[0][0]
        preco_refri = Refri.objects.values_list("preco_refri")[0][0]
        total = (quantidadepedido_arroz * preco_arroz) \
                + (quantidadepedido_feijao * preco_feijao) \
                + (quantidadepedido_refri * preco_refri)
        return Mercearia.objects.filter(total=0).update(total=total)
