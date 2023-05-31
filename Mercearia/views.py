from django.shortcuts import render
from django.http import HttpResponse
from .models import Mercearia


# Fazer puxar o preço dos produtos do Estoque.Views e fazer o cálculo de redução de produtos do estoque
def ver_preco(request):
    from Estoque.views import precoprodutos
    total = 0
    # Quando o usuário acessar o site
    if request.method == 'GET':
        # A função Render faz com que o site renderize um arquivo html e envie informações para o site

        return render(request, "ver_mercearia.html", {'valortotal': '0',
                                                      'preco_arroz': precoprodutos("arroz"),
                                                      'preco_feijao': precoprodutos("feijao"),
                                                      'preco_refri': precoprodutos("refri")})
    # Quando o usuário apertar o botão
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        endereço = request.POST.get('endereço')
        entrega = bool(request.POST.get('entrega'))
        arroz = int(request.POST.get('arroz'))
        feijao = int(request.POST.get('feijao'))
        refri = int(request.POST.get('refri'))
        total = (arroz * precoprodutos("arroz")) + \
                (feijao * precoprodutos("feijao")) + \
                (refri * precoprodutos("refri"))
        Loja = Mercearia(nome=nome,
                         entrega=entrega,
                         endereço=endereço,
                         arroz=arroz,
                         feijao=feijao,
                         refri=refri)
        Loja.save()
        total = "R$ " + str(total)
        return render(request, "ver_mercearia.html", {'valortotal': total,
                                                      'preco_arroz': precoprodutos("arroz"),
                                                      'preco_feijao': precoprodutos("feijao"),
                                                      'preco_refri': precoprodutos("refri")})
