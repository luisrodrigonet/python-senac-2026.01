# Aula 07 - Atividade 01

## **1. Teste de Mesa (Desk Testing)**
**O que é?**  
É uma técnica para simular a execução de um programa **passo a passo**, como se você fosse o computador! Você anota os valores das variáveis e verifica a lógica do código manualmente.  

**Para que serve?**  
- Encontrar erros de lógica.  
- Entender como o código funciona internamente.  
- Treinar a capacidade de "pensar como a máquina".

:snake: **Exemplo Prático:**  
```python
x = 5
y = 0
while x > 0:
    y += x
    x -= 1
print(y)
```

:turtle: **Teste de mesa passo a passo:**

| Passo | x  | y  | Condição `x > 0`? |
|-------|----|----|-------------------|
| 1     | 5  | 0  | Sim               |
| 2     | 4  | 5  | Sim               |
| 3     | 3  | 9  | Sim               |
| 4     | 2  | 12 | Sim               |
| 5     | 1  | 14 | Sim               |
| 6     | 0  | 15 | Não → Sai do loop |

:star: **Resultado final:** `15` (soma de 5+4+3+2+1).

---

## **2. Pensamento Computacional**

**O que é?**  
É uma abordagem para resolver problemas usando técnicas como:  
1. **Decomposição**: Dividir o problema em partes menores.  
2. **Reconhecimento de padrões**: Identificar similaridades.  
3. **Abstração**: Focar no que é essencial.  
4. **Algoritmos**: Criar uma sequência lógica de passos.

**Exemplo:**  
*Problema:* Organizar uma lista de números em ordem crescente.  
- **Decomposição**: Separar números, comparar pares, trocar posições.  
- **Padrão**: Repetir comparações até não haver mais trocas.  
- **Abstração**: Ignorar números já ordenados.  
- **Algoritmo**: Implementar o método *Bubble Sort*.

---

# Exemplo: Fatorial 

## **Enunciado:**  
Escreva um algoritmo que solicite um número inteiro positivo **N** e calcule seu **fatorial**. O fatorial de um número é definido como:  

> N! = N x (N-1) x (N-2) x ... x 1

Por exemplo, **5! = 5 × 4 × 3 × 2 × 1 = 120**.

## **Portugol:**

```text
algoritmo Fatorial
var
    num, fatorial, i: inteiro
inicio
    escreva("Digite um número: ")
    leia(num)
    fatorial ← 1
    para i de 1 ate num faca
        fatorial ← fatorial * i
    fimpara
    escreva("O fatorial é: ", fatorial)
fim_algoritmo
```

## **Python:**

```python
num = int(input("Digite um número: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print("O fatorial é:", fatorial)
```

#### **Teste de Mesa:**

| Entrada | Iteração (i) | Operação            | Acumulado |
|---------|-------------|----------------------|-----------|
| 5       | 1           | 1 × 1                | 1         |
|         | 2           | 1 × 2                | 2         |
|         | 3           | 2 × 3                | 6         |
|         | 4           | 6 × 4                | 24        |
|         | 5           | 24 × 5               | 120       |
| **Saída** | - | - | **O fatorial é: 120** |


---

# Exercícios 

## **Exercício 1 (Baixa Complexidade): Soma de Dois Números**  
**Enunciado:**  
Elabore um algoritmo que leia dois números inteiros e exiba a soma deles.  

## **Exercício 2 (Baixa Complexidade): Verificar Par ou Ímpar**  

**Enunciado:**  
Leia um número e exiba se ele é par ou ímpar.  

## **Exercício 3 (Média Complexidade): Maior Número em uma Lista**  
**Enunciado:**  
Dada uma lista de 5 números, encontre e exiba o maior valor.  

## **Exercício 4 (Alta Complexidade): Ordenação por Bubble Sort**  
**Enunciado:**  
Implemente o algoritmo Bubble Sort para ordenar uma lista de 5 números em ordem crescente.  

## **Exercício 5 (Média Complexidade): Cálculo de Fatorial**  
**Enunciado:**  
Escreva um algoritmo que calcule o fatorial de um número inteiro não negativo fornecido pelo usuário.  

## **Exercício 6 (Média Complexidade): Sequência de Fibonacci**  
**Enunciado:**  
Implemente um algoritmo que gere os primeiros 10 termos da sequência de Fibonacci.  

## **Exercício 7 (Média Complexidade): Verificação de Número Primo**  
**Enunciado:**  
Crie um algoritmo que verifique se um número é primo.  


## **Exercício 8 (Média Complexidade): Reversão de String**  
**Enunciado:**  
Implemente um algoritmo que inverta uma string fornecida pelo usuário.  


## **Exercício 9 (Alta Complexidade): Média Aritmética com Exclusão**  
**Enunciado:**  
Elabore um algoritmo que calcule a média aritmética de 5 notas, excluindo a menor nota.  


## **Exercício 10 (Alta Complexidade): Fibonacci Recursivo**  
**Enunciado:**  
Implemente a sequência de Fibonacci usando recursão. Exiba o 8º termo da sequência.  

---

# Exercícios Extras 

## Simples:  

1. **Calculadora básica**: Soma, subtração, multiplicação e divisão de dois números.  
2. **Conversor de temperatura**: Celsius para Fahrenheit.  
3. **Média aritmética**: Calcular a média de três notas.  
4. **Verificação de par/ímpar**: Determinar se um número é par ou ímpar.  

## **Média Complexidade**:  

5. **Fatorial**: Calcular o fatorial de um número usando loop.  
6. **Soma de números pares**: Somar todos os pares em um intervalo definido.  
7. **Palíndromo**: Verificar se uma palavra é palíndromo (ex: "ovo").  
8. **Primos**: Identificar números primos em uma lista.  

## **Avançado**:  

9. **Ordenação de lista**: Ordenar uma lista de números usando bubble sort.  
10. **Simulador de caixa eletrônico**: Gerenciar saque e saldo.  
