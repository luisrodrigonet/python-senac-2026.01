# Aula 03 - Parte 4 - Bootstrap - Sistema de Grid

## 1. Fundamentos do Grid

### :books: Elementos Principais

- **Container**: Elemento `wrapper` fundamental
  - `.container`: Largura fixa responsiva (**max-width** em breakpoints)
  - `.container-fluid`: Largura **100%** do viewport
  - `.container-{breakpoint}`: Largura 100% até o breakpoint especificado

- **Row**: 
  - `.row`: Define um flex container (display: flex)
  - Remove `padding` do container pai e usa  margem negativa para alinhamento

- **Col**:
  - `.col`: Classe base para colunas
  - `.col-{breakpoint}-{n}`: Especifica largura em diferentes `breakpoints`

### :books: Flexbox 

**Flexbox** (Flexible Box Layout) é um modelo de layout do CSS projetado para organizar elementos em uma interface de forma **dinâmica**, **responsiva** e **eficiente**. Ele permite distribuir espaço entre itens em um container, alinhá-los de maneira precisa e criar layouts complexos sem depender de floats ou posicionamentos fixos.

**Floats** são uma propriedade do CSS usada originalmente para posicionar elementos à esquerda ou à direita de um container, permitindo que outros elementos (como texto) "flutuem" ao seu redor. Embora tenham sido amplamente usados para criar layouts no passado, hoje são considerados **obsoletos para construção de layouts complexos**, sendo substituídos por Flexbox e CSS Grid. No entanto, ainda são úteis em casos específicos.


#### :bookmark: **Para que serve o Flexbox**

1. **Alinhamento inteligente** : Centralizar elementos vertical/horizontalmente com facilidade.

2. **Distribuição de espaço** : Ajustar automaticamente o tamanho dos elementos para preencher o espaço disponível.

3. **Ordenação visual** : Alterar a ordem dos elementos independentemente do HTML.
   
4. **Responsividade** : Criar layouts que se adaptam a diferentes tamanhos de tela.
   
5. **Direcionamento flexível** : Organizar elementos em linhas ou colunas.


#### :bookmark: **Eixos**  
- **Eixo principal**: Direção definida por `flex-direction` (padrão: horizontal).  
- **Eixo transversal**: Perpendicular ao principal.

 **Propriedades Principais**

:globe_with_meridians: Para o **Container**:

| Propriedade          | Função                                      | Valores Comuns                     |
|----------------------|--------------------------------------------|------------------------------------|
| `flex-direction`     | Define a direção dos itens                 | `row`, `column`, `row-reverse`     |
| `justify-content`    | Alinha itens no **eixo principal**         | `center`, `space-between`, `start` |
| `align-items`        | Alinha itens no **eixo transversal**       | `center`, `stretch`, `baseline`    |
| `flex-wrap`          | Permite quebra de linha                    | `wrap`, `nowrap`                   |
| `gap`                | Espaçamento entre itens                    | `10px`, `1rem`                     |

:globe_with_meridians: Para os **Itens**:

| Propriedade      | Função                                  | Valores Comuns         |
|------------------|----------------------------------------|------------------------|
| `order`          | Ordem visual dos itens                 | `0`, `1`, `-1`        |
| `flex-grow`      | Capacidade de expandir                 | `0`, `1`, `2`         |
| `flex-shrink`    | Capacidade de encolher                 | `0`, `1`              |
| `align-self`     | Alinhamento individual no eixo transv. | `center`, `flex-start` |



#### :bookmark: **Alinhamento Horizontal (Eixo Principal)**

Classes: `.justify-content-*`

```html
<div class="d-flex justify-content-start bg-light p-2 mb-3">
  <div class="p-2 bg-primary text-white">Item 1</div>
  <div class="p-2 bg-danger text-white">Item 2</div>
</div>

<div class="d-flex justify-content-center bg-light p-2 mb-3">
  <!-- Itens centralizados -->
</div>

<div class="d-flex justify-content-end bg-light p-2 mb-3">
  <!-- Itens à direita -->
</div>

<div class="d-flex justify-content-between bg-light p-2 mb-3">
  <!-- Espaço entre os itens -->
</div>

<div class="d-flex justify-content-around bg-light p-2">
  <!-- Espaço ao redor -->
</div>
```

#### :bookmark: **Alinhamento Vertical (Eixo Transversal)**

Classes: `.align-items-*`

```html
<div class="d-flex align-items-start bg-light p-2 mb-3" style="height: 100px;">
  <div class="p-2 bg-primary text-white">Topo</div>
</div>

<div class="d-flex align-items-center bg-light p-2 mb-3" style="height: 100px;">
  <div class="p-2 bg-primary text-white">Centro</div>
</div>

<div class="d-flex align-items-end bg-light p-2" style="height: 100px;">
  <div class="p-2 bg-primary text-white">Base</div>
</div>
```

