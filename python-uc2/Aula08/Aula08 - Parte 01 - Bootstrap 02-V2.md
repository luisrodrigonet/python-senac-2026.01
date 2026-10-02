# Aula 08 - Parte 02 - Bootstrap 02
>  **O que é Bootstrap?** Um framework front-end para desenvolvimento responsivo e rápido.
> 
> ---
> 

## :globe_with_meridians: **Configuração:**  
- Inclua o **CSS** no `<head>` e o **JS** no final do `<body>` (requerido para componentes interativos):  
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```


## :one: **Navbar**  

### **Descrição**  

O **Navbar** (navegação responsiva) é um componente essencial para criar menus de navegação adaptáveis a diferentes dispositivos. No Bootstrap 5, o Navbar foi reescrito para usar JavaScript puro (sem dependência de jQuery) e oferece recursos avançados de responsividade. Ela pode conter:
- Logotipo/marca
- Links de navegação
- Dropdowns
- Formulários de busca
- Botões

### **Navbar Simples**

```html
<!-- Navbar ---> 
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <!-- Container -->  
  <div class="container-fluid">
    <!-- Logo -->
    <a class="navbar-brand" href="#">Minha Marca</a>
    
    <!-- Botão -->
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <!-- Conteúdo  -->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#">Início</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Sobre</a>
        </li>
      </ul>
    </div>
    <!-- Conteúdo  -->
    
  </div>
  <!-- Container --> 
</nav>
<!-- Navbar ---> 
```

### **Elementos-Chave**
| Componente               | Classe/Atributo           | Função |
|--------------------------|--------------------------|--------|
| **Container principal**  | `.navbar`                | Define a navbar |
| **Breakpoint**           | `.navbar-expand-*`       | Controla quando vira "hamburger" (lg, md, sm) |
| **Toggler mobile**       | `.navbar-toggler`        | Botão para menu mobile |
| **Área colapsável**      | `.collapse.navbar-collapse` | Conteúdo escondido no mobile |
| **Itens de navegação**   | `.nav-item` + `.nav-link` | Links do menu |


### **Elementos/Propriedades Principais**  

- **`.navbar`**: Classe base.  
- **`.navbar-expand-lg`**: Define o breakpoint para expandir (ex: `lg` = desktop).  
- **`.navbar-dark`/`.navbar-light`**: Define a cor do texto (claro/escuro).  
- **`.bg-*`**: Cor de fundo (ex: `bg-dark`, `bg-primary`).  
- **`.navbar-toggler`**: Botão para expandir/recolher o menu em dispositivos móveis.  
- **`.collapse.navbar-collapse`**: Agrupa os itens que serão colapsados.  
- **Dropdown**: Usa `dropdown`, `dropdown-toggle`, `dropdown-menu`.  

### **Exemplo Prático**  
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <!-- Logo -->
    <a class="navbar-brand" href="#">Empresa</a>

    <!-- Botão Toggler (mobile) -->
    <button 
      class="navbar-toggler" 
      type="button" 
      data-bs-toggle="collapse" 
      data-bs-target="#menuPrincipal"  <!-- ID do elemento a ser colapsado -->
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Itens do Menu -->
    <div class="collapse navbar-collapse" id="menuPrincipal">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a 
            class="nav-link dropdown-toggle" 
            href="#" 
            role="button" 
            data-bs-toggle="dropdown"  <!-- Ativa o dropdown -->
          >
            Produtos
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Eletrônicos</a></li>
            <li><a class="dropdown-item" href="#">Roupas</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

#### **Observações**  
- Use `container-fluid` para ocupar toda a largura ou `container` para largura fixa.  
- Adicione `fixed-top` ou `fixed-bottom` para fixar a navbar no topo ou fundo da tela.  

### Navbar Responsivo com Dropdown

```html
<ul class="navbar-nav ms-auto mb-2 mb-lg-0">
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      Serviços
    </a>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Web Design</a></li>
      <li><a class="dropdown-item" href="#">SEO</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="#">Suporte</a></li>
    </ul>
  </li>
