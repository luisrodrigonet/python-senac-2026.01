# Desafio 6

> 💡 O recrutador entregou uma lista de atividades para você executar, relacionadas às estruturas de repetições 🔁

## 1️⃣ Imprimir números

🔖 Elabore um código para imprimir os números de 1 a 10 usando for


```python 
for i in range(1, 11):
    print(i)
```


## 2️⃣ Imprimir os quadrados 

🔖 Elabore um código para imprimir o quadrado dos números de 1 a 10 usando for

:snake: **Código**
```python 
for i in range(1, 11):
    print(i ** 2)

```


## 3️⃣ Imprimir Números pares e impares

🔖 Elabore um código para imprimir todos os números pares e ímpares de 1 a 20 usando for

:snake: **Código**
```python 
for i in range(1, 21, 2):
    print(i)

```


## 4️⃣ Imprimir de 10 até 1

🔖 Elabore um código para  imprimir de 10 até 1 de forma decrescente, usando while

:snake: **Código**
```python 
i = 10
while i >= 1:
    print(i)
    i -= 1

```

## 5️⃣ Criar um programa que pergunta o nome

🔖 O código deve solicitar o nome do usuário até que ele digite "sair"


:snake: **Código**
```python 
while True:
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    print(f"Olá, {nome}!")

```

## 6️⃣ Imprimir a soma dos números

🔖 Elabora um código para  imprimir a soma dos números de 1 a 100 usando for


:snake: **Código**
```python 
soma = 0
for i in range(1, 101):
    soma += i
print(soma)

```

## 7️⃣ Calcular o fatorial de um número usando while

🔖 O programa deve obter um número e em seguida imprimir o valor do fatorial


:snake: **Código**
```python 
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
print(fatorial)

```

## 8️⃣ Soma de números positivos

🔖 Elabora um código para  imprimir a soma de números positivos até um número negativo ser digitado


:snake: **Código**
```python 
soma = 0
while True:
    numero = int(input("Digite um número (negativo para parar): "))
    if numero < 0:
        break
    soma += numero
print(f"Soma dos números positivos: {soma}")

```

## 9️⃣ Tabela de multiplicação de um número (de 1 a 10)

🔖 O programa deve obter um número e o programa deve imprimir a tabela de multiplicação do número lido (de 1 a 10)


:snake: **Código**
```python 
numero = int(input("Digite um número para mostrar a tabela de multiplicação: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

```

## 🔟 Senha correta e repetição até acertar

🔖 Elabore um código que solicite a senha do usuário, deve-se solicitar a senha até que o valor informando seja igual ao conteúdo da constante "SENHA"


:snake: **Código**
```python 
senha_correta = "python123"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")

```

## 🔢 Imprimir uma lista de nomes

🔖 Elabora um código para listar todos os nomes contidos em uma lista


:snake: **Código**
```python 
nomes = ['Ana', 'Carlos', 'Maria', 'João']
for nome in nomes:
    print(nome)

```

## 🔢 Imprimir uma sequência de números e seus cubos

🔖 Elabore um programa que leia um número, em seguida deve-se imprimir os cubos de 1 até o numero lido


:snake: **Código**
```python 
for i in range(1, 6):
    print(f"Número: {i}, Cubo: {i**3}")

```

## 🔢 Imprimir uma tabela de multiplicação (aninhando loops)

🔖 Elabore um código para imprimir a tabela de multiplicação dos números de 1 até 10


:snake: **Código**
```python 
for i in range(1, 11):  # Loop para a linha
    for j in range(1, 11):  # Loop para as colunas
        print(f"{i} x {j} = {i * j}", end="\t")  # Imprime o produto
    print()  # Pula para a próxima linha

```

## 🔢 Contando o número de dígitos em um número

🔖 Elabore um código para imprimir a quantidade de dígitos de um número


:snake: **Código**
```python 
numero = int(input("Digite um número: "))
contador = 0
while numero > 0:
    numero //= 10  # Remove o último dígito
    contador += 1
print(f"O número tem {contador} dígitos.")

```

## 🔢 Imprimir os números de 1 a 20 e verificar se são múltiplos de 3 ou 5.

