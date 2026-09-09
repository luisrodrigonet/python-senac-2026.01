# Aula 03 - Parte 5 - Bootstrap - Botões
> Utilização de Botões no Bootstrap 5 (HTML5)**  
> Botões são elementos fundamentais em interfaces web, permitindo interações como envio de formulários, navegação e ações específicas. O `Bootstrap` oferece estilos pré-definidos, responsividade e personalização via classes utilitárias. Nesta aula, exploraremos todas as possibilidades.
>
> **Objetivos:**  
> - Criar botões com variações de estilo e tamanho.  
> - Utilizar ícones em botões.  
> - Trabalhar com estados (ativo, desabilitado).  
> - Criar grupos de botões e barras de ferramentas.  
> - Personalizar botões com utilitários do Bootstrap.
> 
> ---

## :one: **Configuração Inicial**  

Inclua os arquivos do **Bootstrap 5** e ícones (**Bootstrap Icons**) via CDN no `<head>`:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
```

---

## :two: **Básico: Criando Botões**  
**Estrutura mínima:**  
```html
<button type="button" class="btn btn-primary">Primário</button>
```
- `type="button"`: Define o comportamento (pode ser `submit`, `reset` em formulários).  
- `btn`: Classe base.  
- `btn-primary`: Define a cor principal.

**Exemplo com tipos:**  
```html
<button class="btn btn-primary">Enviar</button>
<input type="submit" class="btn btn-success" value="Salvar">
<a href="#" class="btn btn-danger">Link como botão</a>
```

📙**Referências**

- [Bootstrap 4 - Buttons](https://getbootstrap.com/docs/4.0/components/buttons/)
- [Bootstrap 5 - Buttons](https://getbootstrap.com/docs/5.3/components/buttons/)

---

### 🔖 **Variações de Cores**  
Bootstrap oferece 8 variações contextuais:  

```html
<button class="btn btn-primary">Primário</button>
<button class="btn btn-secondary">Secundário</button>
<button class="btn btn-success">Sucesso</button>
<!-- Adicione 'btn-info', 'btn-warning', 'btn-danger', 'btn-light', 'btn-dark' -->
```

**Botões Outline (bordas):**  
```html
<button class="btn btn-outline-primary">Primário Outline</button>
```

---

### 🔖 **Tamanhos de Botões**  
- **Pequeno:** `btn-sm`  
- **Grande:** `btn-lg`  
- **Bloco (full-width):** `d-grid gap-2` (Bootstrap 5)  

**Exemplo:**  
```html
<button class="btn btn-primary btn-sm">Pequeno</button>
<button class="btn btn-primary btn-lg">Grande</button>
<div class="d-grid gap-2">
  <button class="btn btn-primary">Botão Bloco</button>
</div>
```

---

### 🔖**Estados do Botão**  
- **Ativo (pressionado):** `active`  
- **Desabilitado:** `disabled` (atributo HTML ou classe para links)  

**Exemplo:**  
```html
<button class="btn btn-primary active">Ativo</button>
<button class="btn btn-secondary" disabled>Desabilitado</button>
<a href="#" class="btn btn-danger disabled" aria-disabled="true">Link Desabilitado</a>
```

💡 **Dica**:  As propriedades ARIA (Accessible Rich Internet Applications) são atributos HTML que tornam o conteúdo web mais acessível, especialmente para pessoas que utilizam tecnologias assistivas (como leitores de tela). Elas fornecem informações adicionais sobre **papéis, estados, propriedades e relações** de elementos, auxiliando na interpretação de interfaces dinâmicas ou complexas.

---

### 🔖 **Ícones em Botões**  
**Usando Bootstrap Icons:**  
```html
<button class="btn btn-success">
  <i class="bi bi-check-circle"></i> Sucesso
</button>
```

**Ícones à Direita:**  
```html
<button class="btn btn-warning">
  Aviso <i class="bi bi-exclamation-triangle ms-2"></i>
</button>
```

**Apenas Ícone (botão circular):**  
```html
<button class="btn btn-danger rounded-circle p-2">
  <i class="bi bi-trash"></i>
</button>
```

📙**Referências**

- [Bootstrap - Espaçamento](https://getbootstrap.com/docs/5.0/utilities/spacing/)


---

### 🔖 **Grupos de Botões**  
**Grupo Simples:**  
```html
<div class="btn-group">
  <button class="btn btn-primary">Esquerda</button>
  <button class="btn btn-primary">Centro</button>
  <button class="btn btn-primary">Direita</button>
</div>
```

**Barra de Ferramentas:**  
```html
<div class="btn-toolbar">
  <div class="btn-group me-2">
    <button class="btn btn-secondary">1</button>
    <button class="btn btn-secondary">2</button>
  </div>
  <div class="btn-group">
    <button class="btn btn-info"><i class="bi bi-pencil"></i></button>
    <button class="btn btn-info"><i class="bi bi-trash"></i></button>
  </div>
</div>
```

---

### 🔖 **Botões Personalizados**  
**Utilizando Gradientes:**  
```html
<button class="btn btn-primary bg-gradient">Gradiente</button>
```

📙**Referências**

- [Bootstrap 5 - Background](https://getbootstrap.com/docs/5.0/utilities/background/) 
  

**Sombras e Bordas:**  
```html
<button class="btn btn-success shadow-lg rounded-pill">Pílula com Sombra</button>
```

📙**Referências**

- [Bootstrap 5.0 - Sombra](https://getbootstrap.com/docs/5.0/utilities/shadows/)
- [Bootstrap 5.0 - Badges](https://getbootstrap.com/docs/5.0/components/badge/)



**Cores Customizadas (via utilitários):**  
```html
<button class="btn text-white" style="background-color: #FF6B6B;">Customizado</button>
```

---

### 🔖 **Botões com Dropdown**  
```html
<div class="btn-group">
  <button class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
    Menu
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Opção 1</a></li>
    <li><a class="dropdown-item" href="#">Opção 2</a></li>
  </ul>
</div>
```

📙**Referências**

- [Bootstrap 5.0 - Button group](https://getbootstrap.com/docs/5.0/components/button-group/)


---

### 📚 **Considerações Finais**  
- **Acessibilidade:** Use `aria-label` em botões apenas com ícones.  
- **Responsividade:** Grupos de botões se adaptam automaticamente em dispositivos móveis.  
- **Documentação Oficial:** Consulte [Bootstrap Buttons](https://getbootstrap.com/docs/5.3/components/buttons/) para mais detalhes.

## 🎯 **Exercício Prático:**  

Crie uma barra de ferramentas com botões de edição (ícone de lápis), exclusão (ícone de lixeira) e um dropdown de opções, utilizando todas as técnicas aprendidas.

```html
<!-- Exemplo de Resposta -->
<div class="btn-toolbar mb-3">
  <div class="btn-group me-2">
    <button class="btn btn-outline-primary"><i class="bi bi-pencil"></i> Editar</button>
    <button class="btn btn-outline-danger"><i class="bi bi-trash"></i> Excluir</button>
  </div>
  <div class="btn-group">
    <button class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown">
      <i class="bi bi-gear"></i> Opções
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Exportar</a></li>
      <li><a class="dropdown-item" href="#">Importar</a></li>
    </ul>
  </div>
</div>
```

**Recursos Adicionais:**  
- [Bootstrap Icons](https://icons.getbootstrap.com/)  
- [Font Awesome](https://fontawesome.com/)