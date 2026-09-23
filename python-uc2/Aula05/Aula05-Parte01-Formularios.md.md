# Aula 05 - Parte 01 - Formulário
> Os formulários são componentes essenciais em páginas web, permitindo a interação do usuário com o sistema.
> 
> Eles são usados para coletar dados, como cadastros, pesquisas, login, entre outros.
> 
> Nesta aula, vamos explorar os principais elementos e atributos relacionados a formulários em HTML5.
> 
> --- 


## :one: **Elemento `<form>`**  

O elemento `<form>` é o container que agrupa todos os campos de um formulário. Ele possui atributos importantes que definem como os dados serão enviados:

### 📚 **Atributos do `<form>`**  

- **`action`**: Define para onde os dados do formulário serão enviados (URL do servidor).  
  ```html
  <form action="/processar-dados" method="POST"> ... </form>
  ```

- **`method`**: Especifica o método HTTP usado para enviar os dados (`GET` ou `POST`).  
  - `GET`: Os dados são enviados na URL (visíveis).  
  - `POST`: Os dados são enviados no corpo da requisição (mais seguro).  

- **`target`**: Define onde a resposta será exibida (`_self`, `_blank`, `_parent`, `_top`).  
  ```html
  <form target="_blank"> ... </form>
  ```

- **`enctype`**: Define como os dados são codificados ao enviar arquivos (`multipart/form-data`).  
  ```html
  <form enctype="multipart/form-data" method="POST"> ... </form>
  ```

---

## :two: **Elemento `<label>`**  

O `<label>` associa um texto descritivo a um campo do formulário, melhorando a acessibilidade e usabilidade.

### 📚 **Atributo `for`**  
Vincula o `label` a um campo usando o `id` do input.  
```html
<label for="nome">Nome:</label>
<input type="text" id="nome" name="nome">
```

---

## :three: **Elementos `<input>`**  
Os `<input>` são os campos onde os usuários inserem dados. O atributo `type` define o tipo de dado esperado.

### 📚 **Tipos de `<input>`**  
- **`text`**: Campo de texto simples.  
- **`email`**: Valida se o valor é um e-mail válido.  
- **`number`**: Aceita apenas números.  
- **`tel`**: Campo para telefone.  
- **`password`**: Oculta o texto digitado.  
- **`date`**: Seleciona uma data.  
- **`checkbox`**: Caixa de seleção múltipla.  
- **`radio`**: Botão de seleção única.  
- **`file`**: Upload de arquivos.  

### 📚 **Atributos dos `<input>`**  
- **`name`**: Identifica o campo ao enviar dados para o servidor.  
- **`id`**: Identificador único (usado com `<label for>`).  
- **`class`**: Define classes CSS para estilização.  
- **`placeholder`**: Texto de exemplo dentro do campo.  
- **`value`**: Valor padrão do campo.  
- **`required`**: Campo obrigatório.  
- **`readonly`**: Campo apenas para leitura (não editável).  
- **`pattern`**: Define uma expressão regular para validação.  
- **`title`**: Mensagem de ajuda ao passar o mouse.  

#### 📖 **Exemplo:**  
```html
<input 
  type="email" 
  id="email" 
  name="email" 
  placeholder="Digite seu e-mail" 
  required 
  pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" 
  title="Exemplo: usuario@dominio.com"
>
```

---

## :four: **Elemento `<button>`**  
Define um botão que pode enviar o formulário (`type="submit"`) ou executar ações JavaScript (`type="button"`).

### 📚 **Tipos de `<button>`**  
- **`submit`**: Envia o formulário (padrão).  
- **`reset`**: Limpa os campos.  
- **`button`**: Botão genérico (usado com JavaScript).  

#### 📖 **Exemplo:**  
```html
<button type="submit">Enviar</button>
<button type="reset">Limpar</button>
<button type="button">Ação Customizada</button>
```

---

## 🎯 **Exemplo Completo**  
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Formulário de Cadastro</title>
</head>
<body>
  <form action="/cadastro" method="POST" target="_blank">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required placeholder="Seu nome completo">

    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email" required placeholder="exemplo@email.com">

    <label for="telefone">Telefone:</label>
    <input type="tel" id="telefone" name="telefone" pattern="[0-9]{11}" title="DDD + Número (apenas dígitos)">

    <label for="senha">Senha:</label>
    <input type="password" id="senha" name="senha" required minlength="6">

    <button type="submit">Cadastrar</button>
    <button type="reset">Limpar</button>
  </form>
</body>
</html>
```

---

## 🎯 **Atividade Sugerida**  
**Atividade Sugerida:** Crie um formulário de contato com validação de e-mail, telefone e campo obrigatório para nome.


🌐 **Código HTML do Formulário de Contato**  

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formulário de Contato</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    form {
      background: #f9f9f9;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background: #45a049;
    }
    .error {
      color: red;
      font-size: 12px;
      margin-top: -10px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>Formulário de Contato</h1>
  <form action="/enviar-contato" method="POST">
    <!-- Campo Nome (Obrigatório) -->
    <label for="nome">Nome*:</label>
    <input 
      type="text" 
      id="nome" 
      name="nome" 
      required 
      placeholder="Digite seu nome completo"
    >

    <!-- Campo E-mail (Validação HTML5) -->
    <label for="email">E-mail*:</label>
    <input 
      type="email" 
      id="email" 
      name="email" 
      required 
      placeholder="exemplo@email.com"
      pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
      title="Digite um e-mail válido (exemplo: usuario@dominio.com)"
    >

    <!-- Campo Telefone (Validação com Regex) -->
    <label for="telefone">Telefone*:</label>
    <input 
      type="tel" 
      id="telefone" 
      name="telefone" 
      required 
      placeholder="(XX) XXXXX-XXXX"
      pattern="\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}"
      title="Formato: (XX) XXXXX-XXXX"
    >

    <!-- Campo Mensagem -->
    <label for="mensagem">Mensagem:</label>
    <textarea 
      id="mensagem" 
      name="mensagem" 
      rows="5" 
      placeholder="Digite sua mensagem..."
    ></textarea>

    <!-- Botões -->
    <button type="submit">Enviar</button>
    <button type="reset">Limpar</button>
  </form>
</body>
</html>
```

---

✨ **Explicação das Validações**  

1. Validação de Nome (Obrigatório)  
- O atributo `required` garante que o campo não seja enviado vazio.  
- O `placeholder` ajuda o usuário a entender o formato esperado.  

2. Validação de E-mail 
- `type="email"` já faz uma validação básica.  
- `pattern` e `title` reforçam a validação com uma **expressão regular** (`[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$`).  

3. Validação de Telefone  
- `type="tel"` ajuda dispositivos móveis a exibir um teclado numérico.  
- `pattern="\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}"` garante o formato `(XX) XXXXX-XXXX`.  
- `title` exibe uma mensagem de ajuda se o formato estiver incorreto.  

4. Estilização Básica
- CSS simples para melhorar a aparência do formulário.  
- Botões estilizados para melhor interação.  

---

