# Aula 11 - Desafio 11

> O recrutador entregou uma lista de atividades para você executar, relacionadas a programação Orientada a Objeto (OO). 

## :one: Objetivo da Atividade:

> Desenvolver um sistema simples de gerenciamento de biblioteca utilizando Orientação a Objetos em Python. O sistema permitirá adicionar livros, listar livros disponíveis, emprestar livros e devolver livros.

## :two: Requisitos do Sistema:

1. **Classes a serem implementadas**:
   - `Livro`: Representa um livro com atributos como título, autor, ano de publicação e status (disponível ou emprestado).
   - `Biblioteca`: Gerencia uma coleção de livros e fornece métodos para adicionar, listar, emprestar e devolver livros.

2. **Funcionalidades**:
   - Adicionar um novo livro à biblioteca.
   - Listar todos os livros disponíveis.
   - Emprestar um livro (alterar seu status para "emprestado").
   - Devolver um livro (alterar seu status para "disponível").

3. **Interação com o usuário**:
   - O programa deve ter um menu interativo para o usuário escolher as operações.
   

## :three: Passos para Implementação:

1. **Criar a classe `Livro`**:
   - Atributos: `titulo`, `autor`, `ano`, `status` (inicialmente "disponível").
   - Métodos: Método para exibir informações do livro.

2. **Criar a classe `Biblioteca`**:
   - Atributos: Uma lista para armazenar os livros.
   - Métodos:
     - `adicionar_livro(livro)`: Adiciona um livro à biblioteca.
     - `listar_livros()`: Exibe todos os livros disponíveis.
     - `emprestar_livro(titulo)`: Altera o status do livro para "emprestado".
     - `devolver_livro(titulo)`: Altera o status do livro para "disponível".

3. **Criar o menu interativo**:
   - Exibir opções para o usuário (adicionar, listar, emprestar, devolver, sair).
   - Ler a escolha do usuário e chamar os métodos apropriados da classe `Biblioteca`.
  
 
