# Aula 02 - HTML5 e CSS (Introdução)
> 
> Nesta parte da ala realizaremos uma demonstração prática com uma estrutura HTML5 básica e explicações sobre comandos CSS essenciais. 
>
> Serão apresentados os comandos básicos de inserção de CSS, cores, bordas, formatação de fonte e tamanho. 
>
> Vamos combinar as referências citadas para construir um exemplo funcional.

---

## :one: **Modelo - Estrutura HTML5 Básica**  

:globe_with_meridians: **Modelo de página HTML**
```html

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Estrutura HTML5</title>
    <meta name="description" content="Uma página de exemplo para demonstrar a estrutura básica do HTML5.">
    <link rel="stylesheet" href="styles.css">
    <style> 
        /* CSS interno para exemplo  */
        /* Estilos serão adicionados aqui */
    </style>
</head>
<body>
    <!-- Elemento HEADER --> 
    <header>
        <h1>Título Principal do Site</h1>
    </header>

    <!-- Ememento MAIN - Área principal da página -->
    <main>

    </main>

    <!-- Elemento FOOTER - Roda-pé da página --> 
    <footer id="footer">
        <p>&copy; 2025 - Todos os direitos reservados.</p>
    </footer>
</body>
</html>

```

Adicionado algum conteúdo para testarmos o `CSS`

:globe_with_meridians: **Código HTML atualizado**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Estrutura HTML5</title>
    <meta name="description" content="Uma página de exemplo para demonstrar a estrutura básica do HTML5.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Elemento HEADER --> 
    <header>
        <h1>Título Principal do Site</h1>
    </header>

    <!-- Ememento MAIN - Área principal da página -->
    <main>
        <section id="section1">
            <h2>Aqui entra o conteúdo da página</h2>
            <p>Cada parágrafo na sua linha</p>
            <div class="caixa">Conteúdo formatado</div>
        </section>
    </main>

    <!-- Elemento FOOTER - Roda-pé da página --> 
    <footer id="footer">
        <p>&copy; 2025 - Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```
---

## :two: **Comandos Básicos do CSS**  

Vamos adicionar estilos ao exemplo acima, explicando propriedades essenciais:

### :bookmark:  **Inserção de CSS**  

As formas de inserção de conteúdo CSS em uma página são:

- **CSS interno**: Usamos a tag **`<style>`** no **`<head>`** (como no exemplo) .  
- **CSS inline**: `style="propriedade: valor;"` diretamente em tags HTML.  
- **CSS externo**: Arquivo `.css` vinculado via `<link href="estilos.css">` .

### :bookmark: **Cores**  


- **Propriedade `color`**: Define a cor do texto.  
  ```css
  h1 {
      color: #FF0000; /* Vermelho em hexadecimal  */
  }
  ```

  
- **Propriedade `background-color`**: Cor de fundo.  
  ```css
  body {
      background-color: lightblue; /* Nome da cor  */
  }
  ```

- **Referencia de Sites**

    - [SheCodes](https://www.shecodes.io/palettes)
    - [W3c Schools - CSS Colors](https://www.w3schools.com/cssref/css_colors.php)
    - [W3c Schools - Color Palettes](https://www.w3schools.com/colors/colors_palettes.asp)
    - [Ranoya - Registro de Cores](https://www.ranoya.com/books/public/css/corescss.php)
    - [Mozilla Developper - Color](https://developer.mozilla.org/pt-BR/docs/Web/CSS/color_value)
    - [Home Host - Tabela de cores HTML](https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/)


### :bookmark: **Formatação de Fonte**  

- **`font-family`**: Define a família tipográfica.  
  ```css
  p {
      font-family: Arial, sans-serif; /* Fonte com fallback  */
  }
  ```
  
  
- **`font-size`**: Tamanho da fonte (pixels, em, %).  
  ```css
  .caixa {
      font-size: 18px; /* Tamanho fixo em pixels */
  }
  ```
  
  
- **`font-weight`**: Espessura da fonte (`bold`, `normal`).  
  ```css
  h1 {
      font-weight: bold; /* Texto em negrito */
  }
  ```
 
 - **Referencia de Sites**

    - [CSS Text](https://www.w3schools.com/css/css_text.asp) 


### :bookmark: **Bordas**  

- **Propriedade `border`**: Define borda (largura, estilo, cor).  
  ```css
  .caixa {
      border: 2px solid #000; /* Borda preta de 2px  */
      padding: 10px; /* Espaçamento interno */
  }
  ```
  
  
 - **Referencia de Sites**

    - [CSS Borders](https://www.w3schools.com/css/css_border.asp) 
    - [CSS Margins](https://www.w3schools.com/css/css_margin.asp)
    - [CSS Padding](https://www.w3schools.com/css/css_padding.asp)

### :bookmark: **Exemplo Completo de CSS**  

```css

/* Estilos para o elemento body */
body {
    font-family: 'Arial', sans-serif; 
    line-height: 1.6; 
    margin: 0;
    padding: 20px;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2); 
    min-height: 100vh;
}

h1 {
    color: #333;
    font-size: 2.5em; /* Tamanho relativo  */
}

p {
    color: #666;
    font-size: 16px;
    line-height: 1.5; /* Espaçamento entre linhas */
}

.caixa {
    background-color: white;
    border: 3px dashed #007BFF; /* Borda tracejada azul */
    padding: 20px;
    margin: 15px 0; /* Margem externa */
    text-align: center; /* Alinhamento de texto */
}
```

---

### :bookmark: **Explicações Adicionais**  

- **Cascata**: O CSS segue uma hierarquia (inline > interno > externo) .  

- **Unidades de medida**: `px` (pixels), `%` (percentual), `em` (relativo ao pai) .  

- **Funções CSS**: Como `calc()` para cálculos dinâmicos (ex: `width: calc(100% - 20px);`) .  

---
