
def menu_principal ():
    print(f"|-----------------------------------------------|")
    print(f"|--               Menu Principal              --|")
    print(f"|-----------------------------------------------|")
    print(f"| [a] Soma de Elementos                         |")
    print(f"| [b] Números Ímpares de um Intervalo           |")
    print(f"| [c] Inserção Ordenada                         |")
    print(f"| [d] Contagem de Ocorrências                   |")
    print(f"| [e] Remoção de Duplicatas                     |")
    print(f"| [f] Estatísticas de uma Lista                 |")
    print(f"| [g] Inversão de Lista                         |")
    print(f"| [h] Interseção de Listas                      |")
    print(f"| [i] Índice dos Múltiplos de 3                 |")
    print(f"| [j] Classificação por Tamanho de Palavra      |")
    print(f"|-----------------------------------------------|")
    valor=input("| Informe a opção : ").lower()
    return (valor)

def funcao_a ():
    print (f"Eu sou so função A")
    

def funcao_principal ():
    opcao=menu_principal ()

    if opcao == "a":
        funcao_a ()
    else :
        print (f"[ERRO] Opcao inválida")


if __name__ == "__main__" :
    funcao_principal ()
         

