# Aula 10 - Atividade 1
> Agora vamos praticar nossos conhecimento utilizando alguns códigos baseados na biblioteca NumPy

## **Exercício :one:: Criar uma matriz 3x3 com valores aleatórios entre 0 e 10**

:rocket: Crie uma matriz 3x3 com valores aleatórios inteiros no intervalo de 0 a 10.

:snake: **Solução:**
```python
import numpy as np

matriz = np.random.randint(0, 11, size=(3, 3))
print(matriz)
```

:pushpin: **Explicação:**
- `np.random.randint(0, 11, size=(3, 3))` gera uma matriz 3x3 com valores inteiros aleatórios entre 0 e 10 (11 é exclusivo).

## **Exercício :two:: Somar duas matrizes**

:rocket: Crie duas matrizes 2x2 e calcule a soma delas.

:snake: **Solução:**
```python
import numpy as np

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
soma = matriz1 + matriz2
print(soma)
```

**Explicação:**
- A soma de matrizes é feita elemento a elemento. O operador `+` é sobrecarregado no `numpy` para realizar essa operação.

## **Exercício :three:: Multiplicar uma matriz por um escalar**

:rocket: Multiplique uma matriz 2x2 por um escalar (por exemplo, 2).

:snake: **Solução:**
```python
import numpy as np

matriz = np.array([[1, 2], [3, 4]])
resultado = 2 * matriz
print(resultado)
```

**Explicação:**
- A multiplicação por um escalar multiplica cada elemento da matriz pelo valor escalar.

## **Exercício :four:: Multiplicar duas matrizes**

:rocket: Multiplique duas matrizes 2x2.

:snake: **Solução:**
```python
import numpy as np

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
produto = np.dot(matriz1, matriz2)
print(produto)
```

**Explicação:**
- A multiplicação de matrizes é feita usando a função `np.dot`, que realiza o produto escalar entre as matrizes.

## **Exercício :five:: Calcular a média dos elementos de uma matriz**

:rocket: Calcule a média dos elementos de uma matriz 3x3.

:snake: **Solução:**
```python
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
media = np.mean(matriz)
print(media)
```

**Explicação:**
- A função `np.mean` calcula a média de todos os elementos da matriz.

## **Exercício :six:: Encontrar o valor máximo e mínimo de uma matriz**

:rocket: Encontre o valor máximo e mínimo de uma matriz 2x3.

:snake: **Solução:**
```python
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])
maximo = np.max(matriz)
minimo = np.min(matriz)
print("Máximo:", maximo)
print("Mínimo:", minimo)
```

**Explicação:**
- As funções `np.max` e `np.min` retornam o valor máximo e mínimo da matriz, respectivamente.

## Exercício :seven:: Encontrando o Maior Valor de Cada Linha

:rocket: Crie uma matriz `4×4` e exiba o **maior elemento de cada linha**.

:snake: **Solução:**
```python
maiores = np.max(matriz, axis=1)
print("Maior valor de cada linha:", maiores)
```

📌 **Explicação:**  
- `np.max(matriz, axis=1)` retorna o **maior elemento** de cada linha.

## **Exercício :eight:: Contagem de Números Pares**

:rocket: Crie uma matriz `4×4` e conte **quantos números pares** ela contém.

:snake: **Solução:**

```python
pares = np.count_nonzero(matriz % 2 == 0)
print(f"Quantidade de números pares: {pares}")
```

📌 **Explicação:**  
- `matriz % 2 == 0` cria uma matriz booleana onde **True indica números pares**.  
- `np.count_nonzero()` conta os **valores True**.

## Exercício :nine:: Multiplicação de uma Linha por um Número

:rocket: Crie uma matriz `4×4`, peça um número ao usuário e **multiplique uma linha específica** por esse número.

:snake: **Solução:**

```python
num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

matriz[linha_escolhida, :] *= num
print("Matriz após multiplicação:")
print(matriz)
```
📌 **Explicação:**  
- `matriz[linha_escolhida, :]` seleciona uma **linha específica** e a multiplica pelo número.

## Exercício :keycap_ten:: Multiplicação de Matrizes

:rocket: Crie **duas matrizes `4×4`** e calcule o **produto matricial** entre elas.

:snake: **Solução:**

```python
matriz2 = np.array([[int(input(f"Digite o valor para matriz2[{i}][{j}]: ")) for j in range(4)] for i in range(4)])

produto = np.dot(matriz, matriz2)
print("Matriz resultante da multiplicação:")
print(produto)
```

📌 **Explicação:**  

- `np.dot(matriz, matriz2)` faz **multiplicação matricial**.


## Exercício :closed_book::  Verificação de Matriz Simétrica

:rocket: Crie uma matriz `4×4` e verifique se ela é **simétrica**.

:snake: **Solução:**
```python
simetrica = np.array_equal(matriz, matriz.T)
print("A matriz é simétrica" if simetrica else "A matriz não é simétrica")
```

📌 **Explicação:**  

- `matriz.T` é a **transposta** da matriz. Se `matriz == matriz.T`, então é **simétrica**.


## Exercício :green_book::  Normalização de uma Matriz

:rocket: Crie uma matriz `4×4` e normalize seus valores dividindo cada elemento pelo **maior valor da matriz**.

:snake: **Solução:**

```python
maior = np.max(matriz)
matriz_normalizada = matriz / maior

print("Matriz normalizada:")
print(matriz_normalizada)
```

📌 **Explicação:**  

- **Dividimos cada elemento** pelo **maior valor da matriz**.

## Exercício :blue_book: Busca de um Elemento na Matriz

:rocket: Crie uma matriz `4×4` e peça um número ao usuário. Informe se **esse número está presente** na matriz e sua posição.

:snake: **Solução:**

```python
x = int(input("Digite o número a buscar: "))
posicoes = np.argwhere(matriz == x)

if posicoes.size > 0:
    print(f"O número {x} está nas posições: {posicoes}")
else:
    print(f"O número {x} não está na matriz.")
```

📌 **Explicação:**  

- `np.argwhere(matriz == x)` retorna **todas as posições onde `x` está presente**.
