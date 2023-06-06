from django.shortcuts import render
from django.http import HttpResponse
from .models import Mercearia


# Fazer puxar o preço dos produtos do Estoque.Views e fazer o cálculo de redução de produtos do estoque
def ver_preco(request):
    from Estoque.views import precoprodutos
    from Estoque.models import Arroz, Feijao, Refri
    total = 0
    # Quando o usuário acessar o site
    if request.method == 'GET':
        # A função Render faz com que o site renderize um arquivo html e envie informações para o site

        return render(request, "index.html", {'preco_arroz': precoprodutos("arroz"),
                                              'preco_feijao': precoprodutos("feijao"),
                                              'preco_refri': precoprodutos("refri"),
                                              'qtd_arroz': Arroz.objects.values_list("qtd_arroz")[0][0],
                                              'qtd_feijao': Feijao.objects.values_list("qtd_feijao")[0][0],
                                              'qtd_refri': Refri.objects.values_list("qtd_refri")[0][0]})
    # Quando o usuário apertar o botão
    elif request.method == 'POST':
        arroz = int(request.POST.get('Quantidade_Arroz'))
        feijao = int(request.POST.get('Quantidade_Feijao'))
        refri = int(request.POST.get('Quantidade_Refri'))
        total = (arroz * precoprodutos("arroz")) + \
                (feijao * precoprodutos("feijao")) + \
                (refri * precoprodutos("refri"))
        total = total
        if request.POST.get('nome') is not None:
            Loja = Mercearia(nome=request.POST.get('nome'),
                             endereço=request.POST.get('endereço'),
                             preco_arroz=precoprodutos("arroz"),
                             arroz=request.POST.get('Quantidade_Arroz'),
                             preco_feijao=precoprodutos("feijao"),
                             feijao=request.POST.get('Quantidade_Feijao'),
                             preco_refri=precoprodutos("refri"),
                             refri=request.POST.get('Quantidade_Refri'),
                             total=total)
            Loja.save()
        return render(request, "compra.html", {'valortotal': total,
                                               'arroz': arroz,
                                               'feijao': feijao,
                                               'refri': refri})


def compras(request):
    if request == 'GET':
        return render(request, "compra.html", 0)


