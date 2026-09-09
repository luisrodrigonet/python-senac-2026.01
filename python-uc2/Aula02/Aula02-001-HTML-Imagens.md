# Aula 02 - HTML5 - Imagens I
> 
> Nesta aula será demonstrada a inserção de imagens dentro de um HTML. Explorando desde a inserção básica até práticas avançadas de acessibilidade e otimização
> 
> Serão apresentadas dicas de boa prática e acessibilidade, como o `alt`, utilizando apenas o `Width` e o `Height` dentro do HTML.
>
> Além disso, discutiremos repositórios gratuitos de imagens e questões relacionadas ao uso de direitos autorais na internet.

---

## :one: **Inserindo Imagens no HTML5**

A tag `<img>` é usada para incorporar imagens em uma página da web. Ela possui atributos essenciais que garantem funcionalidade e acessibilidade.

### :bookmark: **Sintaxe Básica**
```html
<img src="caminho/para/imagem.jpg" alt="Descrição alternativa da imagem">
```

- **`src`**: Define o caminho da imagem (pode ser relativo ou absoluto).
- **`alt`**: Fornece uma descrição textual alternativa para a imagem, essencial para acessibilidade e SEO.

### :bookmark: **Exemplo Completo**


```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Imagem</title>
</head>
<body>
    <h1>Minha Primeira Imagem</h1>
    <img src="img/paisagem.jpg" alt="Uma bela paisagem com montanhas e um lago">
</body>
</html>
```

---

## :two: **Melhores Práticas para Uso de Imagens**

### :bookmark: **Escolha do Formato Adequado**

- **JPEG**: Ideal para fotografias e imagens com muitas cores e gradientes.
- **PNG**: Recomendado para imagens com transparência ou detalhes nítidos (logotipos, ícones).
- **SVG**: Vetor escalável, perfeito para gráficos, ícones e ilustrações simples.
- **WebP**: Novo formato que oferece alta compressão e qualidade, compatível com navegadores modernos.

### :bookmark: **Otimização de Tamanho**
Imagens grandes podem afetar negativamente o desempenho do site. Use ferramentas como:

