# Aula 8 - Atividade 1
> Exercícios envolvendo funções simples

A seguir, temos  lista com 10 exercícios sobre funções. Cada exercício tem um grau de complexidade que varia de simples a média, ideal para praticar e fixar os conceitos:

## Exercício 1: Função saudacao

### Objetivo: Imprimir uma mensagem de boas-vindas.

### Passos:
1. Definir a função saudacao sem parâmetros.
2. Dentro da função, usar o print para exibir a mensagem.
3. Chamar a função para ver o resultado

### Código:

```python 
def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")
    
# Chamando a função
saudacao()
```

## Exercício 2: Função soma

###  Objetivo: Somar dois números e retornar o resultado.

### Passos:
1. Definir a função soma com dois parâmetros: a e b.
2. Calcular a soma dos parâmetros.
3. Retornar o resultado usando return.
4. Chamar a função e imprimir o resultado.

### Código:
```python 
def soma(a, b):
    return a + b
# Exemplo de chamada
resultado = soma(5, 7)
print("A soma é:", resultado)
```

## Exercício 3: Função par_ou_impar

### Objetivo: Verificar se um número é par ou ímpar.

### Passos:
1. Definir a função par_ou_impar com um parâmetro n.
2. Usar a operação de módulo (%) para verificar se n é divisível por 2.
3. Retornar a string "Par" se for divisível ou "Ímpar" caso contrário.
4. Chamar a função e exibir o resultado.

### Código:

```python 
def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
# Exemplo de chamada
print("O número 4 é", par_ou_impar(4))
print("O número 7 é", par_ou_impar(7))
```

##  Exercício 4: Função fatorial

### Objetivo: Calcular o fatorial de um número inteiro não negativo.

### Passos:
1. Definir a função fatorial com o parâmetro n.
2. Tratar o caso em que n seja negativo (opcional: retornar mensagem de erro).
3. Se n for 0, retornar 1 (pois 0! = 1).
4. Para n > 0, inicializar uma variável resultado com 1.
5. Usar um laço for de 1 até n e multiplicar resultado pelo índice.
6. Retornar resultado.


### Código:

```python 
def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
# Exemplo de chamada
print("Fatorial de 5:", fatorial(5))
```

## Exercício 5: Função maior_elemento

### Objetivo: Retornar o maior elemento de uma lista.

### Passos:
1. Definir a função maior_elemento que receba uma lista.
2. Utilizar a função interna max() para encontrar o maior valor.
3. Retornar o maior elemento.
4. Chamar a função com uma lista de números.


### Código:

```python 
def maior_elemento(lista):
    return max(lista)
# Exemplo de chamada
numeros = [3, 8, 1, 20, 7]
print("O maior elemento é:", maior_elemento(numeros))
```

## Exercício 6: Função media

### Objetivo: Calcular a média aritmética dos elementos de uma lista.

### Passos:

1. Definir a função media que receba uma lista de números.
2. Calcular a soma dos elementos com sum().
3. Dividir pela quantidade de elementos usando len().
4. Retornar o resultado.
5. Chamar a função e exibir a média.

### Código:

```python 
def media(lista):
    return sum(lista) / len(lista)
# Exemplo de chamada
valores = [10, 20, 30, 40]
print("A média é:", media(valores))
```

## Exercício 7: Função eh_palindromo

### Objetivo: Verificar se uma palavra é um palíndromo.

### Passos:
1. Definir a função eh_palindromo que receba uma string.
2. Comparar a string com sua versão invertida (utilizando slicing [::-1]).
3. Retornar True se for igual ou False caso contrário.
4. Testar a função com exemplos.

### Código:

```python 
def eh_palindromo(palavra):
    return palavra == palavra[::-1]
# Exemplos de chamada
print("ana é palíndromo?", eh_palindromo("ana"))
print("python é palíndromo?", eh_palindromo("python"))
```

## Exercício 8: Função contar_vogais

### Objetivo: Contar o número de vogais em uma string.

### Passos:

1. Definir a função contar_vogais que receba um texto.
2. Criar uma string com todas as vogais ("aeiouAEIOU").
3. Inicializar um contador.
4. Percorrer cada caractere do texto e, se for uma vogal, incrementar o contador.
5. Retornar o contador.
6. Testar a função.

### Código:

```python 
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
# Exemplo de chamada
print("Número de vogais em 'Python':", contar_vogais("Python"))
```

## Exercício 9: Função tabuada

### Objetivo: Retornar uma lista com a tabuada de um número (de 1 a 10).

### Passos:

1. Definir a função tabuada que receba um número n.
2. Criar uma lista para armazenar os resultados.
3. Usar um laço for de 1 a 10 e, a cada iteração, calcular n * i e adicionar à lista.
4. Retornar a lista.
5. Exibir a tabuada chamando a função.

### Código:

```python 
def tabuada(n):
    resultado = []
    for i in range(1, 11):
        resultado.append(n * i)
    return resultado
# Exemplo de chamada
print("Tabuada do 5:", tabuada(5))
```

## Exercício 10: Função ordenar_por_segundo

### Objetivo: Ordenar uma lista de tuplas com base no segundo elemento de cada tupla.

### Passos:
1. Definir a função ordenar_por_segundo que receba uma lista de tuplas.
2. Utilizar a função sorted() com o parâmetro key definido como uma função lambda que retorna o segundo elemento de cada tupla.
3. Retornar a lista ordenada.
4. Testar a função com um exemplo.

### Código:

```python 
def ordenar_por_segundo(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])
# Exemplo de chamada
lista_exemplo = [("a", 3), ("b", 1), ("c", 2)]
print("Lista ordenada:", ordenar_por_segundo(lista_exemplo))
```

