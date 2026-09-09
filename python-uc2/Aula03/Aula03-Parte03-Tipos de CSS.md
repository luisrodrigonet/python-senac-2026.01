# Aula 03 - Tipos de CSS
> HTML5 é a linguagem de marcação padrão para estruturar conteúdo na web, enquanto CSS (Cascading Style Sheets) é usado para estilizar elementos HTML.
> Existem três formas principais de aplicar CSS: **in-line**, **incorporado** e **externo**. 
> Este tutorial demonstra cada método, evolui de um para o outro e discute vantagens e desvantagens.

---

## **1. CSS In-line**
O CSS `in-line` é aplicado diretamente em elementos HTML usando o atributo `style`.

### **Exemplo**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo CSS In-line</title>
</head>
<body>
    <h1 style="color: blue; font-size: 24px;">Título Estilizado</h1>
    <p style="color: gray; margin: 10px;">Este parágrafo usa CSS in-line.</p>
</body>
</html>
```

:dart: **Vantagens**
- **Rápido para ajustes pontuais**: Útil para testes rápidos ou estilos únicos.
- **Prioridade alta**: Sobrepõe estilos incorporados ou externos (em caso de conflito).

:ghost: **Desvantagens**
- **Dificulta manutenção**: Estilos repetidos em múltiplos elementos.
- **Polui o HTML**: Mistura estrutura e apresentação, violando boas práticas.

---

## **2. CSS Incorporado (Interno)**
O CSS incorporado é definido dentro da tag `<style>` no `<head>` do HTML.

### **Exemplo (Evolução do In-line)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo CSS Incorporado</title>
    <style>
        h1 {
            color: blue;
            font-size: 24px;
        }
        p {
            color: gray;
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>Título Estilizado</h1>
    <p>Este parágrafo usa CSS incorporado.</p>
</body>
</html>
```

:dart: **Vantagens**
- **Organização**: Centraliza estilos em um único local (dentro do HTML).
- **Reutilização**: Aplica o mesmo estilo a múltiplos elementos.

:ghost: **Desvantagens**
- **Não é escalável**: Ineficiente para múltiplas páginas (estilos não são compartilhados).
- **Aumenta o tamanho do HTML**: Pode tornar o carregamento mais lento.

---

## **3. CSS Externo**
O CSS externo é armazenado em um arquivo separado (`.css`) e vinculado ao HTML via `<link>`.

### **Passo a Passo**

#### **1. Crie um arquivo CSS (ex: `estilos.css`)**
```css
/* estilos.css */
h1 {
    color: blue;
    font-size: 24px;
}

p {
    color: gray;
    margin: 10px;
}
```

#### **2. Vincule o CSS ao HTML**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo CSS Externo</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Título Estilizado</h1>
    <p>Este parágrafo usa CSS externo.</p>
</body>
</html>
```

:dart: **Vantagens**
- **Máxima reutilização**: Um arquivo pode estilizar múltiplas páginas.
- **Separação de responsabilidades**: HTML (estrutura) e CSS (design) são independentes.
- **Performance**: O navegador armazena o CSS em cache, acelerando carregamento.

:ghost: **Desvantagens**
- **Complexidade inicial**: Requer organização de arquivos.
- **Dependência externa**: Se o arquivo CSS não carregar, o site perde estilo.

---

## :bulb: **Comparação Resumida**

| Método       | Vantagens                          | Desvantagens                     | Melhor Uso                  |
|--------------|------------------------------------|-----------------------------------|-----------------------------|
| **In-line**  | Simples, prioridade alta           | Manutenção difícil, HTML poluído | Ajustes pontuais            |
| **Incorporado**| Organização, reutilização       | Não escalável, HTML grande       | Páginas únicas              |
| **Externo**  | Escalável, performance, separação | Configuração inicial             | Projetos grandes/múltiplas páginas |

- **In-line**: Use para testes rápidos ou estilos exclusivos.
- **Incorporado**: Ideal para páginas únicas com estilos específicos.
- **Externo**: Recomendado para projetos profissionais, garantindo organização e eficiência.

Ao evoluir de in-line para externo, você adota práticas sustentáveis e escaláveis, essenciais para desenvolvimento web moderno. 🚀