
    for p in pedidos:
        subtotal = p["preco"] * p["quantidade"]
        p["total"]=subtotal
        valor_total = valor_total + subtotal
    
    # Contagem de itens únicos
    #produtos_unicos = set(p["produto"] for p in pedidos)

    produtos_unicos = []
    for p in pedidos:
        produto = p["produto"]
        if produto not in produtos_unicos:
            produtos_unicos.append(produto)

            
    
    quantidade_unicos = len(produtos_unicos)    
    
    # Contexto para o template
    context = {
        'pedidos': pedidos,
        'valor_total': valor_total,
        'quantidade_unicos': quantidade_unicos,
        'produtos_unicos': list(produtos_unicos)
    }
    
    #return render(request, 'loops_app/pedidos.html', context)
    #return render(request, 'loops_app/pedidos_template.html', context)

----------/\--------

