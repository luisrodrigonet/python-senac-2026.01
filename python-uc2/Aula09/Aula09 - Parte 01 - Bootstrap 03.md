# Aula 09 - Parte 01 - Bootstrap 03
>
> ---
>

## Introdução ao Carousel no Bootstrap 5

O Carousel é um componente do Bootstrap que permite criar slideshows para percorrer elementos como imagens, textos ou qualquer conteúdo personalizado de forma sequencial. Ele é construído com transformações CSS 3D e um pouco de JavaScript, oferecendo uma experiência dinâmica e responsiva .

**Principais características:**
- Suporte a navegação por controles anterior/próximo
- Indicadores de posição (pontos na parte inferior)
- Transições suaves entre slides
- Responsivo por padrão
- Pausa automática quando a página não está visível (usando Page Visibility API) 

### Criando um Carousel Básico

Vamos começar com um exemplo simples de carousel com três slides de imagens:

```html
<div id="meuCarousel" class="carousel slide" data-bs-ride="carousel">
    <!-- Indicadores -->
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#meuCarousel" data-bs-slide-to="0" class="active"></button>
        <button type="button" data-bs-target="#meuCarousel" data-bs-slide-to="1"></button>
        <button type="button" data-bs-target="#meuCarousel" data-bs-slide-to="2"></button>
    </div>
    
    <!-- Slides -->
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="https://via.placeholder.com/800x400?text=Slide+1" class="d-block w-100" alt="Primeiro Slide">
        </div>
        <div class="carousel-item">
            <img src="https://via.placeholder.com/800x400?text=Slide+2" class="d-block w-100" alt="Segundo Slide">
        </div>
        <div class="carousel-item">
            <img src="https://via.placeholder.com/800x400?text=Slide+3" class="d-block w-100" alt="Terceiro Slide">
        </div>
    </div>
    
    <!-- Controles -->
    <button class="carousel-control-prev" type="button" data-bs-target="#meuCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Anterior</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#meuCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Próximo</span>
    </button>
</div>
```

#### Explicação do Código:

1. **Estrutura Principal**: 
   - `div` com classes `carousel slide` define o carousel
   - `data-bs-ride="carousel"` faz o carousel iniciar automaticamente 

2. **Indicadores**:
   - `carousel-indicators` mostra os pontos de navegação
   - Cada botão tem `data-bs-target` apontando para o ID do carousel
   - `data-bs-slide-to` define para qual slide ir quando clicado 

3. **Slides**:
   - `carousel-inner` contém os itens do carousel
   - Cada `carousel-item` representa um slide
   - A classe `active` no primeiro item faz ele ser exibido inicialmente 

4. **Controles**:
   - `carousel-control-prev` e `carousel-control-next` adicionam setas de navegação
   - Os ícones são adicionados com `carousel-control-prev-icon` e `carousel-control-next-icon` 

### Adicionando Legendas aos Slides

Você pode adicionar textos sobrepostos aos slides usando a classe `carousel-caption`:

```html
<div class="carousel-item active">
    <img src="https://via.placeholder.com/800x400?text=Slide+1" class="d-block w-100" alt="Primeiro Slide">
    <div class="carousel-caption d-none d-md-block">
        <h5>Título do Primeiro Slide</h5>
        <p>Descrição ou conteúdo adicional aqui.</p>
    </div>
</div>
```

**Observações**:
- `d-none d-md-block` faz as legendas serem ocultadas em telas pequenas e exibidas em médias/grandes 
- Você pode estilizar as legendas com CSS personalizado

### **Alterando o Efeito de Transição**

Por padrão, o carousel usa um efeito de deslize. Você pode mudar para um efeito de fade adicionando a classe `carousel-fade`:

```html
<div id="meuCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
    <!-- conteúdo do carousel -->
</div>
```

### **Controlando o Intervalo entre Slides**

Você pode definir intervalos diferentes para cada slide ou para todo o carousel:

```html
<!-- Intervalo global -->
<div id="meuCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
    <!-- conteúdo do carousel -->
</div>

<!-- Intervalo por slide -->
<div class="carousel-item active" data-bs-interval="1000">
    <!-- conteúdo do slide -->
</div>

<div class="carousel-item" data-bs-interval="2000">
    <!-- conteúdo do slide -->
</div>
```

## Introdução aos Modais no Bootstrap

Um modal é um componente de diálogo/balão que aparece sobre o conteúdo principal da página, criando um foco temporário para interação do usuário. Os modais Bootstrap são construídos com HTML, CSS e JavaScript, e são responsivos por padrão .

**Principais características:**
- Posicionam-se sobre todo o conteúdo da página
- Desativam a rolagem da página principal enquanto estão abertos
- Suportam apenas uma janela modal por vez (não permitem modais aninhados)
- Usam `position: fixed`, o que requer cuidados especiais no posicionamento 

### Configuração Inicial

Para usar modais no Bootstrap 5, você precisa incluir as dependências necessárias:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorial Modal Bootstrap</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Seu conteúdo aqui -->
    
    <!-- Bootstrap JS Bundle com Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Estrutura Básica de um Modal

Um modal Bootstrap consiste em três partes principais:

1. **Botão de acionamento** - Elemento que abre o modal (geralmente um botão)
2. **Estrutura do modal** - HTML que define o conteúdo do modal
3. **JavaScript** - Lógica opcional para interações avançadas

#### Exemplo Básico 