#### :bookmark: **Alinhamento Individual de Itens**

Classes: `.align-self-*`

```html
<div class="d-flex bg-light p-2" style="height: 150px;">
  <div class="align-self-start p-2 bg-warning">Topo</div>
  <div class="align-self-center p-2 bg-success">Centro</div>
  <div class="align-self-end p-2 bg-danger">Base</div>
</div>
```

## **2. Integração entre Grid e Flexbox**

O `grid` é construído com `Flexbox`, oferecendo:

- Layouts unidirecionais (horizontal ou vertical)
- Alinhamento preciso
- Distribuição de espaço inteligente
- Controle de fluxo de itens


### :books: Conceitos Fundamentais:
- **Grid System**: Sistema de 12 colunas responsivo
- **Mobile First**: Design adaptado para dispositivos móveis primeiro
- **Flexbox**: Base tecnológica do sistema
- **Breakpoints**: Pontos de quebra para responsividade

### :books: Setup Inicial:
```html
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Conteúdo aqui -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```



### :books: Breakpoints Detalhados

| Breakpoint | Classe Prefix | Largura      | Comportamento               |
|------------|---------------|--------------|-----------------------------|
| X-Small    | Nenhum        | <576px       | Padrão para mobile          |
| Small      | sm            | ≥576px       | Telefones grandes           |
| Medium     | md            | ≥768px       | Tablets                     |
| Large      | lg            | ≥992px       | Desktops                    |
| X-Large    | xl            | ≥1200px      | Desktops grandes            |
| XX-Large   | xxl           | ≥1400px      | Telas extra grandes         |


### :books: **Tipos de Containers**

```html
<!-- Container padrão responsivo -->
<div class="container"></div>

<!-- Largura total -->
<div class="container-fluid"></div>

<!-- Container responsivo personalizado -->
<div class="container-sm"></div>
<div class="container-md"></div>
<div class="container-lg"></div>
```

## 3. Sistema de Colunas Avançado

### :books: Column Wrapping

Quando mais de 12 colunas são colocadas em uma linha, o grupo excedente cria uma nova linha
```html
<div class="row">
  <div class="col-9">9 </div>
  <div class="col-6">6 (4+6=10)</div>
  <div class="col-6">6 (4+6+6=16 → Nova linha)</div>
</div>
```

### :books: Column Breaks

Forçar quebra de linha com `.w-100`
```html
<div class="row">
  <div class="col-6">6</div>
  <div class="w-100"></div> <!-- Break -->
  <div class="col-6">6</div>
</div>
```

## 4. Alinhamento Avançado

### :books: Vertical Alignment
```html
<div class="row align-items-start"> <!-- Top -->
<div class="row align-items-center"> <!-- Center -->
<div class="row align-items-end"> <!-- Bottom -->

<!-- Alinhamento individual -->
<div class="row">
  <div class="col align-self-start"></div>
  <div class="col align-self-center"></div>
  <div class="col align-self-end"></div>
</div>
```

### :books: Horizontal Alignment

```html
<div class="row justify-content-start"> <!-- Esquerda (padrão) -->
<div class="row justify-content-center"> <!-- Centro -->
<div class="row justify-content-end"> <!-- Direita -->
<div class="row justify-content-between"> <!-- Espaço entre -->
<div class="row justify-content-around"> <!-- Espaço ao redor -->
<div class="row justify-content-evenly"> <!-- Espaço igual -->
```

## 5. Offset e Margin Utilities

### :books: Offsetting Columns
```html
<div class="row">
  <div class="col-md-4 offset-md-4"> <!-- Centralizado -->
  <div class="col-3 offset-lg-2"> <!-- Offset responsivo -->
</div>
```

### :books: Margin Utilities
```html
<div class="row">
  <div class="col-4 ms-auto"> <!-- Margin Start Auto -->
  <div class="col-4 me-lg-5"> <!-- Margin End com breakpoint -->
</div>
```

## 6. Gutters (Espaçamentos)

### :books: Horizontal Gutters
```html
<div class="row gx-0"> <!-- Sem espaçamento -->
<div class="row gx-1"> <!-- 4px -->
<div class="row gx-5"> <!-- 48px -->
```

### :books: Vertical Gutters
```html
<div class="row gy-4"> <!-- Espaçamento vertical 24px -->
```

### :books: Gutters Combinados
```html
<div class="row g-3"> <!-- Espaçamento 12px em ambos eixos -->
```

## 7. Flexbox Options

