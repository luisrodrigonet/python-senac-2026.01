# Aula 05 - Parte 04 - Formulário de Cadastro
>  **Objetivo:** Criar uma página de cadastro de usuários responsiva, utilizando **HTML5**, **CSS3** e **Bootstrap 5**, seguindo as melhores práticas de formulários web.
>
>  ---

**Requisitos Técnicos**  
✔ **HTML5** (semântica, elementos modernos)  
✔ **CSS3** (personalização além do Bootstrap)  
✔ **Bootstrap 5.3+** (formulários, grids, responsividade)  
✔ **Validação de campos** (HTML5 e Bootstrap)  
✔ **Design responsivo** (mobile, tablet, desktop)  

---

## **Passo a Passo**  

### :books: **Estrutura Básica (HTML5)**  
Crie um arquivo `cadastro.html` com a seguinte estrutura:  

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cadastro - Loja de Tênis</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- CSS Personalizado -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container py-5">
    <h1 class="text-center mb-4">Cadastre-se na Loja de Tênis</h1>
    <form id="form-cadastro" class="needs-validation" novalidate>
      <!-- Campos do formulário aqui -->
    </form>
  </div>
  <!-- Bootstrap JS + Validação -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
```

---

### :books: **Formulário de Cadastro (Bootstrap 5)**  
Dentro do `<form>`, adicione os campos:  

```html
<div class="row g-3">
  <!-- Nome Completo -->
  <div class="col-md-6">
    <label for="nome" class="form-label">Nome Completo*</label>
    <input type="text" class="form-control" id="nome" name="nome" required>
    <div class="invalid-feedback">Por favor, insira seu nome.</div>
  </div>

  <!-- E-mail -->
  <div class="col-md-6">
    <label for="email" class="form-label">E-mail*</label>
    <input type="email" class="form-control" id="email" name="email" required>
    <div class="invalid-feedback">Insira um e-mail válido.</div>
  </div>

  <!-- Senha -->
  <div class="col-md-6">
    <label for="senha" class="form-label">Senha*</label>
    <input type="password" class="form-control" id="senha" name="senha" minlength="6" required>
    <div class="invalid-feedback">Mínimo 6 caracteres.</div>
  </div>

  <!-- Confirmação de Senha -->
  <div class="col-md-6">
    <label for="confirmar-senha" class="form-label">Confirmar Senha*</label>
    <input type="password" class="form-control" id="confirmar-senha" required>
    <div class="invalid-feedback">As senhas não coincidem.</div>
  </div>

  <!-- Telefone -->
  <div class="col-md-6">
    <label for="telefone" class="form-label">Telefone*</label>
    <input type="tel" class="form-control" id="telefone" name="telefone" pattern="[0-9]{11}" required>
    <div class="invalid-feedback">Insira um telefone válido (DDD + número).</div>
  </div>

  <!-- Data de Nascimento -->
  <div class="col-md-6">
    <label for="nascimento" class="form-label">Data de Nascimento</label>
    <input type="date" class="form-control" id="nascimento" name="nascimento">
  </div>

  <!-- Gênero (Radio Buttons) -->
  <div class="col-12">
    <label class="form-label">Gênero</label>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="genero" id="masculino" value="masculino">
      <label class="form-check-label" for="masculino">Masculino</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="genero" id="feminino" value="feminino">
      <label class="form-check-label" for="feminino">Feminino</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="genero" id="outro" value="outro">
      <label class="form-check-label" for="outro">Outro</label>
    </div>
  </div>

  <!-- Termos de Aceite -->
  <div class="col-12">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="termos" required>
      <label class="form-check-label" for="termos">Aceito os termos de uso*</label>
      <div class="invalid-feedback">Você deve aceitar os termos.</div>
    </div>
  </div>

  <!-- Botão de Envio -->
  <div class="col-12">
    <button class="btn btn-primary w-100 py-2" type="submit">Cadastrar</button>
  </div>
</div>
```

---

### :books: **Estilização Personalizada (CSS3)**  
No arquivo `styles.css`, adicione:  

```css
body {
  background-color: #f8f9fa;
}

.container {
  max-width: 800px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #0d6efd;
  font-weight: bold;
}

.btn-primary {
  background-color: #0d6efd;
  border: none;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #0b5ed7;
}

/* Validação personalizada */
.was-validated .form-control:invalid,
.was-validated .form-control:valid {
  background-position: right calc(0.375em + 0.1875rem) center;
}
```

---

### :books: **Validação com JavaScript (script.js)**  
Adicione validação para confirmar senha:  

```javascript
document.getElementById('form-cadastro').addEventListener('submit', function(event) {
  const senha = document.getElementById('senha').value;
  const confirmarSenha = document.getElementById('confirmar-senha').value;

  if (senha !== confirmarSenha) {
    document.getElementById('confirmar-senha').setCustomValidity('As senhas não coincidem');
    event.preventDefault();
    event.stopPropagation();
  } else {
    document.getElementById('confirmar-senha').setCustomValidity('');
  }

  this.classList.add('was-validated');
});
```






