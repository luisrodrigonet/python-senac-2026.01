# Aula 05 - Parte 3 - Formulários com Bootstrap

> Nesta aula estudaremos os fundamentos de criação de formulários utilizando o Bootstrap, abordando elementos como `<form>`, `<label>`, `<input>`, e `<button>`, além de suas propriedades e atributos essenciais.  
>
> ---  

## 📚 **Introdução aos Formulários**  
Formulários são componentes essenciais em aplicações web, permitindo a interação do usuário com o sistema. O Bootstrap oferece estilos e componentes prontos para facilitar a criação de formulários responsivos e acessíveis.  

### 🔖 **Estrutura Básica de um `<form>`**  
```html
<form action="/processar-dados" method="POST" enctype="multipart/form-data" target="_blank">
  <!-- Campos do formulário aqui -->
</form>
```  

### 🔖 **Atributos do `<form>`**  
- **`action`**: Define a URL para onde os dados serão enviados.  
- **`method`**: Especifica o método HTTP (`GET` ou `POST`).  
  - `GET`: Envia dados pela URL (visível).  
  - `POST`: Envia dados no corpo da requisição (mais seguro).  
- **`enctype`**: Define como os dados são codificados:  
  - `application/x-www-form-urlencoded` (padrão para textos).  
  - `multipart/form-data` (usado para upload de arquivos).  
- **`target`**: Define onde a resposta será exibida (`_blank`, `_self`, `_parent`, `_top`).  

---  

## 📚 **Elementos do Formulário**  

### 🔖 **`<label>`**  
Associa um texto descritivo a um campo (`<input>`).  
```html
<label for="nome">Nome:</label>
<input type="text" id="nome" name="nome">
```  
- **`for`**: Deve corresponder ao `id` do `<input>`.  

### 🔖 **`<input>`**  
Campos de entrada de dados com diversos tipos:  

#### **Tipos de `<input>`**  
| Tipo (`type`) | Descrição | Exemplo |
|--------------|-----------|---------|
| `text` | Campo de texto simples | `<input type="text">` |
| `email` | Valida se o valor é um e-mail | `<input type="email">` |
| `number` | Aceita apenas números | `<input type="number">` |
| `tel` | Campo para telefone | `<input type="tel">` |
| `password` | Esconde o texto digitado | `<input type="password">` |
| `date` | Seleciona data | `<input type="date">` |
| `file` | Upload de arquivo | `<input type="file">` |
| `checkbox` | Caixa de seleção | `<input type="checkbox">` |
| `radio` | Botão de opção única | `<input type="radio">` |

#### 🔖 **Atributos do `<input>`**  
| Atributo | Descrição | Exemplo |
|----------|-----------|---------|
| `name` | Identifica o campo no envio do formulário | `name="usuario"` |
| `id` | Identificador único (relacionado ao `<label for="">`) | `id="email"` |
| `class` | Classes CSS (Bootstrap usa `form-control`) | `class="form-control"` |
| `placeholder` | Texto de exemplo dentro do campo | `placeholder="Digite seu nome"` |
| `required` | Campo obrigatório | `required` |
| `readonly` | Campo apenas para leitura | `readonly` |
| `value` | Valor padrão do campo | `value="admin"` |
| `pattern` | Define uma regex para validação | `pattern="[A-Za-z]{3}"` |
| `title` | Mensagem de ajuda (usado com `pattern`) | `title="3 letras apenas"` |

---  

## 📚 **Estilização com Bootstrap**  
O Bootstrap fornece classes prontas para melhorar a aparência e usabilidade:  

### 🔖 **Formulário Básico**  
```html
<form>
  <div class="mb-3">
    <label for="email" class="form-label">E-mail:</label>
    <input type="email" class="form-control" id="email" name="email" required>
  </div>
  <div class="mb-3">
    <label for="senha" class="form-label">Senha:</label>
    <input type="password" class="form-control" id="senha" name="senha" required>
  </div>
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```  

### 🔖 **Classes Úteis**  
- `form-control`: Estiliza inputs.  
- `form-label`: Estiliza labels.  
- `mb-3`: Margem inferior (spacing utility).  
- `btn btn-primary`: Estiliza botões.  

---  

## 📚 **Botões (`<button>`)**
Botões podem ter diferentes funções em um formulário:  

### **Tipos de Botão**  
```html
<button type="submit" class="btn btn-primary">Enviar</button>
<button type="reset" class="btn btn-secondary">Limpar</button>
<button type="button" class="btn btn-danger">Cancelar</button>
```  

- **`submit`**: Envia o formulário.  
- **`reset`**: Limpa os campos.  
- **`button`**: Ação personalizada (JavaScript).  

---  

## 📚 **Validação de Formulários**  
O Bootstrap suporta validação HTML5 e estilização de erros:  

### **Exemplo com Validação**  
```html
<form class="was-validated">
  <div class="mb-3">
    <label for="nome" class="form-label">Nome:</label>
    <input type="text" class="form-control" id="nome" required>
    <div class="invalid-feedback">Preencha este campo.</div>
  </div>
  <button type="submit" class="btn btn-success">Validar</button>
</form>
```  

---  

## 📚 **Exercício Prático**  
Crie um formulário de cadastro com:  
- Nome (obrigatório)  
- E-mail (validado)  
- Telefone (apenas números)  
- Botão de envio e reset  

**Exemplo de Resposta:**  
```html
<form>
  <div class="mb-3">
    <label for="nome" class="form-label">Nome:</label>
    <input type="text" class="form-control" id="nome" required>
  </div>
  <div class="mb-3">
    <label for="email" class="form-label">E-mail:</label>
    <input type="email" class="form-control" id="email" required>
  </div>
  <div class="mb-3">
    <label for="telefone" class="form-label">Telefone:</label>
    <input type="tel" class="form-control" id="telefone" pattern="[0-9]{11}" title="11 dígitos">
  </div>
  <button type="submit" class="btn btn-primary">Cadastrar</button>
  <button type="reset" class="btn btn-secondary">Limpar</button>
</form>
```  
