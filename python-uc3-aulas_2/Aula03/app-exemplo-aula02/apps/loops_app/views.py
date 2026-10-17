import random
from django.shortcuts import render

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