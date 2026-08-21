# Aula 09 - Atividade 2

### :one: Cadastro de produtos

:books: **Exercício:**  
Crie um programa que recebe o nome e o preço de **5 produtos**, armazene-os em uma **tupla** e exiba uma listagem formatada.

:snake: **Solução:**

```python
produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
for nome, preco in produtos:
    print(f"{nome:.<20} R$ {preco:.2f}")
```

:pushpin: **Explicação:**  
- Criamos uma **tupla de tuplas**, onde cada item contém um produto e seu preço.
- O `for` percorre a tupla e exibe os valores formatados.

---

### :two: Média de notas

:books: **Exercício:**  
Receba **4 notas** de um aluno, armazene-as em uma **tupla** e exiba a **média** das notas.

:snake: **Solução:**
```python
notas = (7.5, 8.0, 6.5, 9.0)
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")
```

:pushpin: **Explicação:** 

- A função `sum()` soma os valores da tupla.  
- `len()` retorna o número de elementos.  
- A média é calculada e formatada com `2` casas decimais.

---

### :three: Verificação de números primos

:books: **Exercício:**  
Crie uma **tupla** com **10 números inteiros** e exiba apenas os **números primos**.

:snake: **Solução:**
```python
numeros = (2, 7, 10, 13, 17, 22, 29, 31, 40, 53)

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = tuple(num for num in numeros if eh_primo(num))
print(f"Números primos: {primos}")
```

:pushpin: **Explicação:**  

- Criamos a função `eh_primo(n)` para verificar se um número é primo.  
- Utilizamos uma **compreensão de tupla** para filtrar os primos.  

---

### :four: Classificação de idade

:books:**Exercício:**  
Peça ao usuário **5 idades** e exiba quantas pessoas são **maiores de idade**.

:snake: **Solução:**
```python
idades = (18, 25, 16, 30, 14)
maiores = sum(1 for idade in idades if idade >= 18)
print(f"Quantidade de maiores de idade: {maiores}")
```

:pushpin: **Explicação:**  

- A **compreensão de tupla** soma `1` para cada idade maior ou igual a `18`.

---

### :five: Palavras com vogais

:books:**Exercício:**  

Crie uma **tupla** com palavras e exiba suas **vogais**.

:snake: **Solução:**

```python
palavras = ("python", "programação", "desenvolvimento", "computador")

for palavra in palavras:
    vogais = "".join(letra for letra in palavra if letra in "aeiou")
    print(f"Vogais de {palavra}: {vogais}")
```

:pushpin: **Explicação:**  

- Para cada palavra, criamos uma string apenas com as vogais.

---

### :six: Números por extenso

:books:**Exercício:**  

Receba um número de **0 a 9** e exiba-o **por extenso**.

:snake: **Solução:**

```python
extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

num = int(input("Digite um número (0-9): "))
if 0 <= num <= 9:
    print(f"Você digitou: {extenso[num]}")
else:
    print("Número inválido.")
```
:pushpin: **Explicação:**

- Criamos uma **tupla de strings** contendo os números por extenso.  
- O índice da tupla representa o número digitado.  

---

### :seven: Maior e menor valor

:books:**Exercício:**  
Gere uma **tupla** com **10 números aleatórios** e exiba o **maior** e o **menor**.

:snake: **Solução:**

```python
import random
numeros = tuple(random.randint(1, 100) for _ in range(10))
print(f"Números: {numeros}")
print(f"Maior: {max(numeros)}, Menor: {min(numeros)}")
```
:pushpin: **Explicação:**  

- Usamos `random.randint(1, 100)` para gerar números aleatórios.  
- `max()` e `min()` encontram os valores extremos.  

---

### :eight: Frequência de elementos

:books:**Exercício:**  
Peça ao usuário **5 números** e verifique quantas vezes um número escolhido aparece.

:snake: **Solução:**

```python
numeros = (3, 7, 2, 3, 9)
n = int(input("Digite um número para verificar: "))
print(f"O número {n} aparece {numeros.count(n)} vezes.")
```

:pushpin: **Explicação:**  

- O método `.count(n)` retorna quantas vezes `n` aparece na tupla.

---

### :nine: Ordenação sem modificar a tupla

:books:**Exercício:**  
Ordene uma **tupla** sem modificar seu conteúdo original.

:snake:**Solução:**

```python
numeros = (10, 3, 7, 1, 9)
ordenados = tuple(sorted(numeros))
print(f"Tupla original: {numeros}")
print(f"Tupla ordenada: {ordenados}")
```
:pushpin: **Explicação:**  
- `sorted(numeros)` cria uma **lista ordenada**, que é convertida novamente em **tupla**.

---

### :keycap_ten: Jogo de dados

:books:**Exercício:**  
Simule o lançamento de um **dado** 5 vezes e exiba quantas vezes cada número foi sorteado.

:snake: **Solução:**

```python
import random

lancamentos = tuple(random.randint(1, 6) for _ in range(5))
print(f"Resultados: {lancamentos}")

for num in range(1, 7):
    print(f"{num} saiu {lancamentos.count(num)} vezes.")
```

:pushpin: **Explicação:** 

- Criamos uma tupla com **5 lançamentos aleatórios** de um dado.  
- Contamos quantas vezes cada número de `1 a 6` apareceu.  