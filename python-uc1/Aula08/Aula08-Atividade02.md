# Aula 8 - Atividade 1
> Exercícios envolvendo a função main ()

## :one: Modifique o seguinte código para usar a função `main()` corretamente:

```python
def saudacao():
   print("Bem-vindo ao Python!")

saudacao()
```

### :snake: Código

```python
def main():
   print("Olá, mundo!")

if __name__ == "__main__":
   main()
```

## :two: Crie um programa Python que use a função `main()` para calcular e imprimir a soma de dois números fornecidos pelo usuário.

### :snake: Código

```python 
def main():
   num1 = float(input("Digite o primeiro número: "))
   num2 = float(input("Digite o segundo número: "))
   soma = num1 + num2
   print(f"A soma é: {soma}")

if __name__ == "__main__":
   main()
```

## :three: Escreva um programa Python que use a função `main()` para chamar outras funções, como `soma()` e `subtracao()`, e exiba os resultados.


### :snake: Código

```python
def soma(a, b):
   return a + b

def subtracao(a, b):
   return a - b

def main():
   resultado_soma = soma(10, 5)
   resultado_subtracao = subtracao(10, 5)
   print(f"Soma: {resultado_soma}")
   print(f"Subtração: {resultado_subtracao}")

if __name__ == "__main__":
   main()
```

## :four: Crie um programa Python que use a função `main()` para imprimir os números de 1 a 10.

### :snake: Código
```python
def main():
   for i in range(1, 11):
       print(i)

if __name__ == "__main__":
   main()
```

## :five: Escreva um programa Python que use a função `main()` para calcular o fatorial de um número fornecido pelo usuário.

### :snake: Código 

```python
def fatorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n * fatorial(n - 1)

def main():
   num = int(input("Digite um número: "))
   print(f"O fatorial de {num} é {fatorial(num)}")

if __name__ == "__main__":
   main()
```

##  :six: Desenvolva um programa Python que use a função `main()` para verificar se um número é primo ou não.

### :snake: Código

```python
def eh_primo(n):
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True

def main():
   num = int(input("Digite um número: "))
   if eh_primo(num):
       print(f"{num} é primo.")
   else:
       print(f"{num} não é primo.")

if __name__ == "__main__":
   main()
```

## :seven: Crie um programa Python que use a função `main()` para ordenar uma lista de números fornecida pelo usuário.

### :snake: Código

```python
def main():
   numeros = input("Digite uma lista de números separados por espaço: ").split()
   numeros = [int(num) for num in numeros]
   numeros.sort()
   print(f"Lista ordenada: {numeros}")

if __name__ == "__main__":
   main()
```

## :eight: Escreva um programa Python que use a função `main()` para contar quantas vogais existem em uma string fornecida pelo usuário

### :snake: Código

```python
def contar_vogais(texto):
   vogais = "aeiouAEIOU"
   return sum(1 for char in texto if char in vogais)

def main():
   texto = input("Digite uma string: ")
   print(f"A string contém {contar_vogais(texto)} vogais.")

if __name__ == "__main__":
   main()
```


## :nine: Desenvolva um programa Python que use a função `main()` para calcular a média de uma lista de números.

### :snake: Código

```python
def calcular_media(lista):
   return sum(lista) / len(lista)

def main():
   numeros = input("Digite uma lista de números separados por espaço: ").split()
   numeros = [float(num) for num in numeros]
   print(f"A média é: {calcular_media(numeros)}")

if __name__ == "__main__":
   main()
```

## :keycap_ten: Crie um programa Python que use a função `main()` para inverter uma string fornecida pelo usuário.

### :snake: Código

```python
def inverter_string(texto):
   return texto[::-1]

def main():
   texto = input("Digite uma string: ")
   print(f"String invertida: {inverter_string(texto)}")

if __name__ == "__main__":
   main()
```

## :abcd:  Escreva um programa Python que use a função `main()` para encontrar o maior número em uma lista.

### :snake: Código

```python
def encontrar_maior(lista):
   return max(lista)

def main():
   numeros = input("Digite uma lista de números separados por espaço: ").split()
   numeros = [int(num) for num in numeros]
   print(f"O maior número é: {encontrar_maior(numeros)}")

if __name__ == "__main__":
   main()
```


## :capital_abcd: Desenvolva um programa Python que use a função `main()` para gerar a sequência de Fibonacci até um número fornecido pelo usuário.

### :snake: Código

```python
def fibonacci(n):
   sequencia = []
   a, b = 0, 1
   while a <= n:
       sequencia.append(a)
       a, b = b, a + b
   return sequencia

def main():
   num = int(input("Digite um número: "))
   print(f"Sequência de Fibonacci até {num}: {fibonacci(num)}")

if __name__ == "__main__":
   main()
```


## :abc: Crie um programa Python que use a função `main()` para converter uma temperatura de Celsius para Fahrenheit.

### :snake: Código

```python
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def main():
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F")

    if __name__ == "__main__":
        main()
    ```