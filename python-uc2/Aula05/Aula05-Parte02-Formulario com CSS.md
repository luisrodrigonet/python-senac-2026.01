# Aula 05 - Parte 02 - Formulários em HTML5 e CSS  
> 
> Os formulários são componentes essenciais em páginas web, permitindo a interação do usuário com o sistema.
> Nesta aula, vamos explorar:  
> ✅ **Elementos HTML5** (`<form>`, `<input>`, `<label>`, `<button>`)  
> ✅ **Atributos importantes** (`required`, `pattern`, `placeholder`, etc.)  
> ✅ **Estilização com CSS** para melhorar a aparência e usabilidade  
> 
> ---

## 📚 **Elemento `<form>`**  
Define o container do formulário e como os dados serão enviados.  

**Atributos principais:**  
| Atributo   | Função                                                                 |
|------------|-----------------------------------------------------------------------|
| `action`   | URL para onde os dados serão enviados.                                |
| `method`   | Método HTTP (`GET` ou `POST`).                                       |
| `target`   | Define onde a resposta será aberta (`_blank`, `_self`, etc.).         |
| `enctype`  | Codificação dos dados (importante para upload de arquivos).           |

**Exemplo:**  
```html
<form action="/enviar-dados" method="POST" target="_blank" enctype="multipart/form-data">
  <!-- Campos do formulário aqui -->
</form>
```

---

## 📚 **Elementos do Formulário**  

### 🔖 **`<label>`**  
Melhora a acessibilidade e usabilidade, associando texto a um campo.  
```html
<label for="nome">Nome completo:</label>
<input type="text" id="nome" name="nome">
```

### 🔖 **`<input>`**  
Campos para entrada de dados. Principais tipos:  

| Tipo           | Uso                              | Exemplo                          |
|----------------|----------------------------------|----------------------------------|
| `text`         | Texto livre                      | `<input type="text" name="nome">`|
| `email`        | Valida formato de e-mail         | `<input type="email">`           |
| `password`     | Oculta caracteres digitados      | `<input type="password">`        |
| `tel`          | Telefone (útil em mobile)        | `<input type="tel">`             |
| `number`       | Aceita apenas números            | `<input type="number">`          |
| `date`         | Selecionador de data             | `<input type="date">`            |
| `checkbox`     | Caixa de seleção múltipla        | `<input type="checkbox">`        |
| `radio`        | Seleção única                    | `<input type="radio">`           |
| `file`         | Upload de arquivos               | `<input type="file">`            |

**Atributos comuns:**  
- `required` (obrigatório)  
- `placeholder` (texto de exemplo)  
- `pattern` (validação com regex)  
- `readonly` (apenas leitura)  

**Exemplo com validação:**  
```html
<input 
  type="email" 
  id="email" 
  name="email" 
  required 
  placeholder="exemplo@email.com" 
  pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
>
```

### 🔖 **`<button>`**  
Define ações no formulário.  

| Tipo         | Função                                      |
|--------------|--------------------------------------------|
| `submit`     | Envia o formulário (padrão)                |
| `reset`      | Limpa todos os campos                      |
| `button`     | Ação personalizada (usado com JavaScript)  |

**Exemplo:**  
```html
<button type="submit">Enviar</button>
<button type="reset">Limpar</button>
```

---

## 📚 **Estilização com CSS**  
Vamos melhorar a aparência do formulário com CSS.  

### 🔖 **Estilização Básica**  
```css
/* Reset básico para melhor consistência */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background-color: #f4f4f9;
  padding: 20px;
}

form {
  background: #fff;
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Estilo para labels */
label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
  color: #333;
}

/* Estilo para inputs e textarea */
input[type="text"],
input[type="email"],
input[type="tel"],
input[type="password"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

/* Foco nos campos */
input:focus,
textarea:focus {
  border-color: #4CAF50;
  outline: none;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

/* Estilo para botões */
button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-right: 10px;
}

button:hover {
  background-color: #45a049;
}

/* Mensagens de erro (opcional) */
input:invalid {
  border-color: #ff4444;
}

.error-message {
  color: #ff4444;
  font-size: 14px;
  margin-top: -10px;
  margin-bottom: 10px;
}
```