```html
<!-- Botão para abrir o modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exemploModal">
  Abrir Modal
</button>

<!-- Estrutura do Modal -->
<div class="modal fade" id="exemploModal" tabindex="-1" aria-labelledby="exemploModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exemploModalLabel">Título do Modal</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>
      </div>
      <div class="modal-body">
        Conteúdo do modal vai aqui...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
        <button type="button" class="btn btn-primary">Salvar</button>
      </div>
    </div>
  </div>
</div>
```

**Explicação das classes e atributos:**
- `.modal`: Classe base que define o container do modal
- `.fade`: Adiciona efeito de transição ao abrir/fechar
- `aria-labelledby`: Relaciona o título do modal para acessibilidade
- `aria-hidden="true"`: Indica que o modal está inicialmente oculto
- `data-bs-toggle="modal"`: Ativa a funcionalidade de modal no elemento
- `data-bs-target="#exemploModal"`: Especifica qual modal será aberto 

### Componentes do Modal

#### Cabeçalho do Modal (`.modal-header`)
Contém o título e o botão de fechar. Recomenda-se sempre incluir uma ação de fechamento explícita .

#### Corpo do Modal (`.modal-body`)
Área principal para o conteúdo. Pode conter qualquer HTML, incluindo formulários, imagens, textos, etc.

#### Rodapé do Modal (`.modal-footer`)
Opcional. Geralmente contém botões de ação como "Salvar", "Cancelar", etc.


### Tamanhos do Modal
Bootstrap oferece classes para modais de diferentes tamanhos :

```html
<!-- Modal Pequeno -->
<div class="modal-dialog modal-sm">...</div>

<!-- Modal Médio (padrão) -->
<div class="modal-dialog">...</div>

<!-- Modal Grande -->
<div class="modal-dialog modal-lg">...</div>

<!-- Modal Extra Grande -->
<div class="modal-dialog modal-xl">...</div>

<!-- Modal em Tela Cheia -->
<div class="modal-dialog modal-fullscreen">...</div>
```

### Modal Centralizado Verticalmente
Adicione `.modal-dialog-centered` para centralizar verticalmente :

```html
<div class="modal-dialog modal-dialog-centered">
  ...
</div>
```

### Modal com Rolagem
Quando o conteúdo é longo, você pode permitir rolagem apenas dentro do modal :

```html
<div class="modal-dialog modal-dialog-scrollable">
  ...
</div>
```

### Backdrop Estático
Impede que o modal feche ao clicar fora dele :

```html
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1">
  ...
</div>
```

## Introdução ao Accordion no Bootstrap

O componente **Accordion** (acordeão) é uma interface que permite mostrar e ocultar seções de conteúdo de forma organizada. Neste tutorial, vamos explorar como implementar um accordion usando HTML5 e a versão mais recente do Bootstrap (atualmente Bootstrap 5.3).

### Estrutura Básica do Accordion

O accordion do Bootstrap é construído com uma combinação de elementos HTML e classes CSS específicas. Veja a estrutura básica:

```html
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Título do Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        Conteúdo do primeiro item do accordion.
      </div>
    </div>
  </div>
  <!-- Mais itens podem ser adicionados aqui -->
</div>
```

#### Explicação dos Componentes

1. **`accordion`**: A classe principal que envolve todo o componente.
2. **`accordion-item`**: Define cada item individual do accordion.
3. **`accordion-header`**: Contém o título/controle do item.
4. **`accordion-button`**: O botão que controla a expansão/colapso.
5. **`accordion-collapse`**: A área de conteúdo que será mostrada/ocultada.
6. **`accordion-body`**: O container para o conteúdo real.

### Exemplo Completo

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Accordion Bootstrap 5</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-5">
    <h2 class="mb-4">Accordion Básico</h2>
    
    <div class="accordion" id="meuAccordion">
      <!-- Item 1 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="cabecalhoUm">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#colapsoUm" aria-expanded="true" aria-controls="colapsoUm">
            O que é HTML?
          </button>
        </h2>
        <div id="colapsoUm" class="accordion-collapse collapse show" aria-labelledby="cabecalhoUm" data-bs-parent="#meuAccordion">
          <div class="accordion-body">
            HTML (HyperText Markup Language) é a linguagem de marcação padrão para criar páginas web. Ele define a estrutura e o significado do conteúdo web.
          </div>
        </div>
      </div>
      
      <!-- Item 2 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="cabecalhoDois">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#colapsoDois" aria-expanded="false" aria-controls="colapsoDois">
            O que é CSS?
          </button>
        </h2>
        <div id="colapsoDois" class="accordion-collapse collapse" aria-labelledby="cabecalhoDois" data-bs-parent="#meuAccordion">
          <div class="accordion-body">
            CSS (Cascading Style Sheets) é uma linguagem de estilo usada para descrever a apresentação de um documento escrito em HTML. O CSS descreve como elementos devem ser renderizados na tela.
          </div>
        </div>
      </div>
      
      <!-- Item 3 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="cabecalhoTres">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#colapsoTres" aria-expanded="false" aria-controls="colapsoTres">
            O que é JavaScript?
          </button>
        </h2>
        <div id="colapsoTres" class="accordion-collapse collapse" aria-labelledby="cabecalhoTres" data-bs-parent="#meuAccordion">
          <div class="accordion-body">
            JavaScript é uma linguagem de programação que permite implementar funcionalidades complexas em páginas web. Quando aplicada a um documento HTML, pode fornecer interatividade dinâmica em websites.
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap JS Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```