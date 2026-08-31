# Aula 10 - Atividade 1
> Agora vamos praticar nossos conhecimento utilizando alguns códigos python

## Vetores e Matrizes com Listas em Python

## 1.1 Vetores

Um vetor pode ser representado como uma lista comum em Python:

```python 
# Criando um vetor (lista unidimensional)
vetor = [1, 2, 3, 4, 5]
print("Vetor:", vetor)
```

Podemos acessar elementos de um vetor usando índices:
```python 
print("Primeiro elemento:", vetor[0])  # Saída: 1
print("Último elemento:", vetor[-1])  # Saída: 5
```

## 1.2 Matrizes

Uma matriz pode ser representada como uma lista de listas:
```python 
# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Acessamos elementos usando dois índices:

```python 
print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8
```

Podemos percorrer matrizes com loops aninhados:

```python 
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
```

# Exercícios

## :one: Criando e Exibindo uma Matriz

:books: Peça ao usuário para inserir os valores de uma **matriz 4×4** e exiba a matriz formatada.

1. Utilizando `list comprehension`

```python
matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

for linha in matriz:
    print(linha)
```

2. Utilizando laço de repetição `for`

```python
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)
```

📌 **Explicação:**  
- Criamos uma matriz **4×4** e imprimimos cada linha.

## :two: Soma dos Elementos Acima da Diagonal Principal

:books: Receba uma **matriz 4×4** e calcule a **soma dos elementos acima da diagonal principal**.

```python
soma = sum(matriz[i][j] for i in range(4) for j in range(i+1, 4))
print(f"Soma dos elementos acima da diagonal principal: {soma}")
```

```python
soma = 0
for i in range(4):
    for j in range(i + 1, 4):
        soma += matriz[i][j]

print(f"Soma dos elementos acima da diagonal principal: {soma}")
```


📌 **Explicação:**  
- Somamos elementos com **índices coluna maiores que linha** (`j > i`).

## :three:  Soma dos Elementos da Diagonal Secundária

:books:  Receba uma **matriz 4×4** e calcule a **soma dos elementos da diagonal secundária**.

```python
soma = sum(matriz[i][3 - i] for i in range(4))
print(f"Soma da diagonal secundária: {soma}")
```

```python
soma = 0
for i in range(4):
    soma += matriz[i][3 - i]

print(f"Soma da diagonal secundária: {soma}")
```


📌 **Explicação:**  
- A diagonal secundária segue o padrão `matriz[i][3 - i]`.

## :four: Maior Valor de Cada Linha

:books: Solicite ao usuário uma **matriz 4×4** e exiba o **maior elemento de cada linha**.

```python
for i, linha in enumerate(matriz):
    print(f"Maior valor da linha {i}: {max(linha)}")
```

```python
for i in range(4):
    maior = matriz[i][0]
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(f"Maior valor da linha {i}: {maior}")
```


📌 **Explicação:**  
- `max(linha)` retorna o **maior valor** de cada linha.

## :five: Contagem de Números Pares

:books: Peça ao usuário para inserir uma **matriz 4×4** e exiba **quantos números pares** ela contém.

```python
pares = sum(1 for linha in matriz for num in linha if num % 2 == 0)
print(f"Quantidade de números pares: {pares}")
```

```python
pares = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares += 1

print(f"Quantidade de números pares: {pares}")
```


📌 **Explicação:**  
- **Percorremos toda a matriz** contando os valores pares.

## :six: Multiplicação de Linhas por um Número

:books: Receba uma **matriz 4×4** e um número inteiro. Multiplique **todos os elementos de uma linha específica** por esse número e exiba o resultado.

```python
num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

matriz[linha_escolhida] = [num * valor for valor in matriz[linha_escolhida]]

for linha in matriz:
    print(linha)
```

```python
num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

for j in range(4):
    matriz[linha_escolhida][j] *= num

for linha in matriz:
    print(linha)
```



📌 **Explicação:**  
- Multiplicamos **todos os elementos** de uma linha específica.

## :seven: Multiplicação de Matrizes

:books: Receba **duas matrizes 4×4** e calcule a **multiplicação matricial** entre elas.

```python
matriz2 = [[int(input(f"Digite o valor para matriz2[{i}][{j}]: ")) for j in range(4)] for i in range(4)]
produto = [[sum(matriz[i][k] * matriz2[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

for linha in produto:
    print(linha)
```

```python
matriz2 = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para matriz2[{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

produto = []
for i in range(4):
    linha = []
    for j in range(4):
        soma = 0
        for k in range(4):
            soma += matriz[i][k] * matriz2[k][j]
        linha.append(soma)
    produto.append(linha)

for linha in produto:
    print(linha)
```


📌 **Explicação:**  
- Aplicamos a **fórmula da multiplicação de matrizes** (`linha × coluna`).


## :eight: Verificação de Simetria

:books: Receba uma **matriz 4×4** e verifique se ela é **simétrica**, ou seja, se `matriz[i][j] == matriz[j][i]`.

```python
simetrica = all(matriz[i][j] == matriz[j][i] for i in range(4) for j in range(4))
print("A matriz é simétrica" if simetrica else "A matriz não é simétrica")
```

```python
simetrica = True
for i in range(4):
    for j in range(4):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")
```

📌 **Explicação:**  
- Se **todos os elementos** `matriz[i][j] == matriz[j][i]`, a matriz é **simétrica**.


## :nine: Normalização de uma Matriz

:books: Receba uma **matriz 4×4** e normalize seus valores dividindo cada elemento pelo **maior valor da matriz**.

```python
maior = max(max(linha) for linha in matriz)
matriz_normalizada = [[matriz[i][j] / maior for j in range(4)] for i in range(4)]

for linha in matriz_normalizada:
    print(linha)
```

```python
maior = matriz[0][0]
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

matriz_normalizada = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(matriz[i][j] / maior)
    matriz_normalizada.append(linha)

for linha in matriz_normalizada:
    print(linha)
```

📌 **Explicação:**  
- **Dividimos todos os elementos** pelo **maior número** da matriz.

## :ten: Busca de um Elemento na Matriz

:books: Peça ao usuário para inserir uma **matriz 4×4** e um número **X**. Informe se **X** está na matriz e sua posição.

```python
x = int(input("Digite o número a buscar: "))
posicoes = [(i, j) for i in range(4) for j in range(4) if matriz[i][j] == x]

if posicoes:
    print(f"O número {x} está na posição: {posicoes}")
else:
    print(f"O número {x} não está na matriz.")
```

```python
x = int(input("Digite o número a buscar: "))
posicoes = []

for i in range(4):
    for j in range(4):
        if matriz[i][j] == x:
            posicoes.append((i, j))

if posicoes:
    print(f"O número {x} está na posição: {posicoes}")
else:
    print(f"O número {x} não está na matriz.")
```

📌 **Explicação:**  
- Buscamos `x` e armazenamos sua posição `(i, j)`.  
- Se `x` não for encontrado, avisamos o usuário.