</ul>
```

#### Explicação:
- **`dropdown`**: Classe para criar menus suspensos.
- **`dropdown-toggle`**: Ativa o dropdown com `data-bs-toggle="dropdown"`.
- **`dropdown-menu`**: Conteúdo do menu.
- **`dropdown-divider`**: Linha divisória visual.


### **Variações de Estilo**

#### **Cores Temáticas**
```html
<nav class="navbar navbar-dark bg-dark">...</nav>
<nav class="navbar navbar-light bg-light">...</nav>
<nav class="navbar navbar-dark bg-primary">...</nav>
```

#### **Posicionamento**
```html
<nav class="navbar fixed-top">...</nav> <!-- Fixa no topo -->
<nav class="navbar sticky-top">...</nav> <!-- "Gruda" ao rolar -->
<nav class="navbar fixed-bottom">...</nav> <!-- Fixa na base -->
```

#### **Navbar com Logo e Search**
```html
<nav class="navbar bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="logo.png" width="30" class="d-inline-block align-top">
      Marca
    </a>
    <form class="d-flex">
      <input class="form-control me-2" type="search">
      <button class="btn btn-outline-success" type="submit">Buscar</button>
    </form>
  </div>
</nav>
```

#### **Dropdown no Menu**

```html
<li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
    Produtos
  </a>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Eletrônicos</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Acessórios</a></li>
  </ul>
</li>
```

#### **Navbar com Ícones (Bootstrap Icons)**
```html
<li class="nav-item">
  <a class="nav-link" href="#">
    <i class="bi bi-cart"></i> Carrinho
  </a>
</li>
```

#### **Mega Menu (Com Grid)**
```html
<div class="dropdown-menu p-4">
  <div class="row">
    <div class="col-md-4">
      <h5>Categorias</h5>
      <!-- Links aqui -->
    </div>
    <div class="col-md-8">
      <h5>Destaques</h5>
      <!-- Conteúdo adicional -->
    </div>
  </div>
</div>
```

#### **Navbar Responsiva com Login**

**Objetivo:** Criar uma navbar que:

- Mostre logo + 4 links no desktop
- Colapse em mobile
- Inclua dropdown "Minha Conta" à direita

**Gabarito:**
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Loja Online</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Produtos</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Contato</a></li>
      </ul>
      <div class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">
          <i class="bi bi-person"></i> Minha Conta
        </a>
        <ul class="dropdown-menu dropdown-menu-end">
          <li><a class="dropdown-item" href="#">Login</a></li>
          <li><a class="dropdown-item" href="#">Registrar</a></li>
        </ul>
      </div>
    </div>
  </div>
</nav>
```

---

## :two: **Table**  

As tabelas no Bootstrap 5 são componentes essenciais para exibir dados tabulares de forma organizada e responsiva. O framework oferece classes prontas para:
- Estilização básica
- Modos escuro/claro
- Tabelas responsivas
- Efeitos hover e linhas listradas

### **Elementos-Chave**

| Componente               | Tag/Classe            | Função |
|--------------------------|-----------------------|--------|
| **Container da tabela**  | `<table class="table">` | Define a tabela estilizada |
| **Cabeçalho**            | `<thead>`             | Grupo de cabeçalhos |
| **Corpo**                | `<tbody>`             | Dados principais |
| **Rodapé**               | `<tfoot>`             | Rodapé (opcional) |
| **Células de cabeçalho** | `<th scope="...">`    | `col` ou `row` para acessibilidade |


### **Elementos/Propriedades Principais**  
- **`.table`**: Classe base.  
- **`.table-striped`**: Listras alternadas.  
- **`.table-bordered`**: Adiciona bordas.  
- **`.table-dark`**: Tema escuro para cabeçalho.  
- **`.table-success`, `.table-danger`**: Cores contextuais para linhas ou células.  


### **Tabela Simples**

```html
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Nome</th>
      <th scope="col">E-mail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>João Silva</td>
      <td>joao@exemplo.com</td>
    </tr>
  </tbody>
</table>
```


### **Estilos Pré-definidos**
```html
<table class="table table-striped">...</table> <!-- Linhas zebradas -->
<table class="table table-bordered">...</table> <!-- Bordas em todas células -->
<table class="table table-borderless">...</table> <!-- Sem bordas -->
<table class="table table-hover">...</table> <!-- Efeito hover nas linhas -->
<table class="table table-dark">...</table> <!-- Tema escuro -->
```

### **Tabela Responsiva**

Envolva a tabela em um div para rolagem horizontal em telas pequenas:
```html
<div class="table-responsive">
  <table class="table">...</table>
</div>
```

