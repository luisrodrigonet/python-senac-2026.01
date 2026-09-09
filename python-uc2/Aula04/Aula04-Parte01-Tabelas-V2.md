# Aula 04 - Parte 01 - Tabelas
>  Tabelas em HTML5 e Estilização com CSS
>  As tabelas são estruturas para organizar dados de **forma tabular** (linhas e colunas).
>
>  Em HTML5, são criadas usando as tags `<table>`, `<tr>`, `<th>`, `<td>`, e tags semânticas como `<thead>`, `<tbody>`, `<tfoot>`.
> 
> ---

## :one: **Estrutura Básica:**
```html
<table>
  <!-- Head da Tabela -->   
  <thead>
    <!-- Linha -->       
    <tr>
      <th>Produto</th>
      <th>Preço</th>
    </tr>
  </thead>
  <!-- Corpo da tabela --> 
  <tbody>
	<!-- Linha -->     
    <tr>        
      <td>Tênis A</td>
      <td>R$ 299,90</td>
    </tr>
  </tbody>
</table>
```

## :two: **Mesclagem de Células:**
- **`colspan`**: Mescla células horizontalmente.
- **`rowspan`**: Mescla células verticalmente.

**Exemplo:**
```html
<tr>
  <td colspan="2">Promoção Relâmpago</td>
</tr>
<tr>
  <td rowspan="2">Tênis B</td>
  <td>R$ 399,90</td>
</tr>
<tr>
  <td>Desconto: 10%</td>
</tr>
```

---

## :three: **Propriedades Avançadas de Tabelas**
- **`<caption>`**: Adiciona um título à tabela.
- **`scope` em `<th>`**: Define se o cabeçalho é para coluna (`col`) ou linha (`row`).
- **Atributos de Acessibilidade**: `aria-label`, `role="table"`.

**Exemplo Semântico:**
```html
<table aria-label="Tabela de Preços de Tênis">
  <caption>Preços da Loja de Tênis</caption>
  <thead>
    <tr>
      <th scope="col">Modelo</th>
      <th scope="col">Preço</th>
    </tr>
  </thead>
</table>
```

---

## :four: **Estilização de Tabelas com CSS**

### 📚 **Propriedades Principais:**
- **`border-collapse`**: Une bordas adjacentes (`collapse` ou `separate`).
- **`text-align` e `vertical-align`**: Alinhamento de conteúdo.
- **`nth-child()`**: Estilizar linhas alternadas.

🔖  **Exemplo de CSS:**
```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #eaeaea;
}
```

---

## :five: **Caso de Uso**

###  **Tabela de Preços de Loja de Tênis**

🌐 **HTML:**
```html
<div class="table-container">
  <table>
    <caption>Catálogo de Tênis - Preços 2023</caption>
    <thead>
      <tr>
        <th scope="col">Modelo</th>
        <th scope="col">Marca</th>
        <th scope="col">Preço Original</th>
        <th scope="col">Preço com Desconto</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Runner X</td>
        <td>Nike</td>
        <td>R$ 599,90</td>
        <td rowspan="2">R$ 499,90 (Combo)</td>
      </tr>
      <tr>
        <td>Air Max</td>
        <td>Nike</td>
        <td>R$ 799,90</td>
      </tr>
      <tr>
        <td>UltraBoost</td>
        <td>Adidas</td>
        <td colspan="2">Promoção Esgotada</td>
      </tr>
    </tbody>
  </table>
</div>
```

🕸️  **CSS Personalizado:**
```css
table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

caption {
  font-size: 1.5em;
  font-weight: bold;
  margin: 10px 0;
  color: #333;
}

th {
  background-color: #2c3e50;
  color: white;
  padding: 15px;
}

td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

tr:hover {
  background-color: #f0f8ff;
}

td[colspan="2"] {
  text-align: center;
  font-style: italic;
  color: #e74c3c;
}

/* Estilo para promoção combo */
tr:nth-child(2) td {
  background-color: #ecf0f1;
}
```

✨ **Boas Práticas**
1. Use `<th>` para cabeçalhos e `scope` para acessibilidade.
2. Evite tabelas para layouts (use CSS Grid/Flexbox).
3. Sempre teste a responsividade.

