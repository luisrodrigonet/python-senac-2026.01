# Aula07 - Parte 01 - Bootstrap 01
> O [Bootstrap](https://getbootstrap.com/) é o framework front-end mais popular do mundo, oferecendo:  
> ✔ **Design responsivo** (adaptável a celulares, tablets e desktops)  
> ✔ **Componentes prontos** (botões, cards, navegação)  
> ✔ **Utilitários** (cores, espaçamento, flexbox)  
> 
> Nesta aula, focaremos em:  
> - **Ícones** (`Bootstrap Icons`)  
> - **Containers** (estrutura base)  
> - **Sistema de Grid** (responsividade)  
> - **Cores Contextuais** (feedback visual)  
> - **Cards** (exibição de conteúdo)  
> ---
> 

## :one: **Configuração Inicial**  

### **Estrutura HTML Básica**  
Antes de usar o Bootstrap, inclua no `<head>` e no `<body>` as seguintes linhas:  
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula Bootstrap</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Bootstrap Icons -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
</head>
<body>
  <!-- Conteúdo aqui -->
  
  <!-- Bootstrap JS (opcional para componentes interativos) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```


### **O que cada CDN faz?**  
| CDN | Função |  
|------|--------|  
| `bootstrap.min.css` | Estilos principais do Bootstrap |  
| `bootstrap-icons.css` | Biblioteca de ícones |  
| `bootstrap.bundle.min.js` | Funcionalidades JS (dropdowns, modais) |  

---

## :two: **Ícones (Bootstrap Icons)**  

Bootstrap Icons é uma biblioteca de ícones SVG de código aberto desenvolvida pela equipe do Bootstrap. Com mais de 1.300 ícones disponíveis, ela oferece uma solução completa para necessidades de design de interface .

**Principais características:**
- Ícones em formato SVG para qualidade vetorial
- Totalmente gratuitos e de código aberto (licença MIT)
- Projetados para funcionar perfeitamente com Bootstrap, mas também independentes
- Otimizados para clareza em tamanhos pequenos (16x16px)
- Fácil personalização via CSS 


### **Como Usar?**  
Adicione ícones com a classe `bi` + nome do ícone ([lista completa](https://icons.getbootstrap.com/)):  

```html
<i class="bi bi-emoji-smile"></i> Sorriso  
<i class="bi bi-check-circle-fill text-success"></i> Sucesso  
```

**Onde**:
- `bi` é a classe base para todos os Bootstrap Icons
- `bi-nome-do-icone` é a classe específica para o ícone desejado 

### **Exemplo Prático**  
```html
<button class="btn btn-primary">
  <i class="bi bi-download"></i> Baixar
</button>
```

### Tamanho dos Ícones

Você pode ajustar o tamanho dos ícones usando a propriedade CSS `font-size`:

```html
<i class="bi bi-heart" style="font-size: 24px;"></i> <!-- Tamanho médio -->
<i class="bi bi-heart" style="font-size: 48px;"></i> <!-- Tamanho grande -->
```

Ou usando classes utilitárias do Bootstrap:

```html
<i class="bi bi-heart fs-1"></i> <!-- Extra large (2.5rem) -->
<i class="bi bi-heart fs-4"></i> <!-- Medium (1.5rem) -->
<i class="bi bi-heart fs-6"></i> <!-- Small (1rem) -->
```

### Cores dos Ícones

Os ícones herdam a cor do texto do elemento pai, mas você pode sobrescrever isso:

```html
<i class="bi bi-star" style="color: gold;"></i> <!-- Ícone dourado -->
<i class="bi bi-star text-danger"></i> <!-- Usando classe de cor do Bootstrap -->
```

### Efeitos de Hover

Adicione interatividade com efeitos hover:

```css
.bi-star:hover {
    color: gold;
    transform: scale(1.2);
    transition: all 0.3s ease;
}
```

---

## :three: **Containers**  

Os containers são elementos fundamentais no Bootstrap 5 que servem como wrappers (envoltórios) para agrupar e organizar o conteúdo da página. Eles são essenciais para criar layouts responsivos e bem estruturados, pois:

- Fornecem um sistema de **padding** (preenchimento interno) padrão
- Centralizam o conteúdo horizontalmente
- Ajudam no alinhamento do **grid system** (sistema de grades)
- Facilitam a criação de **layouts** responsivos


### **Tipos de Containers**  

| Classe | Comportamento |  
|--------|--------------|  
| `.container` | Largura fixa (responsiva por breakpoint) |  
| `.container-fluid` | Largura 100% da tela |  

**Comportamento responsivo da classe `container`:**
- Extra small (<576px): largura 100%
- Small (≥576px): max-width 540px
- Medium (≥768px): max-width 720px
- Large (≥992px): max-width 960px
- Extra large (≥1200px): max-width 1140px
- XXL (≥1400px): max-width 1320px

### **Exemplo Detalhado**  

```html
<div class="container bg-light border p-4 my-4">
  <h2>Container Padrão</h2>
  <p>Centralizado com margens laterais automáticas.</p>
</div>

<div class="container-fluid bg-dark text-white p-4">
  <h2>Container Fluido</h2>
  <p>Ocupa toda a largura da tela.</p>
</div>
```
**Explicação das classes utilitárias:**  
- `bg-light`: Fundo claro  
- `border`: Borda sutil  
- `p-4`: Padding (espaçamento interno) grande  
- `my-4`: Margem no eixo Y (topo e base)  

### Container Responsivo (Breakpoint específico)

Containers que se tornam fluidos até atingir um breakpoint específico:

```html
<div class="container-sm">...</div>
<div class="container-md">...</div>
<div class="container-lg">...</div>
<div class="container-xl">...</div>
<div class="container-xxl">...</div>
```
---

## :four: **Sistema de Grid**  

O **Grid System** (Sistema de Grades) do Bootstrap é uma das funcionalidades mais poderosas para criar layouts responsivos e organizados. Ele permite estruturar o conteúdo em **linhas (rows)** e **colunas (cols)** com comportamentos adaptáveis para diferentes tamanhos de tela.  

### **Como Funciona?**  

O Bootstrap utiliza um sistema de **12 colunas** que pode ser adaptado para diferentes dispositivos (mobile, tablet, desktop).  

- **`.row`**: Define uma linha.  
- **`.col-*`**: Define colunas (total de 12 por linha).  
- **Breakpoints**: `sm` (≥576px), `md` (≥768px), `lg` (≥992px).  

### **Exemplo 01: Responsivo**  
```html
<!-- Container de linhas -->
<div class="container">
  <!-- Linha -->
  <div class="row">
    <!-- 1a Coluna -->
    <div class="col-md-4 bg-info p-3">Coluna 1 (4/12)</div>
    
    <!-- 2a Coluna -->
    <div class="col-md-4 bg-warning p-3">Coluna 2 (4/12)</div>
    
    <!-- 3a Coluna -->
    <div class="col-md-4 bg-danger p-3">Coluna 3 (4/12)</div>
  </div>
  <!-- Final 1a Linha -->
</div>
<!-- Final: Container de linhas -->
```
**Comportamento:**  
- Em telas **menores que 768px**, as colunas ficam empilhadas.  
- Em telas **maiores**, ficam lado a lado.  

### **Classes Responsivas por Breakpoint**  

O Bootstrap usa **6 breakpoints** para adaptar o layout:  

| Breakpoint | Prefixo | Largura mínima |
|------------|---------|----------------|
| Extra Small | `.col-` | < 576px |
| Small       | `.col-sm-` | ≥ 576px |
| Medium      | `.col-md-` | ≥ 768px |
| Large       | `.col-lg-` | ≥ 992px |
| Extra Large | `.col-xl-` | ≥ 1200px |
| XXL         | `.col-xxl-` | ≥ 1400px |

### **Exemplo 2: Layout Responsivo**  
```html
<div class="container">
    <div class="row">
        <!-- Em telas pequenas (1 coluna), médias (2 colunas), grandes (4 colunas) -->
        <div class="col-12 col-md-6 col-lg-3 bg-info p-3">Bloco 1</div>
        <div class="col-12 col-md-6 col-lg-3 bg-warning p-3">Bloco 2</div>
        <div class="col-12 col-md-6 col-lg-3 bg-danger p-3">Bloco 3</div>
        <div class="col-12 col-md-6 col-lg-3 bg-success p-3">Bloco 4</div>
    </div>
</div>
```
**Resultado:**  
- **Mobile (xs):** 1 coluna (100% de largura).  
- **Tablet (md):** 2 colunas (50% cada).  
- **Desktop (lg):** 4 colunas (25% cada).  


### **Alinhamento Vertical**  
```html
<div class="row align-items-start"> <!-- Topo -->
<div class="row align-items-center"> <!-- Centro -->
<div class="row align-items-end"> <!-- Base -->
```

### **Alinhamento Horizontal**  
```html
<div class="row justify-content-start"> <!-- Esquerda -->
<div class="row justify-content-center"> <!-- Centro -->
<div class="row justify-content-end"> <!-- Direita -->
<div class="row justify-content-between"> <!-- Espaçado -->
```

### **Exemplo 3: Centralizando Conteúdo**  
```html
<div class="container">
    <div class="row justify-content-center align-items-center" style="height: 200px; background: #f0f0f0;">
        <div class="col-4 bg-primary text-white p-3 text-center">
            Conteúdo Centralizado
        </div>
    </div>
</div>
```

---

## :five: **Cores Contextuais**  

As **cores contextuais** no Bootstrap são classes pré-definidas que transmitem significado visual (sucesso, erro, alerta, informação) e garantem consistência no design. Elas são usadas em:
- **Textos** (`.text-*`)
- **Fundo** (`.bg-*`)
- **Bordas** (`.border-*`)
- **Botões** (`.btn-*`)


### **Cores Disponíveis**

| Classe         | Cor          | Uso típico                  |
|----------------|--------------|-----------------------------|
| `.text-primary`| Azul         | Ação principal              |
| `.text-secondary`| Cinza     | Conteúdo secundário         |
| `.text-success`| Verde        | Confirmação/sucesso         |
| `.text-danger` | Vermelho     | Erro/alerta crítico         |
| `.text-warning`| Amarelo      | Aviso                       |
| `.text-info`   | Azul-claro   | Informação                  |
| `.text-light`  | Branco       | Fundos escuros              |
| `.text-dark`   | Preto        | Fundos claros               |

### **Exemplo Aplicado**  
```html
<div class="p-3 mb-2 bg-gradient">
  <p class="text-primary">Texto azul (primário)</p>
  <p class="bg-dark text-white">Fundo escuro com texto branco</p>
</div>
```

### **Exemplo : Textos Coloridos**
```html
<p class="text-primary">Texto primário (azul)</p>
<p class="text-success">Texto de sucesso (verde)</p>
<p class="text-danger">Texto de erro (vermelho)</p>
```

### **Exemplo : Fundos Coloridos**
```html
<div class="bg-warning p-3">
    Aviso: Esta ação requer atenção!
</div>
```

### **Exemplo : Botões Contextuais**
```html
<button class="btn btn-primary">Primário</button>
<button class="btn btn-danger">Excluir</button>
```

### **Sobrescrevendo Cores Padrão**
Adicione no seu CSS:
```css
:root {
    --bs-primary: #8a2be2; /* Roxo */
    --bs-danger: #ff4500;  /* Laranja */
}
```

### **Criando Novas Cores Contextuais**
```css
.bg-custom {
    background-color: #20c997;
}
.text-custom {
    color: #20c997;
}
```

---

## :six: **Cards**  

Os **Cards** são componentes versáteis do Bootstrap que funcionam como "containers" flexíveis para exibir conteúdo organizado. Eles são ideais para:
- Produtos em e-commerce
- Posts de blog
- Perfis de usuário
- Painéis de informação

### **Componentes de um Card**
Um card pode conter múltiplas seções:

| Elemento            | Classe               | Descrição                          |
|---------------------|----------------------|-----------------------------------|
| **Imagem no topo**  | `.card-img-top`      | Imagem alinhada ao topo           |
| **Título**          | `.card-title`        | Título destacado                  |
| **Subtítulo**       | `.card-subtitle`     | Texto secundário                  |
| **Texto**           | `.card-text`         | Conteúdo principal                |
| **Rodapé**          | `.card-footer`       | Área inferior                     |
| **Cabeçalho**       | `.card-header`       | Área superior                     |

### **Estrutura Básica**  
```html
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/300" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Título do Card</h5>
    <p class="card-text">Descrição ou conteúdo resumido.</p>
    <a href="#" class="btn btn-primary">Ação</a>
  </div>
</div>
```

### **Exemplo: Card Básico com Imagem**
```html
<div class="card" style="width: 18rem;">
    <img src="produto.jpg" class="card-img-top" alt="Produto">
    <div class="card-body">
        <h5 class="card-title">Nome do Produto</h5>
        <p class="card-text">R$ 99,90</p>
        <a href="#" class="btn btn-primary">Comprar</a>
    </div>
</div>
```

### **Card com Ícone e Cores**  
```html
<div class="card border-success mb-3">
  <div class="card-header bg-success text-white">
    <i class="bi bi-check-circle"></i> Status
  </div>
  <div class="card-body">
    <h5 class="card-title">Sucesso!</h5>
    <p class="card-text">Operação concluída sem erros.</p>
  </div>
</div>
```

### **Exemplo: Card com Cabeçalho e Rodapé**
```html
<div class="card">
    <div class="card-header bg-primary text-white">
        Promoção
    </div>
    <div class="card-body">
        <h5 class="card-title">Oferta Especial</h5>
        <p class="card-text">Desconto de 20% hoje!</p>
    </div>
    <div class="card-footer text-muted">
        Válido até 30/06
    </div>
</div>
```

### **Exemplo: Card Horizontal**
```html
<div class="card mb-3" style="max-width: 540px;">
    <div class="row g-0">
        <div class="col-md-4">
            <img src="perfil.jpg" class="img-fluid rounded-start" alt="...">
        </div>
        <div class="col-md-8">
            <div class="card-body">
                <h5 class="card-title">Perfil do Usuário</h5>
                <p class="card-text">Descrição breve do perfil.</p>
            </div>
        </div>
    </div>
</div>
```

---

## :computer:**Página Completa de Exemplo**  
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exemplo Bootstrap</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg bg-primary navbar-dark">
    <div class="container">
      <a class="navbar-brand" href="#">
        <i class="bi bi-bootstrap"></i> Aula Bootstrap
      </a>
    </div>
  </nav>

  <!-- Container Principal -->
  <div class="container my-5">
    <h1 class="text-center mb-4"><i class="bi bi-code-slash"></i> Componentes Básicos</h1>
    
    <!-- Grid de Cards -->
    <div class="row g-4">
      <div class="col-md-4">
        <div class="card h-100">
          <div class="card-header bg-warning">
            <i class="bi bi-exclamation-triangle"></i> Alerta
          </div>
          <div class="card-body">
            <h5 class="card-title">Atenção</h5>
            <p class="card-text">Este é um card de aviso importante.</p>
            <a href="#" class="btn btn-warning">Saiba mais</a>
          </div>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="card h-100">
          <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card com Imagem</h5>
            <p class="card-text">Exemplo de card com imagem no topo.</p>
          </div>
        </div>
      </div>
      
      <div class="col-md-4">
        <div class="card h-100 border-success">
          <div class="card-body">
            <h5 class="card-title text-success">
              <i class="bi bi-check2-circle"></i> Sucesso
            </h5>
            <p class="card-text">Operação concluída com êxito.</p>
            <button class="btn btn-outline-success">Voltar</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Rodapé -->
  <footer class="bg-dark text-white text-center p-4 mt-5">
    <p class="mb-0">Feito com <i class="bi bi-heart-fill text-danger"></i> e Bootstrap</p>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## :loudspeaker: **Conclusão**  
Nesta aula, aprendemos:  
- **Ícones**: Como integrar e personalizar.  
- **Containers**: Diferença entre `container` e `container-fluid`.  
- **Grid**: Criar layouts responsivos.  
- **Cores**: Uso de classes utilitárias.  
- **Cards**: Estrutura e variações.  

**Próximos passos:**  
- Explorar [Navbars](https://getbootstrap.com/docs/5.3/components/navbar/).  
- Aprender sobre [Formulários](https://getbootstrap.com/docs/5.3/forms/overview/). 

