# Aula 09 - Atividade 1
> Agora vamos praticar os nossos conhecimentos com algumas atividades envolvendo listas

## :books: Exemplo :one:: Criando e imprimindo uma lista

Criando um vetor (lista) com números inteiros

```python
vetor = [10, 20, 30, 40, 50]
print("Vetor:", vetor)
```

## :books: Exemplo :two:: Iterando sobre uma lista

Iterando e imprimindo cada elemento do vetor
```python
for elemento in vetor:
    print("Elemento:", elemento)
```

## :books: Exemplo :three:: Utilizando NumPy para operações com vetores

```python 
import numpy as np
# Criando um array (vetor) utilizando a biblioteca NumPy
vetor_np = np.array([1, 2, 3, 4, 5])
print("Vetor com NumPy:", vetor_np)
```

## :books: Exercício :five:: Calcular a soma dos elementos de um vetor

:scroll: Explicação:
1. Passo 1: Definimos a lista com os números.
2. Passo 2: A função sum() retorna a soma de todos os elementos da lista.
3. Passo 3: Imprimimos a soma obtida.


```python 
# Passo 1: Definir o vetor.
vetor = [10, 20, 30, 40, 50]
# Passo 2: Calcular a soma utilizando a função sum().
soma = sum(vetor)
# Passo 3: Imprimir o resultado.
print("Soma dos elementos:", soma)
```

## :books: Exercício :six:: Encontrar o maior e o menor valor em um vetor

:scroll:  Explicação:
1. Passo 1: Criamos o vetor com alguns números.
2. Passo 2: max(vetor) retorna o maior número e min(vetor) o menor.
3. Passo 3: Exibimos os valores encontrados.

```python 
# Passo 1: Definir o vetor.
vetor = [3, 7, 2, 9, 4]
# Passo 2: Utilizar as funções max() e min() para encontrar os valores.
maior = max(vetor)
menor = min(vetor)
# Passo 3: Imprimir os resultados.
print("Maior valor:", maior)
print("Menor valor:", menor)
```

## :books: Exercício :seven:: Inverter a ordem dos elementos de um vetor sem usar reverse()

:scroll: Explicação:
1. Passo 1: Definimos um vetor simples.
2. Passo 2: O slicing [::-1] cria uma nova lista com os elementos na ordem inversa.
3. Passo 3: Imprimimos o resultado.

```python 
# Passo 1: Definir o vetor.
vetor = [1, 2, 3, 4, 5]
# Passo 2: Inverter o vetor utilizando slicing.
vetor_invertido = vetor[::-1]
# Passo 3: Imprimir o vetor invertido.
print("Vetor invertido:", vetor_invertido)
```

## :books: Exercício :eight:: Multiplicar cada elemento do vetor por 2 e armazenar em um novo vetor

:scroll: Explicação:
1. Passo 1: Criamos o vetor original.
2. Passo 2: Definimos o valor pelo qual cada elemento será multiplicado.
3. Passo 3: Usamos list comprehension para criar uma nova lista, multiplicando cada elemento.
4. Passo 4: Exibimos o novo vetor.

```python
# Passo 1: Definir o vetor original.
vetor = [1, 2, 3, 4, 5]
# Passo 2: Definir o multiplicador.
multiplicador = 2
# Passo 3: Utilizar list comprehension para multiplicar cada elemento.
vetor_mult = [elemento * multiplicador for elemento in vetor]
# Passo 4: Imprimir o novo vetor.
print("Vetor multiplicado:", vetor_mult)
```

## :books: Exercício :nine:: Contar quantas vezes o valor 3 aparece em um vetor

:scroll: Explicação:
1. Passo 1: Definimos o vetor com alguns elementos repetidos.
2. Passo 2: O método count() retorna quantas vezes o valor 3 aparece na lista.
3. Passo 3: Imprimimos a contagem.

```python
# Passo 1: Definir o vetor.
vetor = [1, 3, 3, 4, 3, 5]
# Passo 2: Utilizar o método count() para contar o valor 3.
ocorrencias = vetor.count(3)
# Passo 3: Imprimir o resultado.
print("O valor 3 aparece", ocorrencias, "vezes.")
```

## :books: Exercício :keycap_ten:: Ordenar um vetor em ordem crescente

:scroll: Explicação:
1. Passo 1: Criamos o vetor desordenado.
2. Passo 2: A função sorted() retorna uma nova lista com os elementos em ordem crescente.
3. Passo 3: Exibimos a lista ordenada.

```python
# Passo 1: Definir o vetor.
vetor = [5, 2, 9, 1, 5, 6]
# Passo 2: Utilizar a função sorted() para ordenar a lista.
vetor_ordenado = sorted(vetor)
# Passo 3: Imprimir o vetor ordenado.
print("Vetor ordenado:", vetor_ordenado)
```

## :books: Exercício :capital_abcd:: Remover elementos duplicados do vetor

:scroll: Explicação:
1. Passo 1: Definimos um vetor que contém elementos repetidos.
2. Passo 2: Ao converter a lista para um dicionário com dict.fromkeys(vetor), eliminamos as duplicatas, pois as chaves de um dicionário são únicas. Em seguida, convertemos de volta para lista.
3. Passo 3: Imprimimos o vetor sem os valores duplicados.

```python 
# Passo 1: Definir o vetor com duplicatas.
vetor = [1, 2, 2, 3, 4, 4, 5]
# Passo 2: Remover duplicatas utilizando dict.fromkeys() para preservar a ordem.
vetor_sem_duplicatas = list(dict.fromkeys(vetor))
# Passo 3: Imprimir o vetor resultante.
print("Vetor sem duplicatas:", vetor_sem_duplicatas)
```

## :books: Exercício :abcd:: Separar os elementos pares e ímpares em duas listas

:scroll: Explicação:
1. Passo 1: Criamos um vetor com números de 1 a 10.
2. Passo 2: A list comprehension [num for num in vetor if num % 2 == 0] seleciona os números pares.
3. Passo 3: Similarmente, [num for num in vetor if num % 2 != 0] seleciona os números ímpares.
4. Passo 4: Imprimimos as duas listas resultantes.

```python 
# Passo 1: Definir o vetor original.
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Passo 2: Utilizar list comprehension para separar os pares.
pares = [num for num in vetor if num % 2 == 0]
# Passo 3: Utilizar list comprehension para separar os ímpares.
impares = [num for num in vetor if num % 2 != 0]
# Passo 4: Imprimir os dois vetores.
print("Pares:", pares)
print("Ímpares:", impares)
```

## :books: Exercício :abc:: Calcular a média e exibir elementos acima da média

:scroll: Explicação:
1. Passo 1: Definimos o vetor com números simples.
2. Passo 2: Calculamos a média dividindo a soma dos elementos pelo número total de elementos (len(vetor)).
3. Passo 3: Selecionamos os números que são maiores que a média utilizando list comprehension.
4. Passo 4: Imprimimos a média calculada e a lista dos elementos acima dela.

```Python 
# Passo 1: Definir o vetor.
vetor = [1, 2, 3, 4, 5]
# Passo 2: Calcular a média dos elementos.
media = sum(vetor) / len(vetor)
# Passo 3: Utilizar list comprehension para selecionar elementos acima da média.
acima_media = [num for num in vetor if num > media]
# Passo 4: Imprimir a média e os elementos que estão acima dela.
print("Média:", media)
print("Elementos acima da média:", acima_media)
```


