# Aula 12 - Orientação a Objeto 
> ## Sistema de Gerenciamento de Biblioteca
> 
> **Objetivo da Atividade**:
> 
> Desenvolver um sistema simples de gerenciamento de biblioteca utilizando Orientação a Objetos em Python. O sistema permitirá adicionar livros, listar livros disponíveis, emprestar livros e devolver livros.
> 
> ### Requisitos do Sistema:
> 
> 1. **Classes a serem implementadas**:
>    - `Livro`: Representa um livro com atributos como título, autor, ano de publicação e status (disponível ou emprestado).
>    - `Biblioteca`: Gerencia uma coleção de livros e fornece métodos para adicionar, listar, emprestar e devolver livros.
> 
> 2. **Funcionalidades**:
>    - Adicionar um novo livro à biblioteca.
>    - Listar todos os livros disponíveis.
>    - Emprestar um livro (alterar seu status para "emprestado").
>    - Devolver um livro (alterar seu status para "disponível").
> 
> 3. **Interação com o usuário**:
>    - O programa deve ter um menu interativo para o usuário escolher as operações.
>
> ### Passos para Implementação:
> 
> 1. **Criar a classe `Livro`**:
>    - Atributos: `titulo`, `autor`, `ano`, `status` (inicialmente "disponível").
>    - Métodos: Método para exibir informações do livro.
> 
> 2. **Criar a classe `Biblioteca`**:
>    - Atributos: Uma lista para armazenar os livros.
>    - Métodos:
>      - `adicionar_livro(livro)`: Adiciona um livro à biblioteca.
>      - `listar_livros()`: Exibe todos os livros disponíveis.
>      - `emprestar_livro(titulo)`: Altera o status do livro para "emprestado".
>      - `devolver_livro(titulo)`: Altera o status do livro para "disponível".
> 
> 3. **Criar o menu interativo**:
>    - Exibir opções para o usuário (adicionar, listar, emprestar, devolver, sair).
>    - Ler a escolha do usuário e chamar os métodos apropriados da classe `Biblioteca`.
> 

# Resolução da Atividade

## Classe Livro

:snake: **Código**:
```python
# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = "disponível"  # Status inicial

    def exibir_info(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano} | Status: {self.status}")

```

## Classe Biblioteca

:snake: **Código**:
```python
class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                livro.exibir_info()

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.status == "disponível":
                    livro.status = "emprestado"
                    print(f"Livro '{titulo}' emprestado com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está emprestado.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.status == "emprestado":
                    livro.status = "disponível"
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está disponível.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

```

## Menu do programa

:snake: **Código**:
```
# Função para exibir o menu
def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Biblioteca ---")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")

```

## Função principal


:snake: **Código**:
```
if __name__ == "__main__" :
    # Programa principal
    biblioteca = Biblioteca()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            titulo = input("Título do livro a ser emprestado: ")
            biblioteca.emprestar_livro(titulo)
        elif opcao == "4":
            titulo = input("Título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

```

---

