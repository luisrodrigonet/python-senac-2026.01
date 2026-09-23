# Aula 05 - Parte 05 - JavaScript
> **Objetivos da Aula**  
> - Demonstrar o uso básico do `alert()` para exibir mensagens.  
> - Introduzir eventos de input em JavaScript.  
> - Explicar os métodos `parseInt()` e `parseFloat()`.  
> - Enfatizar que esses métodos podem retornar strings em certos casos.  
>
> ---
> 

## :one: **Introdução ao `alert()`**  
O `alert()` é uma função nativa do **JavaScript** que exibe uma mensagem em uma caixa de diálogo no navegador.  

### **Exemplo Prático:**  
```javascript
alert("Python UC02 - Desenvolvimento Web");
```

**Explicação:**  
- Quando o código é executado, uma caixa de diálogo aparece com a mensagem.  
- Útil para feedback rápido, mas não deve ser usado excessivamente em aplicações reais.  

---

## :two: **Capturando Inputs do Usuário**  

Elementos HTML como `<input>` permitem que o usuário insira dados. No JavaScript, esses valores são **sempre strings**, mesmo que o usuário digite números.    

### :computer: **Exemplo:**  
```html
<input type="text" id="entradaUsuario" placeholder="Digite algo">
<button onclick="capturarInput()">Enviar</button>

<script>
  function capturarInput() {
    const valor = document.getElementById("entradaUsuario").value;
     alert("Valor digitado: " + valor + " | Tipo: " + typeof valor);
  }
</script>
```

**Explicação:**  
- O botão chama a função `capturarInput()` quando clicado.  
- O valor digitado no campo de **input** é capturado e exibido em um `alert()`.  

---

## :three: **Convertendo Strings em Números: `parseInt()` e `parseFloat()`**  

Para realizar cálculos, precisamos converter strings em números. Dois métodos essenciais são:  

| Método       | Descrição                           |  
|--------------|-----------------------------------|  
| `parseInt()` | Converte uma string em **número inteiro**. |  
| `parseFloat()`| Converte uma string em **número decimal**. |  

### :computer: **Exemplo 1**  
```html
<input type="text" id="numeroInteiro" placeholder="Digite um número inteiro">
<input type="text" id="numeroDecimal" placeholder="Digite um número decimal">
<button onclick="converterNumeros()">Converter</button>

<script>
  function converterNumeros() {
    const inteiro = parseInt(document.getElementById("numeroInteiro").value);
    const decimal = parseFloat(document.getElementById("numeroDecimal").value);

    alert(`Inteiro: ${inteiro}, Decimal: ${decimal}`);
  }
</script>
```

### :computer: **Exemplo 2**  
```html
<input type="text" id="numero" placeholder="Digite um número">
<button onclick="calcular()">Calcular</button>

<script>
  function calcular() {
    const input = document.getElementById("numero").value;
    const numero = parseFloat(input); // Converte a string para número

    if (isNaN(numero)) { // Verifica se a conversão falhou
      alert("Isso não é um número válido!");
    } else {
      alert("O dobro é: " + (numero * 2));
    }
  }
</script>
```  


**Observações Importantes:**  
1. **Retorno como String:**  
   - Se o valor não for numérico, `parseInt()` e `parseFloat()` retornam `NaN` (Not a Number), que é um tipo especial, mas ainda assim **não é uma string**.  
   - Exemplo:  
     ```javascript
     console.log(parseInt("abc")); // NaN (não é uma string, mas um valor especial)
     ```  

2. **Comportamento de Conversão:**  
   - `parseInt("10.5")` retorna `10` (ignora a parte decimal).  
   - `parseFloat("10.5")` retorna `10.5`.  

3. **Alternativas Modernas:**  
   - Usar `Number()` ou o operador `+` para conversão:  
     ```javascript
     const num = +"123"; // 123 (número)
     ```  

---

## :four: **Erro Comum: Esquecer a Conversão**  
Valores de input são strings, e operações matemáticas **não convertem automaticamente**.  

### :computer: **Exemplo:**  
```javascript
const valor1 = document.getElementById("numero1").value; // "5"
const valor2 = document.getElementById("numero2").value; // "3"

const somaErrada = valor1 + valor2; // Resultado: "53" (concatenação)
const somaCorreta = parseInt(valor1) + parseInt(valor2); // Resultado: 8
```  

**Por Que Isso Acontece?**  
- O operador `+` concatena strings, mas soma números.  


## :five: **Exercício Prático**  

Crie um programa que peça dois números ao usuário, calcule a soma e exiba o resultado. 

### :computer: **Solução:**  
```html
<input type="text" id="num1" placeholder="Número inteiro">
<input type="text" id="num2" placeholder="Número decimal">
<button onclick="somarNumeros()">Somar</button>

<script>
  function somarNumeros() {
    const num1 = parseInt(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
      alert("Digite números válidos!");
    } else {
      const soma = num1 + num2;
      alert(`Resultado: ${soma}`);
    }
  }
</script>
```

**Destaque:**  
- `isNaN()` verifica se o valor **não é um número**.  
- Sempre valide entradas antes de converter!  

---

## **Conclusão**  
- `alert()` é útil para mensagens simples.  
- Eventos de input capturam interações do usuário.  
- `parseInt()` e `parseFloat()` convertem strings em números, mas podem retornar `NaN` se a conversão falhar.  
- Sempre valide entradas para evitar erros.  


