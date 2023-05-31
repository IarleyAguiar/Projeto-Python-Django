from django.shortcuts import render
def precoprodutos(nomeproduto):
    from Estoque.models import Arroz, Feijao, Refri
    if nomeproduto == "arroz":
        return Arroz.objects.values_list("preco_arroz")[0][0]
    elif nomeproduto == "feijao":
        return Feijao.objects.values_list("preco_feijao")[0][0]
    else:
        return Refri.objects.values_list("preco_refri")[0][0]

def calculopedidos():
    from Estoque.models import Arroz, Feijao, Refri
    from Mercearia.models import Mercearia
    lenprod= 0
    if len(Mercearia.objects.values_list("id")) == 0:
        return lenprod
    else:
        lenprod= len(Mercearia.objects.values_list("id"))-1
    ultimopedido = Mercearia.objects.values_list("id")[lenprod][0]
    quantidadepedido_arroz = Mercearia.objects.filter(id=ultimopedido).values_list("arroz")[0][0]
    quantidadepedido_feijao = Mercearia.objects.filter(id=ultimopedido).values_list("feijao")[0][0]
    quantidadepedido_refri = Mercearia.objects.filter(id=ultimopedido).values_list("refri")[0][0]
    preco_arroz = Arroz.objects.values_list("preco_arroz")[0][0]
    preco_feijao = Feijao.objects.values_list("preco_feijao")[0][0]
    preco_refri = Refri.objects.values_list("preco_refri")[0][0]
    total = (quantidadepedido_arroz * preco_arroz) \
            + (quantidadepedido_feijao * preco_feijao) \
            + (quantidadepedido_refri * preco_refri)
    print(ultimopedido)
    return Mercearia.objects.filter(id=ultimopedido).update(total=total)