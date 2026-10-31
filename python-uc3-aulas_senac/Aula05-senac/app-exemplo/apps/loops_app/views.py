##
# APP: loops_app - views.py
##
import random
import string
from django.shortcuts import render

def teste():
    pass

def index (request):
    return render(request, 'loops_app/index.html')

def pagina_for(request):
    # 1. Iterando sobre listas e range no Python (Backend)
    frutas = ["Maçã", "Banana", "Cereja", "Morango"]
    
    # Recebe um número via GET (ex: ?numero=7) ou usa 5 como padrão
    numero = int(request.GET.get('numero', 5))
    
    tabuada = []
    for i in range(1, 11):
        tabuada.append({
            'multiplicador': i,
            'resultado': numero * i
        })

    contexto = {
        'frutas': frutas,
        'numero': numero,
        'tabuada': tabuada,
    }
    return render(request, 'loops_app/exemplo_for.html', contexto)

def jogo_adivinhacao(request):
    
    # Inicializa o segredo e contador na sessão do navegador
    if 'numero_secreto' not in request.session:
        request.session['numero_secreto'] = random.randint(1, 10)
        request.session['tentativas'] = 0

    mensagem = ""
    acertou = False

    if request.method == "POST":
        palpite = int(request.POST.get('palpite', 0))
        request.session['tentativas'] += 1
        segredo = request.session['numero_secreto']

        if palpite < segredo:
            mensagem = "O número secreto é maior!"
        elif palpite > segredo:
            mensagem = "O número secreto é menor!"
        else:
            mensagem = f"Parabéns! Você acertou em {request.session['tentativas']} tentativa(s)."
            acertou = True
            # Reinicia o jogo
            del request.session['numero_secreto']
            del request.session['tentativas']

    return render(request, 'loops_app/jogo.html', {'mensagem': mensagem, 'acertou': acertou})

def amortizacao_divida(request):
    tabela = []
    saldo = 0
    
    saldo = float(request.POST.get('valor_total', 0))
    parcela_mensal = float(request.POST.get('parcela', 0))
    mes = 1

    # O laço while continua até a dívida ser quitada
    while saldo > 0:
        if saldo < parcela_mensal:
            pago = saldo
            saldo = 0
        else:
            pago = parcela_mensal
            saldo -= parcela_mensal

        tabela.append({
            'mes': mes,
            'pago': round(pago, 2),
            'saldo_restante': round(saldo, 2)
        })
        mes += 1

    return render(request, 'loops_app/amortizacao.html', {'tabela': tabela})

def fatores_primos(request):
    fatores = []
    numero_original = None

    if request.method == "POST":
        numero = int(request.POST.get('numero', 1))
        numero_original = numero
        divisor = 2

        # Reduz o número dividindo pelos fatores primos possíveis
        while numero > 1:
            if numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            else:
                divisor += 1

    contexto = {
        'numero': numero_original,
        'fatores': fatores
    }

    return render(request, 'loops_app/fatores.html', contexto)

def consolidacao_pedidos(request):
    # Lista de pedidos
    pedidos = [
        {"produto": "Laptop", "preco": 3000, "quantidade": 1},
        {"produto": "Mouse", "preco": 50, "quantidade": 2},
        {"produto": "Teclado", "preco": 150, "quantidade": 1},
        {"produto": "Laptop", "preco": 3000, "quantidade": 1},
        {"produto": "Pendrive 128Gb SanDisk", "preco": 105, "quantidade": 5},
    ]
    
    # Cálculo do valor total
    valor_total = 0

    produtos_unico=[]

    for pedido in pedidos :
        #print(pedido)        
        subtotal=pedido["preco"] * pedido["quantidade"]
        pedido["subtotal"]=subtotal

        produto=pedido["produto"]
        if produto not in produtos_unico :
            produtos_unico.append(produto)

        # debug
        #print (pedido)  
        valor_total = valor_total + subtotal
    
    qt_unicos = len (produtos_unico)
    
    print (produtos_unico)
    print (f"Valor total: {valor_total}")

    contexto={
        'produtos': pedidos,
        'total': valor_total,
        'unicos': produtos_unico,
        'qt_unicos': qt_unicos,
    }
 
    return render (request, 'loops_app/pedidos_v1.html',contexto)