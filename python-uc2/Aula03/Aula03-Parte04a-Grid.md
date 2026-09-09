# Aula 03 - Parte 4 (full) - Bootstrap - Sistema de Grid
>  Domínio do Sistema Grid do Bootstrap 5
>
> Esta aula cobre todos os aspectos essenciais do sistema grid do Bootstrap 5, com progressão lógica de conceitos e aplicação prática. 
> Cada exercício foi projetado para reforçar habilidades específicas, culminando em um projeto realista que integra todos os conhecimentos adquiridos.
>
> ---

## :one: **Introdução**

### Conceitos Fundamentais:
- **Grid System**: Sistema de 12 colunas responsivo
- **Mobile First**: Design adaptado para dispositivos móveis primeiro
- **Flexbox**: Base tecnológica do sistema
- **Breakpoints**: Pontos de quebra para responsividade

### Setup Inicial:
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

---

## :two: **Containers**
### Teoria:
- `.container`: Largura fixa responsiva
- `.container-fluid`: Largura total
- `.container-{breakpoint}`: Híbrido

### Exemplo Prático:
```html
<div class="container border">Largura fixa</div>
<div class="container-fluid border">Largura total</div>
```

### Exercício 1:
Crie 3 containers diferentes:
1. Que ocupe 100% até 768px
2. Fixo para desktop
3. Fluido apenas em telas grandes

<details>
<summary>Resposta</summary>

```html
<div class="container-md border"></div>
<div class="container-lg border"></div>
<div class="container-fluid d-lg-block"></div>
```
</details>

---

## :three: **Linhas e Colunas**
### Teoria:
- `.row`: Flex container
- `.col`: Divisão automática
- `.col-{n}`: Tamanho fixo (1-12)

### Exemplo:
```html
<div class="container">
    <div class="row">
        <div class="col-4 border">33%</div>
        <div class="col-8 border">66%</div>
    </div>
</div>
```

### Exercício 2:
Crie um layout com:
- 3 colunas iguais em desktop
- 2 colunas em tablet
- 1 coluna em mobile

<details>
<summary>Resposta</summary>

```html
<div class="row">
    <div class="col-12 col-md-6 col-lg-4">Conteúdo</div>
    <div class="col-12 col-md-6 col-lg-4">Conteúdo</div>
    <div class="col-12 col-md-6 col-lg-4">Conteúdo</div>
</div>
```
</details>

---

## :four: **Breakpoints e Responsividade**

### Tabela de Breakpoints:

| Classe | Largura    | Dispositivo      |
|--------|------------|------------------|
| sm     | ≥576px     | Smartphones      |
| md     | ≥768px     | Tablets          |
| lg     | ≥992px     | Laptops          |
| xl     | ≥1200px    | Desktops         |
| xxl    | ≥1400px    | Telas Grandes    |

### Exercício 3:
Crie um card que:
- Ocupe 6 colunas em mobile
- 4 colunas em tablets
- 3 colunas em desktops

<details>
<summary>Resposta</summary>

```html
<div class="col-6 col-md-4 col-lg-3"></div>
```
</details>

---

## :five: **Alinhamentos**
### Vertical:
```html
<div class="row align-items-start/center/end">
    <div class="col align-self-start/center/end">
```

### Horizontal:
```html
<div class="row justify-content-start/center/end/between/around">
```

### Exercício 4:
Centralize vertical e horizontalmente um conteúdo dentro de uma linha de 500px de altura

<details>
<summary>Resposta</summary>

```html
<div class="row justify-content-center align-items-center" style="height: 500px;">
    <div class="col-auto">Conteúdo Centralizado</div>
</div>
```
</details>

---

## :six: **Recursos Avançados**

### :books: Gutters
```html
<div class="row g-0/g-1/g-3/g-5">
```

### :books: Offsets
```html
<div class="col-6 offset-3">
```

### :books:Ordem
```html
<div class="col order-1/order-md-2">
```

### Exercício 5:
Crie 2 colunas com:
- Espaçamento duplo entre elas
- Segunda coluna offset em desktop
- Ordem invertida em mobile

<details>
<summary>Resposta</summary>