### 🔖 **Formulário Estilizado**  
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formulário Estilizado</title>
  <link rel="stylesheet" href="estilos.css">
</head>
<body>
  <form action="/contato" method="POST">
    <h2>Formulário de Contato</h2>
    
    <label for="nome">Nome*</label>
    <input type="text" id="nome" name="nome" required placeholder="Seu nome completo">
    
    <label for="email">E-mail*</label>
    <input type="email" id="email" name="email" required placeholder="exemplo@email.com">
    
    <label for="telefone">Telefone</label>
    <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000">
    
    <label for="mensagem">Mensagem</label>
    <textarea id="mensagem" name="mensagem" rows="5" placeholder="Digite sua mensagem..."></textarea>
    
    <button type="submit">Enviar</button>
    <button type="reset">Limpar</button>
  </form>
</body>
</html>
```

---

## :books: **Melhorias Avançadas (Opcional)**  

### 🔖 **Validação Personalizada com JavaScript**  
```javascript
document.querySelector('form').addEventListener('submit', function(e) {
  const telefone = document.getElementById('telefone').value;
  
  if (telefone && !/^\(\d{2}\) \d{5}-\d{4}$/.test(telefone)) {
    alert('Telefone no formato inválido! Use (XX) XXXXX-XXXX');
    e.preventDefault(); // Impede o envio
  }
});
```

### 🔖 **Responsividade (Media Queries)**  
```css
@media (max-width: 600px) {
  form {
    padding: 15px;
  }
  
  input, textarea {
    padding: 8px;
  }
}
```

---
## 🚀 **Prática sugerida:**  
Crie um formulário de cadastro com:  
- Validação de CPF (usando `pattern`).  
- Estilização moderna com CSS Flexbox/Grid.  
- Efeitos de hover nos botões.  

### 🌐 **Código Completo**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formulário de Cadastro</title>
  <style>
    /* Reset e Estilos Globais */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    body {
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    
    /* Container do Formulário */
    .form-container {
      background: white;
      width: 100%;
      max-width: 600px;
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
    }
    
    .form-container:hover {
      transform: translateY(-5px);
    }
    
    /* Cabeçalho */
    .form-header {
      text-align: center;
      margin-bottom: 30px;
    }
    
    .form-header h1 {
      color: #2c3e50;
      font-size: 28px;
      margin-bottom: 10px;
    }
    
    .form-header p {
      color: #7f8c8d;
    }
    
    /* Grid Layout */
    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    
    /* Estilos dos Campos */
    .form-group {
      margin-bottom: 20px;
      grid-column: span 1;
    }
    
    .full-width {
      grid-column: span 2;
    }
    
    label {
      display: block;
      margin-bottom: 8px;
      color: #2c3e50;
      font-weight: 600;
    }
    
    input, select {
      width: 100%;
      padding: 12px 15px;
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      font-size: 16px;
      transition: all 0.3s;
    }
    
    input:focus, select:focus {
      border-color: #3498db;
      box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
      outline: none;
    }
    
    /* Validação */
    input:invalid {
      border-color: #e74c3c;
    }
    
    input:valid {
      border-color: #2ecc71;
    }
    
    /* CPF Field */
    #cpf {
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="%237f8c8d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>');
      background-repeat: no-repeat;
      background-position: right 15px center;
      background-size: 20px;
    }
    
    /* Botões */
    .button-group {
      grid-column: span 2;
      display: flex;
      justify-content: space-between;
      margin-top: 20px;
    }
    
    button {
      flex: 1;
      padding: 15px;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s;
    }
    
    button[type="submit"] {
      background: #3498db;
      color: white;
      margin-right: 10px;
    }
    
    button[type="submit"]:hover {
      background: #2980b9;
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(41, 128, 185, 0.3);
    }
    
    button[type="reset"] {
      background: #e0e0e0;
      color: #2c3e50;
    }
    
    button[type="reset"]:hover {
      background: #bdc3c7;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
      .form-grid {
        grid-template-columns: 1fr;
      }
      
      .form-group, .full-width, .button-group {
        grid-column: span 1;
      }
      
      .button-group {
        flex-direction: column;
      }
      
      button[type="submit"] {
        margin-right: 0;
        margin-bottom: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="form-container">
    <div class="form-header">
      <h1>Crie sua conta</h1>
      <p>Preencha os campos abaixo para se cadastrar</p>
    </div>
    
    <form action="/cadastro" method="POST" class="form-grid">
      <!-- Nome Completo -->
      <div class="form-group">
        <label for="nome">Nome Completo*</label>
        <input type="text" id="nome" name="nome" required placeholder="Digite seu nome completo">
      </div>
      
      <!-- E-mail -->
      <div class="form-group">
        <label for="email">E-mail*</label>
        <input type="email" id="email" name="email" required placeholder="seu@email.com">
      </div>
      
      <!-- CPF -->
      <div class="form-group">
        <label for="cpf">CPF*</label>
        <input type="text" id="cpf" name="cpf" required 
               pattern="\d{3}\.\d{3}\.\d{3}-\d{2}" 
               placeholder="000.000.000-00"
               title="Digite um CPF no formato 000.000.000-00">
      </div>
      
      <!-- Telefone -->
      <div class="form-group">
        <label for="telefone">Telefone</label>
        <input type="tel" id="telefone" name="telefone" 
               pattern="\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}" 
               placeholder="(00) 00000-0000">
      </div>
      
      <!-- Senha -->
      <div class="form-group full-width">
        <label for="senha">Senha*</label>
        <input type="password" id="senha" name="senha" required 
               minlength="8" placeholder="Mínimo 8 caracteres">
      </div>
      
      <!-- Confirmação de Senha -->
      <div class="form-group full-width">
        <label for="confirmar-senha">Confirmar Senha*</label>
        <input type="password" id="confirmar-senha" name="confirmar-senha" required 
               placeholder="Digite novamente sua senha">
      </div>
      
      <!-- Botões -->
      <div class="button-group">
        <button type="submit">Cadastrar</button>
        <button type="reset">Limpar</button>
      </div>
    </form>
  </div>

  <script>
    // Validação de CPF
    document.getElementById('cpf').addEventListener('input', function(e) {
      let value = e.target.value.replace(/\D/g, '');
      
      if (value.length > 3) {
        value = value.substring(0,3) + '.' + value.substring(3);
      }
      if (value.length > 7) {
        value = value.substring(0,7) + '.' + value.substring(7);
      }
      if (value.length > 11) {
        value = value.substring(0,11) + '-' + value.substring(11,13);
      }
      
      e.target.value = value;
    });
    
    // Validação de confirmação de senha
    document.querySelector('form').addEventListener('submit', function(e) {
      const senha = document.getElementById('senha').value;
      const confirmarSenha = document.getElementById('confirmar-senha').value;
      
      if (senha !== confirmarSenha) {
        alert('As senhas não coincidem!');
        e.preventDefault();
      }
    });
  </script>
</body>
</html>
```

### 🎯 **Principais Recursos Implementados**

1. **Validação Avançada**
   - CPF com máscara automática (formato 000.000.000-00)
   - Confirmação de senha com JavaScript
   - Validação HTML5 para e-mail, telefone e campos obrigatórios

2. **Estilização Moderna**
   - Layout em Grid CSS para organização responsiva
   - Efeitos hover e transições suaves
   - Ícone de telefone no campo CPF
   - Feedback visual para campos válidos/inválidos

3. **Responsividade**
   - Adaptação para mobile (mudança para layout de coluna única)
   - Botões que se ajustam em diferentes tamanhos de tela

4. **Interatividade**
   - Efeito de elevação no hover do formulário
   - Botões com efeitos de hover
   - Foco visual nos campos ativos

5. **Design Atual**
   - Gradiente sutil no background
   - Sombras e bordas arredondadas
   - Tipografia moderna

### 🎲 **Como Testar**

1. Tente enviar o formulário sem preencher os campos obrigatórios
2. Teste formatos inválidos de CPF, e-mail e telefone
3. Digite senhas diferentes nos campos de senha e confirmação
4. Redimensione a janela para ver o layout responsivo
5. Passe o mouse sobre os elementos para ver os efeitos interativos