- [TinyPNG](https://tinypng.com/)
- [ImageOptim](https://imageoptim.com/)
- [Squoosh](https://squoosh.app/)

### :bookmark: **Largura e Altura**

Sempre especifique as dimensões da imagem para evitar redimensionamento inesperado no navegador.

:globe_with_meridians: **Código HTML**
```html
<img src="paisagem.jpg" alt="Paisagem" width="800" height="600">
```

Ou use CSS para controle responsivo:

:zap: **Código CSS**
```css
img {
    max-width: 100%;
    height: auto;
}
```

### :bookmark: **Imagens Responsivas**

O código HTML oferece a tag `<img>`  alguns atributos específicos para implementar uma imagem responsiva, permitindo que o navegador carregue a versão mais adequada da imagem de acordo com o tamanho da tela e a densidade de pixels do dispositivo.

:globe_with_meridians: **Código HTML**
```html
<img 
    src="paisagem-pequena.jpg" 
    srcset="paisagem-pequena.jpg 480w, paisagem-media.jpg 800w, paisagem-grande.jpg 1200w" 
    sizes="(max-width: 600px) 480px, (max-width: 900px) 800px, 1200px" 
    alt="Paisagem responsiva">
```

- **`src` (Fonte Padrão)** - Define a imagem padrão que será carregada em navegadores que não suportam `srcset`. Geralmente é a menor versão da imagem, ideal para dispositivos antigos ou situações onde o `srcset` não é aplicado.

- **`srcset` (Conjunto de Fontes)** - Oferece uma lista de imagens alternativas, permitindo que o navegador escolha a mais adequada com base no tamanho da tela e na densidade de `pixels`.

    - **Sintaxe:** `caminho-da-imagem largura-da-imagem`.
    - **Valores:**
      - `paisagem-pequena.jpg 480w`: Imagem de 480 `pixels` de largura.
      - `paisagem-media.jpg 800w`: Imagem de 800 `pixels` de largura.
      - `paisagem-grande.jpg 1200w`: Imagem de 1200 `pixels` de largura.
    - **Como Funciona:**
        - O navegador calcula qual imagem tem a largura mais próxima da necessária, considerando o layout definido em `sizes` e a densidade de pixels do dispositivo (ex: telas Retina).

- **`sizes` (Tamanhos de Exibição)** - Define condições de mídia (como breakpoints) e o tamanho que a imagem ocupará no layout em cada cenário.

    - **Sintaxe:** `(condição-de-mídia) tamanho, ...`.
    - **Valores:**
      - `(max-width: 600px) 480px`: Se a tela tiver até 600px de largura, a imagem ocupará 480px.
      - `(max-width: 900px) 800px`: Se a tela tiver até 900px (mas mais que 600px), a imagem ocupará 800px.
      - `1200px`: Caso padrão (telas maiores que 900px), a imagem ocupará 1200px.
    - **Como Funciona:**
      - O navegador usa essas regras para determinar a largura virtual da imagem no layout, combinando com as opções do `srcset` para selecionar a imagem ideal.

- **`alt` (Texto Alternativo)** - Fornece uma descrição textual da imagem para acessibilidade (leitores de tela) e situações onde a imagem não carrega.
    - **Valor:** `"Paisagem responsiva"`.


#### **Exemplo Prático**
- **Dispositivo Mobile (300px de largura, tela 2x):**
  - `sizes` define 480px de espaço para a imagem.
  - Densidade 2x: 480px × 2 = 960px necessários.
  - A imagem mais próxima é `paisagem-media.jpg` (800px), que cobre 960px com qualidade aceitável.

- **Desktop (1200px de largura, tela 1x):**
  - `sizes` define 1200px de espaço.
  - A imagem escolhida é `paisagem-grande.jpg` (1200px).

#### **Vantagens**
- **Performance:** Evita carregar imagens grandes em dispositivos pequenos.
- **Qualidade:** Garante a melhor resolução possível para cada contexto.
- **Flexibilidade:** Adapta-se automaticamente a diferentes layouts.

#### **Compatibilidade**
- Funciona em navegadores modernos (Chrome, Firefox, Safari, Edge).
- Navegadores antigos ignoram `srcset` e `sizes`, usando apenas `src`.

---

## :three: **Acessibilidade em Imagens**

### :bookmark: **Descrições Alternativas (`alt`)**
- Sempre forneça um texto alternativo significativo.
- Para imagens decorativas (sem valor informativo), use `alt=""`.

:globe_with_meridians: **Exemplo:**
```html
<img src="decoracao.png" alt="">
```

### :bookmark: **Figuras Complexas**

Para gráficos ou infográficos, use `<figure>` e `<figcaption>` para fornecer contexto adicional.

:globe_with_meridians: **Exemplo:**
```html
<figure>
    <img src="grafico.jpg" alt="Gráfico mostrando a previsão do crescimento populacional de 1950 a 2100">
    <figcaption>Gráfico mostrando a previsão do crescimento populacional de 1950 a 2100.</figcaption>
</figure>
```

### :bookmark: **Evitar Texto em Imagens**

Prefira usar texto real sempre que possível. Se necessário, insira o texto diretamente no HTML com estilização CSS.

---

## :four: **Repositórios Gratuitos de Imagens**

Utilizar imagens de alta qualidade e gratuitas pode economizar tempo e recursos. Aqui estão alguns repositórios confiáveis:

### :bookmark: **Repositórios de Fotos**
- **Unsplash**: [https://unsplash.com](https://unsplash.com)
- **Pexels**: [https://www.pexels.com](https://www.pexels.com)
- **Pixabay**: [https://pixabay.com](https://pixabay.com)

### :bookmark: **Ícones e Ilustrações**
- **Flaticon**: [https://www.flaticon.com](https://www.flaticon.com)
- **Icons8**: [https://icons8.com](https://icons8.com)
- **Freepik**: [https://www.freepik.com](https://www.freepik.com)

### :bookmark: **SVG Grátis**
- **SVG Repo**: [https://www.svgrepo.com](https://www.svgrepo.com)
- **Openclipart**: [https://openclipart.org](https://openclipart.org)

---

## :five: **Direitos Autorais e Licenças**

### :bookmark: **Entendendo Licenças**
Antes de usar uma imagem, verifique sua licença:
- **Domínio Público**: Livre para qualquer uso.
- **Creative Commons (CC)**: Permite uso com condições específicas (atribuição, não comercial, etc.).
- **Licença Paga**: Requer pagamento ou contrato.

### :bookmark: **Como Atribuir Créditos**
Se a licença exigir atribuição, inclua o crédito no rodapé da página ou próximo à imagem.

:globe_with_meridians: **Exemplo:**
```html
<p>Imagem por <a href="https://unsplash.com/@autor">Autor</a> no Unsplash.</p>
```

### :bookmark: **Evite Roubo de Conteúdo**
Nunca use imagens encontradas em motores de busca sem verificar os direitos autorais. Utilize repositórios confiáveis ou contrate profissionais.



## :books: **Referências**

- [W3C - HTML Images](https://www.w3schools.com/html/html_images.asp)



## :bulb: **Conclusão**

Incorporar imagens no HTML5 é simples, mas requer atenção a detalhes importantes para garantir acessibilidade, desempenho e conformidade legal. Seguindo as melhores práticas, você poderá criar sites visualmente atraentes e inclusivos, enquanto evita problemas relacionados a direitos autorais.