```html
<div class="row g-4">
    <div class="col-md-6 order-2 order-md-1">Col 1</div>
    <div class="col-md-4 offset-md-2 order-1 order-md-2">Col 2</div>
</div>
```
</details>

---

## :seven: **Projeto Final**

### Requisitos:
1. Header com logo à esquerda e menu à direita
2. Seção hero centralizada verticalmente
3. Grid de 4 cards responsivos
4. Footer com 3 colunas alinhadas no topo

### Exercício 6:
Implemente o layout acima usando todas as técnicas aprendidas

<details>
<summary>Solução Proposta</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .hero-section { height: 400px; }
        .card { height: 200px; }
    </style>
</head>
<body>

<!-- Header -->
<header class="container py-3">
    <div class="row justify-content-between align-items-center">
        <div class="col-auto">
            <h2>Logo</h2>
        </div>
        <nav class="col-auto">
            <a href="#" class="me-3">Home</a>
            <a href="#" class="me-3">Sobre</a>
            <a href="#">Contato</a>
        </nav>
    </div>
</header>

<!-- Hero -->
<section class="hero-section bg-light">
    <div class="container h-100">
        <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8 text-center">
                <h1>Título Principal</h1>
                <p>Texto de introdução</p>
            </div>
        </div>
    </div>
</section>

<!-- Cards -->
<section class="container py-5">
    <div class="row g-4">
        <div class="col-12 col-sm-6 col-lg-3">
            <div class="card p-3">
                Card 1
            </div>
        </div>
        <!-- Repetir para 3 cards adicionais -->
    </div>
</section>

<!-- Footer -->
<footer class="container py-5 border-top">
    <div class="row">
        <div class="col-md-4">
            <h5>Seção 1</h5>
            <p>Conteúdo</p>
        </div>
        <div class="col-md-4">
            <h5>Seção 2</h5>
            <p>Conteúdo</p>
        </div>
        <div class="col-md-4">
            <h5>Seção 3</h5>
            <p>Conteúdo</p>
        </div>
    </div>
</footer>