### :books: Direction
```html
<div class="row flex-row"> <!-- Padrão horizontal -->
<div class="row flex-row-reverse"> <!-- Invertido -->
<div class="row flex-column"> <!-- Vertical -->
<div class="row flex-column-reverse"> <!-- Vertical invertido -->
```

### :books: Flex Fill
```html
<div class="row">
  <div class="col flex-fill">Preenche espaço disponível</div>
</div>
```

### :books: Order
```html
<div class="row">
  <div class="col order-3">Primeiro</div>
  <div class="col order-1">Segundo</div>
</div>
```

## 8. Exemplo Completo com Todos os Recursos
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Website Avançado</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .box { background: #f8f9fa; border: 1px solid #dee2e6; padding: 20px; margin-bottom: 1rem; }
    </style>
</head>
<body>

<!-- Container Responsivo -->
<div class="container-lg">

    <!-- Header com Alinhamento Complexo -->
    <header class="row py-3 align-items-center gx-5">
        <div class="col-12 col-md-4 order-md-2 text-center">
            <h2 class="mb-0">Logo Central</h2>
        </div>
        <div class="col-6 col-md-4 order-md-1">
            <nav class="d-flex justify-content-start gap-3">
                <a href="#">Menu Esq</a>
            </nav>
        </div>
        <div class="col-6 col-md-4 order-md-3">
            <div class="d-flex justify-content-end">
                <button class="btn btn-primary">Login</button>
            </div>
        </div>
    </header>

    <!-- Hero Section com Vertical Alignment -->
    <section class="row min-vh-50 bg-light align-items-center justify-content-center gy-4">
        <div class="col-12 col-lg-8 text-center">
            <h1 class="display-4">Layout Complexo</h1>
            <p class="lead">Demonstração de recursos avançados</p>
        </div>
        <div class="col-12 col-lg-4 order-lg-first">
            <div class="box">
                <h3>Conteúdo Lateral</h3>
                <p>Exemplo de order</p>
            </div>
        </div>
    </section>

    <!-- Grid Complexo com Multiple Breakpoints -->
    <section class="row g-4">
        <div class="col-12 col-sm-6 col-xl-3">
            <div class="box h-100">
                <h4>Card 1</h4>
                <p>Responsivo: 12/6/3 colunas</p>
            </div>
        </div>
        <div class="col-12 col-sm-6 col-xl-3">
            <div class="box h-100">
                <h4>Card 2</h4>
                <p>Com altura igual</p>
            </div>
        </div>
        <div class="col-12 col-sm-6 col-xl-3 offset-xl-0 offset-sm-3">
            <div class="box h-100">
                <h4>Card 3</h4>
                <p>Offset personalizado</p>
            </div>
        </div>
        <div class="col-12 col-sm-6 col-xl-3">
            <div class="box h-100">
                <h4>Card 4</h4>
                <p>Com gutter ajustado</p>
            </div>
        </div>
    </section>

    <!-- Seção com Column Wrapping -->
    <section class="row gx-5 gy-4 mt-5">
        <div class="col-8">Main Content</div>
        <div class="col-4">Sidebar</div>
        <div class="w-100"></div> <!-- Break -->
        <div class="col-6">Lower Section 1</div>
        <div class="col-6">Lower Section 2</div>
    </section>

    <!-- Footer com Alinhamento Vertical -->
    <footer class="row py-4 mt-5 border-top align-items-center">
        <div class="col-md-4 mb-3 mb-md-0">
            <p class="text-body-secondary">© 2024 Empresa</p>
        </div>
        <div class="col-md-8">
            <nav class="d-flex justify-content-md-end gap-4">
                <a href="#">Políticas</a>
                <a href="#">Termos</a>
                <a href="#">Contato</a>
            </nav>
        </div>
    </footer>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### :books: Explicação do Exemplo Completo:

1. **Container Responsivo**:
   - Usa `.container-lg` para limitar largura máxima em telas grandes

2. **Header**:
   - Layout 3 colunas com reordenamento (order-md-*)
   - Gutters horizontais personalizadas (gx-5)
   - Combinação de alinhamentos flex

3. **Hero Section**:
   - Altura mínima (min-vh-50)
   - Alinhamento vertical central (align-items-center)
   - Ordem invertida em desktop (order-lg-first)

4. **Grid Complexo**:
   - 4 cards responsivos com múltiplos breakpoints
   - Offset personalizado para diferentes telas
   - Altura igual (h-100)

5. **Column Wrapping**:
   - Uso proposital de 8+4 colunas seguido por break
   - Divisão explícita com `.w-100`

6. **Footer**:
   - Alinhamento vertical central
   - Margem condicional (mb-3 mb-md-0)
   - Alinhamento horizontal responsivo

