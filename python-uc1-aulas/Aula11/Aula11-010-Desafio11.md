# Aula 11 - Desafio 11

## O Desafio :
> 
>  Utilizando a estrutura de dados `Dicionário` **desenvolva um sistema interativo** para gerenciar livros, com as seguintes funcionalidades:
> 1. Adicionar Livro
> 2. Remover um livro
> 3. Buscar um livro
> 4. Listar todos os usuários.

**Por que usar um Dicionário para gerenciar livros?**

Um dicionário em Python é uma coleção de pares chave-valor (key-value). A grande vantagem é que ele oferece um acesso muito rápido aos valores, já que usamos a chave para encontrá-los.

Para o nosso sistema de livros, a chave ideal seria o título do livro, já que ele é único. O valor associado a essa chave pode ser outro dicionário, contendo detalhes como autor e ano de publicação.

Exemplo:

```Python
livros = {
    "Dom Quixote": {
        "autor": "Miguel de Cervantes",
        "ano": 1605
    },
    "1984": {
        "autor": "George Orwell",
        "ano": 1949
    }
}
```