🎁 **Recursos Adicionais:**
- MDN Web Docs: [HTML Tables](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/table)
- W3Schools: [CSS Styling Tables](https://www.w3schools.com/css/css_table.asp)


###  **Tabela de Preços Responsiva com Bootstrap**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tabela de Tênis com Bootstrap 5</title>
    <!-- Bootstrap 5.3 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .img-tenis {
            width: 100px;
            height: auto;
            object-fit: cover;
            border-radius: 5px;
        }
    </style>
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="mb-4 text-center">Catálogo de Tênis Esportivos</h1>
        
        <div class="table-responsive-lg">
            <table class="table table-striped table-hover align-middle shadow">
                <thead class="table-dark">
                    <tr>
                        <th scope="col" style="width: 15%">Foto</th>
                        <th scope="col" style="width: 55%">Descrição</th>
                        <th scope="col" style="width: 30%">Valor</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Item 1 -->
                    <tr>
                        <td>
                            <img src="https://via.placeholder.com/100x100.png?text=Nike+Air" 
                                 class="img-thumbnail img-tenis" 
                                 alt="Nike Air Force">
                        </td>
                        <td>
                            <h5 class="mb-1">Nike Air Force 1 '07</h5>
                            <ul class="list-unstyled">
                                <li><small>Cor: Branco</small></li>
                                <li><small>Material: Couro premium</small></li>
                                <li><span class="badge bg-success">Disponível</span></li>
                            </ul>
                        </td>
                        <td>
                            <span class="text-success fw-bold">R$ 899,90</span>
                            <del class="text-muted d-block">R$ 1.099,90</del>
                        </td>
                    </tr>

                    <!-- Item 2 -->
                    <tr>
                        <td>
                            <img src="https://via.placeholder.com/100x100.png?text=Adidas" 
                                 class="img-thumbnail img-tenis" 
                                 alt="Adidas Superstar">
                        </td>
                        <td>
                            <h5 class="mb-1">Adidas Superstar Foundation</h5>
                            <ul class="list-unstyled">
                                <li><small>Cor: Preto/Branco</small></li>
                                <li><small>Característica: Shell toe</small></li>
                                <li><span class="badge bg-warning text-dark">Últimas unidades</span></li>
                            </ul>
                        </td>
                        <td>
                            <span class="text-success fw-bold">R$ 499,90</span>
                            <div class="mt-1">
                                <small class="text-muted">ou 10x R$ 49,99</small>
                            </div>
                        </td>
                    </tr>

                    <!-- Itens 3-15 (padrão similar) -->
                    <!-- [Conteúdo repetido com diferentes valores e informações] -->
                    
                </tbody>
                <tfoot class="table-secondary">
                    <tr>
                        <td colspan="3" class="text-center small">
                            * Preços válidos até 30/11/2023 | Frete grátis para compras acima de R$ 300,00
                        </td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

💡 **Principais Atualizações para Bootstrap 5:**

1. **Sistema Responsivo:**
   - `table-responsive-lg`: Tabela scrollable horizontal em telas menores
   - Layout adaptativo automático com classes do container Bootstrap

2. **Componentes Modernos:**
   - `badge`: Para status de disponibilidade
   - `img-thumbnail`: Estilo padrão para imagens
   - `shadow`: Efeito de profundidade na tabela

3. **Classes de Estilização:**
   - `table-striped`: Listras alternadas
   - `table-hover`: Efeito hover nas linhas
   - `align-middle`: Alinhamento vertical centralizado
   - `text-success`: Para preços em verde
   - `fw-bold`: Texto em negrito

4. **Layout Aprimorado:**
   - Sistema de grid flexível com `container` e `py-5` (padding vertical)
   - Espaçamentos responsivos com classes como `mb-4` e `mt-1`

5. **Componentes de Feedback:**
   - `del` para preços cortados
   - `small` para textos secundários
   - `list-unstyled` para listas limpas

6. **Acessibilidade:**
   - `scope="col"` em cabeçalhos
   - Textos alternativos em imagens
   - Hierarquia de cabeçalhos (`h1` > `h5`)

✨ **Vantagens da Versão com Bootstrap:**
1. Design consistente em todos os dispositivos
2. Menos CSS customizado necessário
3. Componentes pré-estilizados e acessíveis
4. Facilidade de manutenção
5. Sistema de temas integrado

**Dica:** Para ver todos os estilos disponíveis, consulte a [documentação oficial do Bootstrap](https://getbootstrap.com/docs/5.3/content/tables/).