**Tamanhos específicos:**
- `table-responsive-sm` (≥576px)
- `table-responsive-md` (≥768px)
- `table-responsive-lg` (≥992px)



### **Cores Contextuais**

```html
<tr class="table-primary">...</tr> <!-- Linha azul -->
<tr class="table-success">...</tr> <!-- Linha verde -->
<td class="table-danger">...</td> <!-- Célula vermelha -->
```

### **Exemplo Prático**  
```html
<table class="table table-striped table-hover table-bordered">
  <thead class="table-dark">
    <tr>
      <th scope="col">#</th> <!-- scope="col" para acessibilidade -->
      <th scope="col">Nome</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>João</td>
      <td class="table-success">Ativo</td> <!-- Cor contextual -->
    </tr>
    <tr>
      <td>2</td>
      <td>Maria</td>
      <td class="table-warning">Pendente</td>
    </tr>
  </tbody>
</table>
```

### **Observações**  
- Use `scope="row"` ou `scope="col"` para melhorar a acessibilidade.  
- Adicione `.table-responsive` para tornar a tabela rolável em dispositivos pequenos.  

---

## :three: **Alert**  

Os **Alertas** são componentes do Bootstrap para exibir mensagens contextuais destacadas. Eles são ideais para:
- Mensagens de sucesso/erro
- Avisos importantes
- Informações temporárias
- Confirmações de ações

### **Alerta Simples**
```html
<div class="alert alert-primary" role="alert">
  Mensagem informativa importante!
</div>
```

### **Cores Contextuais Disponíveis**
| Classe               | Cor          | Uso típico                  |
|----------------------|--------------|-----------------------------|
| `.alert-primary`     | Azul         | Informação geral            |
| `.alert-secondary`   | Cinza        | Conteúdo secundário         |
| `.alert-success`     | Verde        | Ação bem-sucedida           |
| `.alert-danger`      | Vermelho     | Erro ou ação perigosa       |
| `.alert-warning`     | Amarelo      | Aviso ou atenção            |
| `.alert-info`        | Azul-claro   | Informação adicional        |
| `.alert-light`       | Branco       | Fundos escuros              |
| `.alert-dark`        | Preto        | Fundos claros               |


### **Exemplo Prático**  
```html
<div class="alert alert-info alert-dismissible fade show" role="alert">
  <strong>Novo recurso!</strong> Confira as atualizações. 
  <button 
    type="button" 
    class="btn-close" 
    data-bs-dismiss="alert"  
    aria-label="Fechar"
  ></button>
</div>
```

#### **Elementos/Propriedades Principais**  
- **`.alert`**: Classe base.  
- **`.alert-success`, `.alert-danger`**: Define a cor do alerta.  
- **`.alert-dismissible`**: Permite fechar o alerta.  
- **`.fade`/`.show`**: Adiciona animação de entrada/saída.  
- **`data-bs-dismiss="alert"`**: Vincula o botão de fechar ao alerta.  


#### **Observações**  
- Sempre inclua `role="alert"` para acessibilidade.  
- Use `aria-label` no botão de fechar para descrever sua função.  

### **Alerta com Ícone (Bootstrap Icons)**
```html
<div class="alert alert-success d-flex align-items-center" role="alert">
  <i class="bi bi-check-circle-fill me-2"></i>
  <div>Registro salvo com sucesso!</div>
</div>
```

### **Alerta Descartável**
```html
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Atenção!</strong> Esta ação não pode ser desfeita.
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>
```

### **Alerta com Conteúdo Adicional**
```html
<div class="alert alert-info">
  <h4 class="alert-heading">Novo recurso disponível!</h4>
  <p>Confira as atualizações mais recentes em nosso sistema.</p>
  <hr>
  <p class="mb-0">Atualizado em 15/06/2023</p>
</div>
```

---

## :four: **Forms**  

Os formulários são componentes essenciais para coleta de dados em aplicações web. O Bootstrap 5 oferece:
- Estilos pré-definidos para todos os elementos de formulário
- Layouts responsivos
- Validação integrada
- Componentes especializados (selects, file inputs, etc.)

### **Formulário Simples**

