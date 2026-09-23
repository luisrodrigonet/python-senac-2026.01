# Aula 06 - Parte 01 - Formulário - Cont
> Apresentar os principais elementos de formulário HTML **select**, **radio**, **checkbox**, **color**, **file** e **textarea**), suas propriedades e exemplos de uso prático.
>
> ---
>

## 1. Elemento `<select>`

Este elemento cria uma lista suspensa (_dropdown_) que permite ao usuário selecionar uma ou mais opções de uma lista pré-definida. Ideal para campos com múltiplas opções fixas, como estados, países ou categorias.


**Propriedades:**
- `name`: Nome do campo
- `multiple`: Permite seleção múltipla
- `size`: Número de opções visíveis
- `required`: Campo obrigatório
- `disabled`: Desabilita o campo

**Exemplo:**
```html
<label for="estado">Estado:</label>
<select id="estado" name="estado" required>
  <option value="">Selecione...</option>
  <option value="SP">São Paulo</option>
  <option value="RJ">Rio de Janeiro</option>
  <option value="MG">Minas Gerais</option>
</select>
```

## 2. Elemento `<input type="radio">`

Cria botões de opção exclusiva onde o usuário deve escolher uma **única alternativa** entre um grupo de opções. Todos os `radio buttons` do mesmo grupo compartilham o mesmo atributo name.

**Propriedades:**
- `name`: Nome do grupo (mesmo para todas opções)
- `value`: Valor que será enviado
- `checked`: Selecionado por padrão
- `disabled`: Desabilita a opção

**Exemplo:**
```html
<label>Gênero:</label>
<input type="radio" id="masculino" name="genero" value="M" checked>
<label for="masculino">Masculino</label>

<input type="radio" id="feminino" name="genero" value="F">
<label for="feminino">Feminino</label>
```

## 3. Elemento `<input type="checkbox">`

Cria caixas de seleção que permitem **múltiplas escolhas**. Diferente do radio button, cada checkbox funciona de forma independente, mas pode ser agrupado logicamente usando o mesmo name.

**Propriedades:**
- `name`: Nome do campo (pode ser array com [])
- `value`: Valor que será enviado
- `checked`: Selecionado por padrão
- `disabled`: Desabilita a opção

**Exemplo:**
```html
<label>Interesses:</label>
<input type="checkbox" id="esportes" name="interesses[]" value="esportes">
<label for="esportes">Esportes</label>

<input type="checkbox" id="musica" name="interesses[]" value="musica">
<label for="musica">Música</label>
```

## 4. Elemento `<input type="color">`

