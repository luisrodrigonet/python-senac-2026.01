# Aula 8 - Atividade 1
> Exercícios envolvendo a função main ()

## :one: Crie um programa Python que receba um nome como argumento da linha de comando e imprima "Olá, [nome]!"

### :snake: Código

```python
import sys

def main():
   nome = sys.argv[1]
   print(f"Olá, {nome}!")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py João`

## :two: Escreva um programa Python que receba dois números como argumentos da linha de comando e imprima a soma deles.

### :snake: Código

```python
import sys

def main():
   num1 = float(sys.argv[1])
   num2 = float(sys.argv[2])
   print(f"Soma: {num1 + num2}")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py 5 10`


## :three: Desenvolva um programa Python que receba uma lista de números como argumentos da linha de comando e calcule a média desses números

### :snake: Código

```python
import sys

def main():
   numeros = [float(arg) for arg in sys.argv[1:]]
   media = sum(numeros) / len(numeros)
   print(f"Média: {media}")

if __name__ == "__main__":
   main()
```

## :four: Crie um programa Python que receba uma string como argumento da linha de comando e conte quantas vogais existem nessa string

### :snake: Código

```python
import sys

def contar_vogais(texto):
   vogais = "aeiouAEIOU"
   return sum(1 for char in texto if char in vogais)

def main():
   texto = sys.argv[1]
   print(f"Vogais: {contar_vogais(texto)}")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py "Olá, mundo!"`

## :five: Escreva um programa Python que receba um número como argumento da linha de comando e verifique se ele é par ou ímpar.

### :snake: Código 

```python
import sys

def main():
   num = int(sys.argv[1])
   if num % 2 == 0:
       print(f"{num} é par.")
   else:
       print(f"{num} é ímpar.")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py 7`


##  :six: Desenvolva um programa Python que receba um arquivo de texto como argumento da linha de comando e conte quantas linhas existem nesse arquivo.

### :snake: Código

```python
import sys

def main():
   arquivo = sys.argv[1]
   with open(arquivo, 'r') as f:
       linhas = f.readlines()
   print(f"O arquivo tem {len(linhas)} linhas.")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py arquivo.txt`

## :seven: Crie um programa Python que receba dois números como argumentos da linha de comando e imprima o maior deles.

### :snake: Código

```python
import sys

def main():
   num1 = float(sys.argv[1])
   num2 = float(sys.argv[2])
   print(f"Maior número: {max(num1, num2)}")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py 15 10`

## :eight: Escreva um programa Python que receba uma palavra como argumento da linha de comando e verifique se ela é um palíndromo.

### :snake: Código

```python
import sys

def eh_palindromo(palavra):
   return palavra == palavra[::-1]

def main():
   palavra = sys.argv[1]
   if eh_palindromo(palavra):
       print(f"{palavra} é um palíndromo.")
   else:
       print(f"{palavra} não é um palíndromo.")

if __name__ == "__main__":
   main()
```
- Uso: `python programa.py arara`

## :nine: Desenvolva um programa Python que receba um número como argumento da linha de comando e calcule o fatorial desse número.

### :snake: Código

```python
import sys

def fatorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n * fatorial(n - 1)

def main():
   num = int(sys.argv[1])
   print(f"Fatorial de {num}: {fatorial(num)}")

if __name__ == "__main__":
   main()
```

- Uso: `python programa.py 5`

## :keycap_ten: Crie um programa Python que receba uma lista de palavras como argumentos da linha de comando e imprima a palavra mais longa.

### :snake: Código

```python
import sys

def main():
    palavras = sys.argv[1:]
    mais_longa = max(palavras, key=len)
    print(f"Palavra mais longa: {mais_longa}")

if __name__ == "__main__":
    main()
```

- Uso: `python programa.py Python é incrível`