```html
<form>
  <div class="mb-3">
    <label for="email" class="form-label">Email</label>
    <input type="email" class="form-control" id="email">
  </div>
  
  <div class="mb-3">
    <label for="senha" class="form-label">Senha</label>
    <input type="password" class="form-control" id="senha">
  </div>
  
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

### **Elementos Principais**
| Componente            | Classe/Atributo       | Descrição |
|-----------------------|----------------------|-----------|
| **Container**         | `.mb-3` (margin-bottom) | Espaçamento entre campos |
| **Label**             | `.form-label`         | Rótulo do campo |
| **Input**             | `.form-control`       | Estiliza inputs |
| **Select**            | `.form-select`        | Estiliza dropdowns |
| **Checkbox/Radio**    | `.form-check`         | Grupo de seleção |


### **Tipos de Campos**

#### **Inputs Básicos**
```html
<input type="text" class="form-control" placeholder="Texto simples">
<input type="email" class="form-control" placeholder="Email">
<input type="password" class="form-control" placeholder="Senha">
```

#### **Textarea**
```html
<textarea class="form-control" rows="3"></textarea>
```

#### **Select Menu**
```html
<select class="form-select">
  <option selected>Selecione...</option>
  <option value="1">Opção 1</option>
  <option value="2">Opção 2</option>
</select>
```

#### **Checkboxes e Radios**
```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" id="check1">
  <label class="form-check-label" for="check1">Aceito os termos</label>
</div>

<div class="form-check">
  <input class="form-check-input" type="radio" name="radioGroup" id="radio1">
  <label class="form-check-label" for="radio1">Opção 1</label>
</div>
```

### **Exemplo Prático**  
```html
<form class="container mt-4">
  <!-- Input Simples -->
  <div class="mb-3">
    <label class="form-label">Nome:</label>
    <input type="text" class="form-control" placeholder="Digite seu nome">
  </div>

  <!-- Checkbox -->
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="termos">
    <label class="form-check-label" for="termos">Aceitar termos</label>
  </div>

  <!-- Select -->
  <div class="mb-3">
    <label class="form-label">País:</label>
    <select class="form-select">
      <option>Brasil</option>
      <option>EUA</option>
    </select>
  </div>

  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```
#### **Elementos/Propriedades Principais**  
- **`.form-control`**: Estiliza inputs, selects e textareas.  
- **`.form-label`**: Estiliza rótulos.  
- **`.mb-3`**: Margem inferior (espaçamento entre campos).  
- **`.form-check`**: Agrupa checkboxes/radios.  
- **`.is-invalid`/`.is-valid`**: Validação visual.  

#### **Observações**  
- Use `.form-select` para estilizar elementos `<select>`.  
- Adicione `.disabled` a inputs para desativá-los.  


### **Formulário em Colunas**
```html
<div class="row">
  <div class="col-md-6 mb-3">
    <label>Nome</label>
    <input type="text" class="form-control">
  </div>
  <div class="col-md-6 mb-3">
    <label>Sobrenome</label>
    <input type="text" class="form-control">
  </div>
</div>
```

### **Input Groups**
```html
<div class="input-group mb-3">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Usuário">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Valor">
  <span class="input-group-text">.00</span>
  <span class="input-group-text">R$</span>
</div>
```

### **Formulário Flutuante (Floating Labels)**
```html
<div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingInput" placeholder="Email">
  <label for="floatingInput">Email</label>
</div>
```

---

## :five: **Toasts**  

Os **Toasts** são componentes de notificação não intrusivos que fornecem feedback leve ao usuário. Eles são ideais para:
- Confirmações de ações
- Notificações de sistema
- Alertas temporários
- Mensagens de status

### **Toast Simples**
```html
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    <strong class="me-auto">Notificação</strong>
    <small>1 min atrás</small>
    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
  </div>
  <div class="toast-body">
    Sua ação foi concluída com sucesso!
  </div>