Exibe um** seletor de cores nativo do navegador**, permitindo ao usuário escolher uma cor através de uma interface visual. Retorna o valor em hexadecimal (#RRGGBB).

**Propriedades:**
- `name`: Nome do campo
- `value`: Cor padrão (hexadecimal)
- `list`: Associado a um `<datalist>`

**Exemplo:**
```html
<label for="cor-favorita">Cor favorita:</label>
<input type="color" id="cor-favorita" name="cor_favorita" value="#ff0000">
```

## 5. Elemento `<input type="file">`

Cria um campo para **upload de arquivos**. Pode ser configurado para aceitar **tipos específicos** de arquivos e permitir seleção múltipla.

**Propriedades:**
- `name`: Nome do campo
- `accept`: Tipos de arquivo aceitos (ex: image/*, .pdf)
- `multiple`: Permite múltiplos arquivos
- `capture`: Em dispositivos móveis, abre câmera diretamente
- `required`: Campo obrigatório

**Exemplo:**
```html
<label for="foto">Envie sua foto:</label>
<input type="file" id="foto" name="foto" accept="image/*" required>
```

## 6. Elemento `<textarea>`

Cria uma **área de texto multilinha** para entradas extensas como comentários, descrições ou mensagens. Oferece melhor controle sobre dimensões que um input text comum.

**Propriedades:**
- `name`: Nome do campo
- `rows`: Número de linhas visíveis
- `cols`: Número de colunas (largura)
- `maxlength`: Máximo de caracteres
- `placeholder`: Texto de exemplo
- `wrap`: Define quebra de linha (soft/hard)

**Exemplo:**
```html
<label for="mensagem">Mensagem:</label>
<textarea id="mensagem" name="mensagem" rows="4" cols="50" 
          placeholder="Digite sua mensagem aqui..."></textarea>
```

## Exemplo Completo: Página de Cadastro de Clientes

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Cliente</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        form { display: grid; gap: 15px; }
        fieldset { border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
        legend { font-weight: bold; }
        .form-group { display: grid; gap: 5px; }
        button { padding: 10px 15px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Cadastro de Cliente</h1>
    
    <form action="/cadastro" method="POST" enctype="multipart/form-data">
        <fieldset>
            <legend>Dados Pessoais</legend>
            
            <div class="form-group">
                <label for="nome">Nome Completo:</label>
                <input type="text" id="nome" name="nome" required>
            </div>
            
            <div class="form-group">
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label>Gênero:</label>
                <div>
                    <input type="radio" id="masculino" name="genero" value="M" checked>
                    <label for="masculino">Masculino</label>
                    
                    <input type="radio" id="feminino" name="genero" value="F">
                    <label for="feminino">Feminino</label>
                    
                    <input type="radio" id="outro" name="genero" value="O">
                    <label for="outro">Outro</label>
                </div>
            </div>
            
            <div class="form-group">
                <label for="data-nascimento">Data de Nascimento:</label>
                <input type="date" id="data-nascimento" name="data_nascimento" required>
            </div>
            
            <div class="form-group">
                <label for="cor-favorita">Cor Favorita:</label>
                <input type="color" id="cor-favorita" name="cor_favorita" value="#ff0000">
            </div>
        </fieldset>
        
        <fieldset>
            <legend>Endereço</legend>
            
            <div class="form-group">
                <label for="estado">Estado:</label>
                <select id="estado" name="estado" required>
                    <option value="">Selecione...</option>
                    <option value="SP">São Paulo</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="MG">Minas Gerais</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="cidade">Cidade:</label>
                <input type="text" id="cidade" name="cidade" required>
            </div>
        </fieldset>
        
        <fieldset>
            <legend>Preferências</legend>
            
            <div class="form-group">
                <label>Interesses:</label>
                <div>
                    <input type="checkbox" id="esportes" name="interesses[]" value="esportes">
                    <label for="esportes">Esportes</label>
                </div>
                <div>
                    <input type="checkbox" id="musica" name="interesses[]" value="musica">
                    <label for="musica">Música</label>
                </div>
                <div>
                    <input type="checkbox" id="viagens" name="interesses[]" value="viagens">
                    <label for="viagens">Viagens</label>
                </div>
            </div>
            
            <div class="form-group">
                <label for="newsletter">Deseja receber newsletter?</label>
                <input type="checkbox" id="newsletter" name="newsletter" value="1" checked>
            </div>
        </fieldset>
        
        <fieldset>
            <legend>Documentos</legend>
            
            <div class="form-group">
                <label for="foto">Foto do Perfil:</label>
                <input type="file" id="foto" name="foto" accept="image/*" required>
            </div>
            
            <div class="form-group">
                <label for="curriculo">Currículo (PDF):</label>
                <input type="file" id="curriculo" name="curriculo" accept=".pdf">
            </div>
        </fieldset>
        
        <div class="form-group">
            <label for="observacoes">Observações:</label>
            <textarea id="observacoes" name="observacoes" rows="4" 
                      placeholder="Alguma observação importante..."></textarea>
        </div>
        
        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
```

## Conclusão

Nesta aula, exploramos os principais elementos de formulário HTML:
- `<select>` para listas suspensas
- `<input type="radio">` para seleção única
- `<input type="checkbox">` para múltiplas seleções
- `<input type="color">` para seleção de cores
- `<input type="file">` para upload de arquivos
- `<textarea>` para textos longos

