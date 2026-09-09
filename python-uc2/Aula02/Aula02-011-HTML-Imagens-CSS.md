# Aula 02 - HTML5 - CSS - Imagens
> 
> Nesta aula será demonstrada a inserção de imagens dentro de um HTML. Explorando desde a inserção básica até práticas avançadas de acessibilidade e otimização
> 
> Serão apresentadas dicas de boa prática e acessibilidade, como o `alt`, utilizando apenas o `Width` e o `Height` dentro do HTML.
>
> Além disso, discutiremos as principais propriedades e técnicas do CSS para manipular imagens, com exemplos práticos e melhores práticas. 

---

## :one:  **Controle de Dimensões e Posicionamento**  

- **`width` e `height`**: Definem o tamanho da imagem.  
  ```css
  img {
    width: 300px;
    height: auto; /* Mantém a proporção */
    aspect-ratio: 16/9; /* Mantém proporção automática */
  }
  ```  
  **Melhor prática**: Use `height: auto` para evitar distorções .  

- **`object-fit`**: Controla como a imagem se ajusta ao contêiner.  
  ```css
  img {
    object-fit: cover; /* Recorta a imagem para preencher o espaço */
    object-position: 50% 25%; /* Posiciona o foco na parte superior  */
    width: 100%;
    height: 300px;
  }
  ```  
  
  Opções: `fill`, `contain`, `cover`, `none`, `scale-down` .  

---

## :two:  **Efeitos Visuais** 

A propriedade `filter` permite aplicar efeitos como:  

- **`grayscale()`**: Converte a imagem para tons de cinza.  
  ```css
  img {
    filter: grayscale(50%); /* 50% de cinza */
  }
  ```  

- **`brightness()`**: Ajusta o brilho.  
  ```css
  img:hover {
    filter: brightness(120%); /* Brilho aumentado no hover */
  }
  ```  

- **Combinações**:  
  ```css
  filter: sepia(30%) contrast(150%);
  ```  

- **`blur()`, `brightness()`, `contrast()`**:  
  ```css
  img:hover {
    filter: blur(2px) brightness(120%); /* Efeito de desfoque e brilho  */
  }
  ```  
- **Combinações avançadas**:  
  ```css
  filter: sepia(30%) drop-shadow(2px 2px 4px rgba(0,0,0,0.5));
  ```  

---

## :three:  **Máscaras com `mask-image`**  

Use imagens ou gradientes para criar máscaras:  

```css
img {
  mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));
}
```  

Isso cria um efeito de fade na parte inferior da imagem.

---

## :four:  **Recorte de Imagens com `clip-path`**  

Define a área visível da imagem:  

```css
img {
  clip-path: polygon(50% 0%, 100% 100%, 0% 100%); /* Forma triangular */
}
```  

```css
img {
    clip-path: circle(50%); /* Recorte circular  */
}
```  


**DICA**: Ferramentas como [Clippy](https://bennettfeely.com/clippy/) ajudam a gerar paths.


---

## :five:  **Imagens Responsivas**  


- **`background-*` properties**:  

  ```css
  .container {
    background-image: url("imagem.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  ```  

- **`srcset` e `sizes`**: Carrega imagens adequadas ao dispositivo.  
  ```html
  <img src="imagem.jpg"
       srcset="imagem-320.jpg 320w, imagem-640.jpg 640w"
       sizes="(max-width: 600px) 320px, 640px">
  ```  
  
  
- **`<picture>`**: Para art direction (ex.: imagens diferentes em telas pequenas).  
  ```html
  <picture>
    <source media="(max-width: 600px)" srcset="mobile.jpg">
    <img src="desktop.jpg">
  </picture>
  ```  

---

## :six:  **Efeitos de Hover e Animações**  

- **Transições suaves**:  
  ```css
  img {
    transition: transform 0.3s ease;
  }
  img:hover {
    transform: scale(1.1);
  }
  ```  
- **Efeito de zoom com `object-position`**:  
  ```css
  img:hover {
    object-position: 50% 25%; /* Move o foco para cima */
  }
  ```  

---

## :seven:  **Melhores Práticas**  

- **Otimização**: Use formatos modernos como WebP e comprima imagens.  

- **Acessibilidade**: Adicione `alt` descritivo e evite substituir texto por imagens .  

- **Performance**: Prefira CSS para efeitos em vez de imagens estáticas editadas.  

---

## :eight:  **Exemplo: HTML + CSS**  
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .imagem-estilizada {
      width: 400px;
      object-fit: cover;
      filter: grayscale(20%) contrast(120%);
      transition: transform 0.3s;
    }
    .imagem-estilizada:hover {
      transform: scale(1.05);
      filter: grayscale(0%) brightness(110%);
    }
  </style>
</head>
<body>
  <img class="imagem-estilizada" src="floresta.jpg" alt="Floresta com efeitos CSS">
</body>
</html>
```  

**Resultado**: Uma imagem responsiva com efeito de escala suave e filtros dinâmicos no hover.  
 
---

## :nine: **Exemplo: CSS**

```css
        /* Estilos para o elemento body */
        body {
            font-family: 'Arial', sans-serif; 
            line-height: 1.6; 
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2); 
            min-height: 100vh;
        }

        h1 {
            color: #333;
            font-size: 2.5em; 
            font-weight: bold;
        }

        p {
            color: #666;
            font-size: 16px;
            line-height: 1.5; /* Espaçamento entre linhas */
        }

        .caixa {
            background-image: url("img/paisagem-original.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            
            border: 3px dashed #007BFF; /* Borda tracejada azul */
            padding: 20px;
            margin: 15px 0; /* Margem externa */
            text-align: center; /* Alinhamento de texto */
        }

        /*Removedo as margens*/
        figure {
            margin: 0px; 
            margin-bottom: 10px;       
            border-bottom: 3px solid  #007BFF ;
        }

        img.l300 {
            width: 300px;
            height: auto;
            aspect-ratio: 16/9;
        }

        img.l300_triangulo {
            width: 300px;
            height: auto;
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
        }
        
        img.l300_circulo {
            width: 300px;
            height: auto;
            clip-path: circle(50%); /* Recorte circular  */
        }

        img.l300_transicao {
            width: 300px;;
            height: auto;
            transition: transform 0.3s ease;
        }

        img.l300_transicao:hover {
            transform: scale(1.1);
        }

        img.lmax {
            max-width: 100%;
            height: auto;
        }

        img.recorte_t {
            object-fit: cover; 
            object-position: 25% 50%; 
            width: 100%;
            height: 300px;
        }

        img.recorte_b {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
        }
        
        img.recorte_move {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
        }

        img.recorte_move:hover {
            object-position: 50% 25%; /* Move o foco para cima */
        }

        img.recorte_b_cinza {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
            filter: grayscale(90%); 
        }

        img.recorte_b_brilho_alto {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
            filter: brightness(150%); 
        }

        img.recorte_b_sepia {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
            filter: sepia(90%) contrast(150%);
        }

        img.recorte_b_mask {
            object-fit: cover; 
            object-position: 25% 100%; 
            width: 100%;
            height: 300px;
            mask-image: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0));
        }
```





--- 

## :nine:  **Conclusão**

O CSS oferece ferramentas poderosas para manipular imagens sem precisar de edições manuais. Explore combinações de propriedades e priorize a performance e acessibilidade!