</div>
```

#### **Elementos Principais**
| Componente            | Classe/Atributo             | Descrição |
|-----------------------|----------------------------|-----------|
| **Container**         | `.toast`                   | Elemento principal |
| **Cabeçalho**         | `.toast-header`            | Área do título |
| **Corpo**             | `.toast-body`              | Conteúdo da mensagem |
| **Botão de fechar**   | `data-bs-dismiss="toast"`  | Fecha o toast |
| **Acessibilidade**    | `aria-live`, `aria-atomic` | Para leitores de tela |


#### **Elementos/Propriedades Principais**  
- **`.toast`**: Classe base.  
- **`.toast-header`/`.toast-body`**: Divide o conteúdo.  
- **`data-bs-autohide="false"`**: Desativa o fechamento automático.  
- **JavaScript**: Inicialização obrigatória via `bootstrap.Toast()`.  

#### **Ativação do Toast** - **Via JavaScript**

```javascript
// Inicializa todos os toasts da página
document.querySelectorAll('.toast').forEach(toastEl => {
  const toast = new bootstrap.Toast(toastEl)
  toast.show()
})
```

#### **Ativação do Toast** - **Via Atributos HTML**
```html
<button class="btn btn-primary" 
        data-bs-toggle="toast" 
        data-bs-target="#meuToast">
  Mostrar Toast
</button>
```


#### **Exemplo Prático**  
```html
<!-- Botão para acionar o toast -->
<button class="btn btn-warning" onclick="mostrarToast()">Notificação</button>

<!-- Toast -->
<div 
  class="toast" 
  id="toastExemplo" 
  role="alert" 
  data-bs-autohide="false"  <!-- Não fecha automaticamente -->
>
  <div class="toast-header">
    <strong class="me-auto">Sistema</strong>
    <button class="btn-close" data-bs-dismiss="toast"></button>
  </div>
  <div class="toast-body">Usuário cadastrado com sucesso!</div>
</div>

<script>
  function mostrarToast() {
    const toastEl = document.getElementById('toastExemplo');
    const toast = new bootstrap.Toast(toastEl);
    toast.show();  <!-- Exibe o toast -->
  }
</script>
```

#### **Observações**  
- Posicione o toast com classes como `.position-absolute top-0 end-0`.  
- Use `aria-live="polite"` para leitores de tela.  

---

## :six: **Spinners**  

Os **Spinners** são componentes visuais que indicam um processo de carregamento ou ação em andamento. No Bootstrap 5, eles oferecem:
- **Animações suaves** de carregamento
- **Múltiplos estilos** (borda, crescimento)
- **Tamanhos personalizáveis**
- **Cores contextuais**

### **Elementos/Propriedades Principais**  
- **`.spinner-border`**: Spinner circular.  
- **`.spinner-grow`**: Spinner com efeito de "crescimento".  
- **`.text-primary`**: Define a cor.  
- **`.spinner-border-sm`**: Tamanho pequeno.  

### **Spinner de Borda (Padrão)**
```html
<div class="spinner-border" role="status">
  <span class="visually-hidden">Carregando...</span>
</div>
```

### **Spinner de Crescimento**
```html
<div class="spinner-grow" role="status">
  <span class="visually-hidden">Carregando...</span>
</div>
```

### **Cores Contextuais**
```html
<div class="spinner-border text-primary"></div>
<div class="spinner-border text-success"></div>
<div class="spinner-border text-danger"></div>
<!-- Disponível para todas cores do Bootstrap -->
```

### **Tamanhos**
```html
<div class="spinner-border spinner-border-sm"></div> <!-- Pequeno -->
<div class="spinner-border"></div> <!-- Médio (padrão) -->
<div class="spinner-border" style="width: 3rem; height: 3rem;"></div> <!-- Grande -->
```

### **Dentro de Botões**
```html
<button class="btn btn-primary" disabled>
  <span class="spinner-border spinner-border-sm"></span>
  Processando...
</button>
```

### **Com Texto**
```html
<div class="d-flex align-items-center">
  <strong>Carregando dados...</strong>
  <div class="spinner-border ms-auto" role="status"></div>
</div>
```

### **Exemplo Prático**  
```html
<!-- Spinner Simples -->
<div class="spinner-border text-success" role="status">
  <span class="visually-hidden">Carregando...</span> <!-- Texto oculto para acessibilidade -->
</div>

<!-- Spinner em Botão -->
<button class="btn btn-primary" disabled>
  <span class="spinner-border spinner-border-sm"></span>
  Processando...
</button>
```

#### **Observações**  
- Sempre inclua `role="status"` e texto oculto (`.visually-hidden`) para acessibilidade.  


### **Spinner com Progresso**
```html
<div class="progress mb-3" style="height: 5px;">
  <div id="progressBar" class="progress-bar" role="progressbar" style="width: 0%"></div>
