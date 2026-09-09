# Aula 03 - Parte 1 - Multimídia 

> O HTML5 trouxe recursos nativos para incorporar áudio, vídeo e integração com mapas em páginas web, eliminando a necessidade de plugins externos.
> Nesta parte do curso, exploraremos como usar essas funcionalidades e estilizá-las com CSS.
> Para incorporar áudio, vídeo e mapas em HTML5 utilizando arquivos públicos disponíveis na web.


---

## **1. Áudio em HTML5**

### **Tag  <audio>**  

Adicione áudio à sua página com a tag `<audio>`. Formatos suportados: `MP3`, `WAV`, `OGG`.

**Exemplo Básico:**
```html
<audio controls>
  <source src="musica.mp3" type="audio/mpeg">
  Seu navegador não suporta áudio HTML5.
</audio>
```

#### **Estilizando o Player de Áudio com CSS**  

Personalize a aparência do player:

```css
audio {
  width: 100%;
  margin: 20px 0;
  background-color: #f0f0f0;
  border-radius: 10px;
  padding: 10px;
}

audio:hover {
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
```

Utilize arquivos de áudio públicos (ex.: [CC0 ou domínio público](https://creativecommons.org/publicdomain/)) para garantir acesso universal.

#### **Exemplo com Arquivo Público**  
```html
<audio controls>
  <source src="https://cdn.pixabay.com/music/audiosample.mp3" type="audio/mpeg">
  <source src="https://commons.wikimedia.org/audiosample.ogg" type="audio/ogg">
  Seu navegador não suporta áudio HTML5.
</audio>
```

#### **CSS para Estilização**  
```css
audio {
  width: 80%;
  margin: 15px auto;
  background: #f8f9fa;
  border-radius: 15px;
  padding: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
```

---

## **2. Vídeo em HTML5**

### **Tag <video>**  

Incorpore vídeos com a tag `<video>`. Formatos suportados: `MP4`, `WebM`, `OGG`.

**Exemplo Básico:**
```html
<video controls width="600">
  <source src="video.mp4" type="video/mp4">
  Seu navegador não suporta vídeo HTML5.
</video>
```

#### **Estilizando o Player de Vídeo com CSS**  

Crie um container responsivo e estilizado:

```css
.video-container {
  max-width: 800px;
  margin: 20px auto;
  border: 3px solid #333;
  border-radius: 15px;
  overflow: hidden;
}

video {
  width: 100%;
  display: block;
}
```

Incorpore vídeos públicos de plataformas como `Wikimedia Commons` ou arquivos de demonstração.

#### **Exemplo com Vídeo Público**  
```html
<video controls width="800">
  <source src="https://archive.org/download/ElephantsDream/ed_hd.mp4" type="video/mp4">
  <source src="https://commons.wikimedia.org/videosample.webm" type="video/webm">
  Seu navegador não suporta vídeo HTML5.
</video>
```

#### **CSS para Container Responsivo**  
```css
.video-container {
  max-width: 1000px;
  margin: 20px auto;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  overflow: hidden;
}

video {
  width: 100%;
  height: auto;
}
```

---

## **3. Integração com Mapas**

### **Incorporando Mapas (Google Maps)**  
Use `<iframe>` para integrar mapas. Obtenha o código de incorporação no Google Maps.

**Exemplo Básico:**
```html
<div class="mapa">
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12345..."
    width="600" 
    height="450" 
    style="border:0;" 
    allowfullscreen>
  </iframe>
</div>
```

#### **Estilizando o Mapa com CSS**  
Adicione efeitos e ajuste o layout:

```css
.mapa {
  width: 100%;
  max-width: 800px;
  margin: 20px auto;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}

.mapa:hover {
  transform: scale(1.02);
}

iframe {
  width: 100%;
  height: 400px;
  border: none;
  border-radius: 15px;
}
```

Use um local público (ex.: Torre Eiffel) para demonstrar a integração.

#### **Exemplo com Iframe**  

```html
<div class="mapa">
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.991440608207!2d2.292292615509614!3d48.858373608662095!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e2964e34e2d%3A0x8ddca9ee380ef7e0!2sTorre%20Eiffel!5e0!3m2!1spt-BR!2sbr!4v1713123456789!5m2!1spt-BR!2sbr" 
    width="600" 
    height="450" 
    style="border:0;" 
    allowfullscreen>
  </iframe>
</div>
```

#### **CSS para Efeitos no Mapa**  
```css
.mapa {
  max-width: 1000px;
  margin: 20px auto;
  border-radius: 12px;
  transition: transform 0.3s;
}

.mapa:hover {
  transform: scale(1.01);
}

iframe {
  width: 100%;
  height: 450px;
  border: none;
  border-radius: 12px;
}
```


---

### **4. Exemplo Completo Integrado**


**HTML:**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Multimídia com HTML5 e CSS</title>
  <style>
    /* Estilos CSS */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    audio {
      width: 100%;
      background: #e9ecef;
      border-radius: 20px;
      margin: 15px 0;
    }

    .video-container {
      background: #000;
      border-radius: 15px;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Demonstração de Multimídia</h1>
    
    <!-- Áudio -->
    <audio controls>
      <source src="audio.mp3" type="audio/mpeg">
    </audio>

    <!-- Vídeo -->
    <div class="video-container">
      <video controls>
        <source src="video.mp4" type="video/mp4">
      </video>
    </div>

    <!-- Mapa -->
    <div class="mapa">
      <iframe src="URL_DO_MAPA"></iframe>
    </div>
  </div>
</body>
</html>
```

**Exemplo Completo:** utilizando arquivos públicos

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Multimídia com Arquivos Públicos</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    .container { max-width: 1200px; margin: 0 auto; }
    audio, .video-container, .mapa { margin: 25px 0; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Demonstração de Recursos Multimídia</h1>

    <!-- Áudio -->
    <audio controls>
      <source src="https://cdn.pixabay.com/music/audiosample.mp3" type="audio/mpeg">
      Seu navegador não suporta áudio HTML5.
    </audio>

    <!-- Vídeo -->
    <div class="video-container">
      <video controls>
        <source src="https://archive.org/download/ElephantsDream/ed_hd.mp4" type="video/mp4">
        <track src="legendas.vtt" kind="subtitles" srclang="pt" label="Português">
      </video>
    </div>

    <!-- Mapa -->
    <div class="mapa">
      <iframe src="URL_DO_MAPA_PÚBLICO"></iframe>
    </div>
  </div>
</body>
</html>
```

## **4. Dicas Essenciais**

1. **Formatos Multiplataforma**:  
   - Para áudio: inclua MP3 (suporte universal) e OGG (Firefox/Chrome).  
   - Para vídeo: use MP4 (H.264) e WebM (VP9) para compatibilidade cruzada.  

2. **Acessibilidade**:  
   - Adicione `<track>` para legendas em vídeos:  
     ```html
     <track src="legendas.vtt" kind="subtitles" srclang="pt" label="Português">
     ```
   - Use `alt` em imagens e `aria-label` em players para leitores de tela .

3. **Fontes de Arquivos Públicos**:  
   - **Áudio**: [Free Music Archive](https://freemusicarchive.org/) ou [Pixabay](https://pixabay.com/music/).  
   - **Vídeo**: [Wikimedia Commons](https://commons.wikimedia.org/) ou [Internet Archive](https://archive.org/).  
   - **Mapas**: Links públicos do Google Maps (gerados via "Compartilhar > Incorporar").

4. **Otimização**:  
   - Reduza o tamanho de arquivos com ferramentas como [HandBrake](https://handbrake.fr/) (vídeo) ou [Audacity](https://www.audacityteam.org/) (áudio).  
   - Use `preload="metadata"` em `<video>` para carregamento eficiente .

5. **Licenciamento**:  
   - Verifique licenças (ex.: CC0, Creative Commons) para evitar violações de direitos autorais .

---

## **5. Dicas Finais**  
1. **Responsividade:** Use `max-width: 100%` e unidades relativas para adaptação a diferentes telas.  

1. **Compatibilidade:** Inclua múltiplos formatos de mídia para garantir funcionamento em todos os navegadores.

1. **Formatos Multiplataforma**:  
   - Para áudio: inclua MP3 (suporte universal) e OGG (Firefox/Chrome).  
   - Para vídeo: use MP4 (H.264) e WebM (VP9) para compatibilidade cruzada.  

1. **Acessibilidade**:  
   - Adicione `<track>` para legendas em vídeos:  
     ```html
     <track src="legendas.vtt" kind="subtitles" srclang="pt" label="Português">
     ```
   - Use `alt` em imagens e `aria-label` em players para leitores de tela .

1. **Fontes de Arquivos Públicos**:  
   - **Áudio**: [Free Music Archive](https://freemusicarchive.org/) ou [Pixabay](https://pixabay.com/music/).  
   - **Vídeo**: [Wikimedia Commons](https://commons.wikimedia.org/) ou [Internet Archive](https://archive.org/).  
   - **Mapas**: Links públicos do Google Maps (gerados via "Compartilhar > Incorporar").

1. **Otimização**:  
   - Reduza o tamanho de arquivos com ferramentas como [HandBrake](https://handbrake.fr/) (vídeo) ou [Audacity](https://www.audacityteam.org/) (áudio).  
   - Use `preload="metadata"` em `<video>` para carregamento eficiente .

5. **Licenciamento**:  
   - Verifique licenças (ex.: CC0, Creative Commons) para evitar violações de direitos autorais .

## **Recursos Adicionais**  
- **Templates HTML5**: Use modelos responsivos de [Mobirise](https://mobirise.com/html-templates/) para layouts prontos .  
- **Codecs**: Prefira VP9 (WebM) e H.264 (MP4) para equilibrar qualidade e compatibilidade .  
- **Ferramentas**: Utilize [FFmpeg](https://ffmpeg.org/) para conversão de formatos e compressão.  