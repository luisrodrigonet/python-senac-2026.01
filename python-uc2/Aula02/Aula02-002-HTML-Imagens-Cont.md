# Aula 02 - HTML5 - Imagens II
> 
> Nesta aula será demonstrada a inserção de imagens dentro de um HTML. Explorando desde a inserção básica até práticas avançadas de acessibilidade e otimização
> 

---

## :one: **Preload de Imagens com `<link rel="preload">`**

O HTML5 permite carregar imagens antecipadamente para melhorar o desempenho.

### **Sintaxe**
```html
<link rel="preload" href="imagem-importante.jpg" as="image">
```

### **Exemplo Prático**
```html
<head>
    <link rel="preload" href="banner.jpg" as="image">
</head>
<body>
    <img src="banner.jpg" alt="Banner principal">
</body>
```

## :two: **Lazy Loading com `loading="lazy"`**

O atributo `loading="lazy"` carrega imagens apenas quando elas entram no campo de visão do usuário, economizando recursos.

### **Sintaxe**
```html
<img src="imagem.jpg" alt="Imagem com lazy loading" loading="lazy">
```

### **Exemplo Prático**
```html
<img src="paisagem.jpg" alt="Paisagem" loading="lazy" width="800" height="600">
```

## :three: **Imagens de Fundo com CSS e `object-fit`**

Embora não seja exclusivo do HTML5, o CSS oferece propriedades complementares para controlar imagens.

### **Propriedade `object-fit`**
Define como a imagem deve se ajustar ao seu contêiner.
```css
img {
    width: 100%;
    height: 300px;
    object-fit: cover; /* Outras opções: contain, fill, scale-down */
}
```

A propriedade `object-fit` pode assumir um dos seguintes valores:

- **fill** – Este é o valor padrão. A imagem é redimensionada para preencher as dimensões especificadas. Se necessário, a imagem será esticada ou comprimida para se ajustar.  

- **contain** – A imagem mantém sua proporção original, mas é redimensionada para caber dentro das dimensões especificadas.  

- **cover** – A imagem mantém sua proporção original e preenche completamente as dimensões especificadas. A imagem será cortada para se ajustar.  

- **none** – A imagem não é redimensionada.  

- **scale-down** – A imagem é redimensionada para a menor versão possível entre os valores `none` e `contain`.  



**Exemplo Prático**
```html
<div style="width: 300px; height: 200px; overflow: hidden;">
    <img src="foto.jpg" alt="Foto" style="width: 100%; height: 100%; object-fit: cover;">
</div>
```

**Referência**:

- [CSS The object-fit Property](https://www.w3schools.com/css/css3_object-fit.asp)


## :four: **Uso de Picture e Source para Múltiplos Formatos**

A tag `<picture>` permite fornecer diferentes formatos de imagem para navegadores compatíveis.

### **Estrutura**
```html
<picture>
    <source srcset="imagem.webp" type="image/webp">
    <source srcset="imagem.jpg" type="image/jpeg">
    <img src="imagem.jpg" alt="Imagem fallback">
</picture>
```

### **Exemplo Prático**
```html
<picture>
    <source srcset="logo.webp" type="image/webp">
    <source srcset="logo.png" type="image/png">
    <img src="logo.png" alt="Logo da empresa">
</picture>
```