</div>
<div class="spinner-border text-primary"></div>
<span id="progressText">0% concluído</span>

<script>
// Simulação de progresso
let progress = 0;
const interval = setInterval(() => {
  progress += 5;
  document.getElementById('progressBar').style.width = `${progress}%`;
  document.getElementById('progressText').textContent = `${progress}% concluído`;
  if(progress >= 100) clearInterval(interval);
}, 300);
</script>
```

---

## :seven: **Progress**  

Os elementos de progresso no Bootstrap fornecem feedback visual sobre o andamento de processos. São ideais para:

- **Indicadores de carregamento**
- **Barra de conclusão de tarefas**
- **Visualização de etapas**
- **Feedback de upload/download**

### **Estrutura Fundamental**
```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 25%"></div>
</div>
```

#### **Elementos Principais**
| Componente               | Classe/Atributo          | Descrição |
|--------------------------|-------------------------|-----------|
| **Container principal**  | `.progress`             | Define a área do progresso |
| **Barra interna**        | `.progress-bar`         | Elemento que preenche |
| **Acessibilidade**       | `role="progressbar"`    | Para leitores de tela |
| **Largura**              | `style="width: X%"`     | Define porcentagem |


### **Exemplo Prático**  
```html
<div class="progress mt-3" style="height: 30px"> <!-- Altura customizada -->
  <div 
    class="progress-bar bg-success progress-bar-striped progress-bar-animated" 
    role="progressbar" 
    style="width: 75%" 
    aria-valuenow="75" 
    aria-valuemin="0" 
    aria-valuemax="100"
  >
    75%
  </div>
</div>
```

#### **Elementos/Propriedades Principais**  
- **`.progress`**: Classe base.  
- **`.progress-bar`**: Elemento que preenche a barra.  
- **`width: 45%`**: Define o progresso atual.  
- **`.bg-danger`**, **`.bg-info`**: Cores contextuais.  
- **`.progress-bar-striped`**: Efeito de listras.  
- **`.progress-bar-animated`**: Animação de movimento.  

#### **Observações**  
- Use `aria-valuenow`, `aria-valuemin` e `aria-valuemax` para acessibilidade.  
- Adicione `.progress-bar-striped` e `.progress-bar-animated` para efeitos visuais.  

### **Cores Contextuais**
```html
<div class="progress-bar bg-success" style="width: 25%"></div>
<div class="progress-bar bg-info" style="width: 50%"></div>
<div class="progress-bar bg-warning" style="width: 75%"></div>
```

### **Barras Listradas**
```html
<div class="progress-bar progress-bar-striped" style="width: 50%"></div>
```

### **Barras Animadas**
```html
<div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 75%"></div>
```

### **Múltiplas Barras**
```html
<div class="progress">
  <div class="progress-bar bg-success" style="width: 15%"></div>
  <div class="progress-bar bg-warning" style="width: 30%"></div>
  <div class="progress-bar bg-danger" style="width: 20%"></div>
</div>
```

### **Altura Customizada**
```html
<div class="progress" style="height: 30px;">
  <div class="progress-bar" style="width: 65%;"></div>
</div>
```

### **Com Rótulo de Texto**
```html
<div class="progress">
  <div class="progress-bar" style="width: 75%;">75%</div>
</div>
```

### **Atualização Progressiva**
```html
<div class="progress mb-3">
  <div id="dynamicBar" class="progress-bar" style="width: 0%">0%</div>
</div>
<button id="startBtn" class="btn btn-primary">Iniciar</button>

<script>
document.getElementById('startBtn').addEventListener('click', function() {
  const bar = document.getElementById('dynamicBar');
  let progress = 0;
  
  const interval = setInterval(() => {
    progress += 5;
    bar.style.width = `${progress}%`;
    bar.textContent = `${progress}%`;
    
    if(progress >= 100) {
      clearInterval(interval);
      bar.classList.add('bg-success');
    }
  }, 300);
});
</script>
```

### **Simulação de Upload**
```html
<div class="mb-3">
  <div class="d-flex justify-content-between">
    <span>Enviando arquivo...</span>
    <span id="uploadPercent">0%</span>
  </div>
  <div class="progress">
    <div id="uploadBar" class="progress-bar progress-bar-striped progress-bar-animated" style="width: 0%"></div>
  </div>