🔖 Para cada número de 1 a 20, imprima se o número é múltiplo de 3, de 5 ou de ambos.


:snake: **Código**
```python 
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} é múltiplo de 3 e 5")
    elif i % 3 == 0:
        print(f"{i} é múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} é múltiplo de 5")

```

## 🔢 Criar um programa que imprima uma tabela de multiplicação de 1 a 5 (sem usar o range).

🔖 Imprima a tabuada do 1 até o 5, sem utilizar a função range().


:snake: **Código**
```python 
for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5]:
        print(f"{i} x {j} = {i * j}")

```

## 🔢 Criar um programa que peça ao usuário para digitar uma sequência de números até que ele digite um número maior que 100.

🔖 O programa deve contar quantos números foram digitados antes do número maior que 100 ser inserido.


:snake: **Código**
```python 
contador = 0
while True:
    numero = int(input("Digite um número: "))
    if numero > 100:
        break
    contador += 1
print(f"Foram digitados {contador} números antes de um valor maior que 100.")

```

## 🔢 Imprimir o somatório de todos os números pares de 1 a 100.

🔖 Crie um programa que calcule a soma dos números pares entre 1 e 100.


:snake: **Código**
```python 
soma = 0
for i in range(2, 101, 2):
    soma += i
print(f"A soma dos números pares de 1 a 100 é {soma}.")

```

## 🔢 Contagem regressiva

🔖 Faça um programa que conte de 10 até 1 usando um `for`.


:snake: **Código**
```python 
for i in range(10, 0, -1):
   print(i)
```

## 🔢 Soma de números: 

🔖 Use um `while` para somar números até que o usuário digite 0.


:snake: **Código**
```python 
soma = 0
while True:
   numero = int(input("Digite um número (0 para sair): "))
   if numero == 0:
       break
   soma += numero
print(f"Soma total: {soma}")
```

## 🔢 Tabuada

🔖 Peça um número ao usuário e mostre a tabuada de 1 a 10 usando um `for`.


:snake: **Código**
```python 
numero = int(input("Digite um número: "))
for i in range(1, 11):
   print(f"{numero} x {i} = {numero * i}")
```

## 🔢 Números pares

🔖 Use um `for` para imprimir todos os números pares de 1 a 20.


:snake: **Código**
```python 
for i in range(2, 21, 2):
   print(i)
```

## 🔢 Adivinhe o número

🔖 Crie um jogo onde o usuário tenta adivinhar um número secreto (use `while` e `break`).


:snake: **Código**
```python 
import random
numero_secreto = random.randint(1, 10)
while True:
   palpite = int(input("Adivinhe o número (1 a 10): "))
   if palpite == numero_secreto:
       print("Parabéns! Você acertou!")
       break
   else:
       print("Tente novamente!")
```

## 🔢 Fatorial: 

🔖 Calcule o fatorial de um número usando um `for`.


:snake: **Código**
```python 
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
   fatorial *= i
print(f"Fatorial de {numero} é {fatorial}")
```

## 🔢 Lista de compras

🔖 Use um `for` para percorrer uma lista de compras e imprimir cada item.


:snake: **Código**
```python 
compras = ["maçã", "banana", "leite", "pão"]
for item in compras:
   print(item)
```

## 🔢 Números primos

🔖 Verifique se um número é primo usando um `for` e `break`.


:snake: **Código**
```python 
numero = int(input("Digite um número: "))
primo = True
for i in range(2, numero):
   if numero % i == 0:
       primo = False
       break
print("É primo!" if primo else "Não é primo!")
```

## 🔢 Sequência de Fibonacci

🔖 Gere os primeiros 10 números da sequência de Fibonacci usando um `while`.


:snake: **Código**
```python 
a, b = 0, 1
contador = 0
while contador < 10:
   print(a)
   a, b = b, a + b
   contador += 1
```

## 🔢 Menu interativo

🔖 Crie um menu que repete até o usuário escolher "sair" (use `while`).

:snake: **Código**
```python
while True:
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "3":
        print("Saindo...")
        break
    else:
        print(f"Você escolheu a opção {opcao}")
```