</body>
</html>
```
</details>


## :seven: **Desafio Extra:**

Desafio Extra: Criar um layout de blog responsivo

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Responsivo</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .card-img-top {
            height: 200px;
            object-fit: cover;
        }
        
        .sidebar-card {
            background-color: #f8f9fa;
            border: none;
        }

        body {
            background-color: #e9ecef;
        }

        .main-content {
            margin-top: 30px;
        }
    </style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">Meu Blog</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Sobre</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contato</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- Conteúdo Principal -->
<div class="container main-content">
    <div class="row g-4">
        <!-- Posts -->
        <div class="col-lg-8">
            <div class="row row-cols-1 row-cols-md-2 g-4">
                <!-- Post 1 -->
                <div class="col">
                    <div class="card h-100">
                        <img src="https://source.unsplash.com/random/600x400" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Título do Post 1</h5>
                            <p class="card-text text-muted small">Publicado em 01/01/2023 por Autor</p>
                            <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptates...</p>
                            <a href="#" class="btn btn-primary">Leia mais</a>
                        </div>
                    </div>
                </div>

                <!-- Post 2 -->
                <div class="col">
                    <div class="card h-100">
                        <img src="https://source.unsplash.com/random/601x400" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Título do Post 2</h5>
                            <p class="card-text text-muted small">Publicado em 02/01/2023 por Autor</p>
                            <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptates...</p>
                            <a href="#" class="btn btn-primary">Leia mais</a>
                        </div>
                    </div>
                </div>

                <!-- Post 3 -->
                <div class="col">
                    <div class="card h-100">
                        <img src="https://source.unsplash.com/random/602x400" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Título do Post 3</h5>
                            <p class="card-text text-muted small">Publicado em 03/01/2023 por Autor</p>
                            <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptates...</p>
                            <a href="#" class="btn btn-primary">Leia mais</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Paginação -->
            <nav class="mt-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled">
                        <a class="page-link" href="#" tabindex="-1">Anterior</a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                        <a class="page-link" href="#">Próxima</a>
                    </li>
                </ul>
            </nav>
        </div>

        <!-- Sidebar -->
        <div class="col-lg-4">
            <div class="card sidebar-card mb-4">
                <div class="card-body">
                    <h5 class="card-title">Pesquisar</h5>
                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Digite aqui...">
                        <button class="btn btn-primary" type="button">Buscar</button>
                    </div>
                </div>
            </div>

            <div class="card sidebar-card mb-4">
                <div class="card-body">
                    <h5 class="card-title">Categorias</h5>
                    <div class="list-group">
                        <a href="#" class="list-group-item list-group-item-action">Tecnologia</a>
                        <a href="#" class="list-group-item list-group-item-action">Programação</a>
                        <a href="#" class="list-group-item list-group-item-action">Design</a>
                        <a href="#" class="list-group-item list-group-item-action">Carreira</a>
                    </div>
                </div>
            </div>

            <div class="card sidebar-card">
                <div class="card-body">
                    <h5 class="card-title">Posts Recentes</h5>
                    <ul class="list-unstyled">
                        <li class="mb-3">
                            <a href="#" class="text-decoration-none">Post Recente 1</a>
                            <p class="small text-muted mb-0">01/01/2023</p>
                        </li>
                        <li class="mb-3">
                            <a href="#" class="text-decoration-none">Post Recente 2</a>
                            <p class="small text-muted mb-0">02/01/2023</p>
                        </li>
                        <li>
                            <a href="#" class="text-decoration-none">Post Recente 3</a>
                            <p class="small text-muted mb-0">03/01/2023</p>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Footer -->
<footer class="bg-dark text-white mt-5">
    <div class="container py-4">
        <div class="row">
            <div class="col-md-6">
                <h5>Sobre Nós</h5>
                <p class="small">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat, voluptatem.</p>
            </div>
            <div class="col-md-3">
                <h5>Links Úteis</h5>
                <ul class="list-unstyled small">
                    <li><a href="#" class="text-white text-decoration-none">Política de Privacidade</a></li>
                    <li><a href="#" class="text-white text-decoration-none">Termos de Uso</a></li>
                </ul>
            </div>
            <div class="col-md-3">
                <h5>Redes Sociais</h5>
                <ul class="list-unstyled small">
                    <li><a href="#" class="text-white text-decoration-none">Facebook</a></li>
                    <li><a href="#" class="text-white text-decoration-none">Twitter</a></li>
                    <li><a href="#" class="text-white text-decoration-none">Instagram</a></li>
                </ul>
            </div>
        </div>
        <div class="text-center mt-3 pt-3 border-top">
            <p class="small mb-0">&copy; 2023 Meu Blog. Todos os direitos reservados.</p>
        </div>
    </div>
</footer>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

Este layout inclui:

1. Uma navbar responsiva que colapsa em dispositivos móveis
2. Área principal de posts com cards responsivos
3. Sidebar com widgets de pesquisa, categorias e posts recentes
4. Paginação
5. Footer responsivo com múltiplas colunas
6. Layout totalmente responsivo que se adapta a diferentes tamanhos de tela

Recursos utilizados:
- Sistema de grid do Bootstrap para criar layouts responsivos
- Cards para exibir os posts e widgets
- Classes utilitárias para espaçamento e cores
- Componentes do Bootstrap como navbar, paginação e forms
- Layout que se ajusta automaticamente entre dispositivos móveis e desktop

Características responsivas:
- Navbar colapsável em telas pequenas
- Posts em colunas que mudam de 2 para 1 coluna em dispositivos móveis
- Sidebar que fica abaixo dos posts em telas pequenas
- Footer com colunas que se ajustam verticalmente em mobile
- Imagens responsivas nos cards




## :eight: **Recursos Adicionais**

1. [Documentação Oficial do Bootstrap](https://getbootstrap.com/docs/5.3/layout/grid/)

1. Ferramenta de Prática: [Grid Generator](https://layout.bootstrapdocs.com/)

1. Erros Comuns:
   - Esquecer de usar `.row` dentro de containers
   - Não resetar paddings em elementos aninhados
   - Confundir breakpoints (md vs lg)