</div>

<script>
// Simulação de upload
function simulateUpload() {
  const bar = document.getElementById('uploadBar');
  const percent = document.getElementById('uploadPercent');
  let progress = 0;
  
  const upload = setInterval(() => {
    progress += Math.random() * 10;
    if(progress > 100) progress = 100;
    
    bar.style.width = `${progress}%`;
    percent.textContent = `${Math.round(progress)}%`;
    
    if(progress >= 100) {
      clearInterval(upload);
      bar.classList.remove('progress-bar-animated');
      bar.classList.add('bg-success');
    }
  }, 800);
}

simulateUpload();
</script>
```

---

## :eight: **Tooltips**  

Os **Tooltips** são pequenas mensagens flutuantes que aparecem quando o usuário interage com um elemento. Eles são ideais para:

- Explicar ícones ou ações
- Fornecer informações adicionais
- Mostrar texto alternativo compacto
- Guiar o usuário em interfaces complexas

### **Habilitando Tooltips**
Todos os tooltips devem ser inicializados via JavaScript:

```javascript
// Inicializa todos os tooltips da página
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(el => new bootstrap.Tooltip(el));
```

### **Estrutura Básica**
```html
<button 
  type="button" 
  class="btn btn-secondary" 
  data-bs-toggle="tooltip" 
  data-bs-placement="top" 
  title="Texto do tooltip">
  Botão com tooltip
</button>
```

### **Posicionamento**
```html
<button data-bs-placement="top">Top</button>
<button data-bs-placement="right">Right</button>
<button data-bs-placement="bottom">Bottom</button>
<button data-bs-placement="left">Left</button>
```

### **Tooltips com HTML**
```html
<button 
  data-bs-toggle="tooltip" 
  data-bs-html="true" 
  title="<em>Itálico</em> <strong>Negrito</strong> <u>Sublinhado</u>">
  Tooltip com HTML
</button>
```

### **Modos de Disparo**
```html
<button data-bs-trigger="hover">Hover (padrão)</button>
<button data-bs-trigger="click">Click</button>
<button data-bs-trigger="focus">Focus</button>
<button data-bs-trigger="manual">Manual (via JS)</button>
```

### **Exemplo Prático**  
```html
<button 
  class="btn btn-dark" 
  data-bs-toggle="tooltip" 
  data-bs-placement="right" 
  title="Clique para confirmar"
>
  Confirmar
</button>

<script>
  // Inicializar todos os tooltips na página
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltipTriggerList.forEach(t => new bootstrap.Tooltip(t));
</script>
```

#### **Elementos/Propriedades Principais**  
- **`data-bs-toggle="tooltip"`**: Ativa o tooltip.  
- **`data-bs-placement="top"`**: Define a posição (top, bottom, left, right).  
- **`title`**: Texto exibido no tooltip.  
- **JavaScript**: Inicialização obrigatória via `bootstrap.Tooltip()`.  

#### **Observações**  
- Tooltips não funcionam em dispositivos touch por padrão.  
- Personalize o estilo com CSS (ex: cor, tamanho).  

### **Exemplo 1: Tooltip em Ícone**
```html
<i 
  class="bi bi-info-circle" 
  data-bs-toggle="tooltip" 
  data-bs-placement="right" 
  title="Mais informações sobre este item">
</i>
```

### **Exemplo 2: Tooltip em Link Desabilitado**
```html
<a 
  href="#" 
  class="text-muted pe-none" 
  tabindex="-1" 
  data-bs-toggle="tooltip" 
  title="Link desabilitado temporariamente">
  Recursos indisponíveis
</a>
```

### **Exemplo 3: Tooltip com Delay**
```html
<button 
  data-bs-toggle="tooltip" 
  data-bs-delay='{"show":500, "hide":100}'
  title="Aparece após 500ms">
  Tooltip com delay
</button>
```


---

### **10. Exemplo Integrado**  
Combine todos os componentes em uma página HTML única para demonstrar funcionalidades interativas e responsividade.

---

### **Recursos Adicionais**  
1. **Documentação Oficial:** [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)  
2. **Personalização:** Use variáveis Sass para modificar cores e breakpoints.  
3. **Prática:** Crie um dashboard fictício usando todos os componentes aprendidos.