# Aula 11 - Tarefa 0
> Utilizando dicionários

## **Exercício 1: Operações Básicas**  

**Problema:**  
- Crie um dicionário `pessoa` com as chaves `nome`, `idade`, e `cidade`. 
- Adicione uma nova chave `email`
- Atualize a `idade` para 31
- Remova `cidade`.  

**Solução:**  
```python
# Criar dicionário
pessoa = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}

# Adicionar chave
pessoa["email"] = "ana@email.com"

# Atualizar idade
pessoa["idade"] = 31

# Remover cidade
del pessoa["cidade"]

print(pessoa)
```

**Explicação:**  
- **Criação**: Inicializamos o dicionário com chaves pré-definidas.  
- **Adição**: Usamos `pessoa["email"] = ...` para incluir uma nova chave.  
- **Atualização**: Sobrescrevemos o valor de `idade`.  
- **Remoção**: Usamos `del` para excluir `cidade`.  

**Saída:**  
```
{'nome': 'Ana', 'idade': 31, 'email': 'ana@email.com'}
```

---

## **Exercício 2: União de Dicionários**  
**Problema:**  
Combine dois dicionários (`d1` e `d2`), priorizando os valores de `d2` em caso de chaves repetidas.  

**Solução:**  
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Método 1: update()
d1.update(d2)

# Método 2: operador ** (Python 3.9+)
d3 = {**d1, **d2}

print("Resultado:", d1)
```

**Explicação:**  
- `update()` modifica `d1` diretamente, substituindo valores de chaves existentes.  
- O operador `**` desempacota os dicionários, combinando-os em um novo (`d3`).  

**Saída:**  
```
Resultado: {'a': 1, 'b': 3, 'c': 4}
```

---

## **Exercício 3: Contador de Frequência**  
**Problema:**  
Conte a frequência de cada palavra na frase:  
`"o rato roeu a roupa do rei de roma"`.  

**Solução:**  
```python
frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)
```

**Explicação:**  
- Usamos `split()` para dividir a frase em palavras.  
- `get(palavra, 0)` retorna 0 se a palavra não existir, evitando `KeyError`.  

**Saída:**  
```
{'o': 1, 'rato': 1, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1, 'de': 1, 'roma': 1}
```

---

## **Exercício 4: Sistema de Banco de Dados de Alunos**  

**Problema:**  
- Crie um dicionário `alunos`:
    -onde cada chave é o **ID do aluno** e 
    - o valor é outro dicionário com:
        - `nome`, 
        - `notas` (lista), e
        - `média`. 
- Adicione 3 alunos e calcule suas médias.  

**Solução:**  
```python
alunos = {}

# Adicionar alunos
alunos[1] = {"nome": "Maria", "notas": [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "João", "notas": [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "Carlos", "notas": [5.5, 6.5, 7.0]}

# Calcular médias
for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media, 2)

print(alunos)
```

**Explicação:** 

- Cada aluno é armazenado como um dicionário aninhado.  
- Usamos um loop para iterar sobre os alunos e calcular a média.  

--- 

## **Exercício 5: Sistema Completo de Gerenciamento de Usuários**  
**Problema:**  
Desenvolva um sistema interativo para gerenciar usuários, com as seguintes funcionalidades:  
1. Adicionar usuário (nome, e-mail).  
2. Remover usuário por e-mail.  
3. Buscar usuário por e-mail.  
4. Listar todos os usuários.  

**Solução:**  
```python
usuarios = {}

def adicionar_usuario():
    nome = input("Nome: ")
    email = input("E-mail: ")
    usuarios[email] = {"nome": nome, "email": email}
    print("Usuário adicionado!")

def remover_usuario():
    email = input("E-mail para remover: ")
    if email in usuarios:
        del usuarios[email]
        print("Usuário removido!")
    else:
        print("E-mail não encontrado.")

def buscar_usuario():
    email = input("E-mail para buscar: ")
    usuario = usuarios.get(email)
    if usuario:
        print(f"Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    else:
        print("Usuário não encontrado.")

def listar_usuarios():
    for email, info in usuarios.items():
        print(f"{info['nome']} - {email}")

while True:
    print("\nMenu:")
    print("1. Adicionar")
    print("2. Remover")
    print("3. Buscar")
    print("4. Listar")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_usuario()
    elif opcao == "2":
        remover_usuario()
    elif opcao == "3":
        buscar_usuario()
    elif opcao == "4":
        listar_usuarios()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
```

**Funcionamento:**  
- **Estrutura**: O dicionário `usuarios` armazena e-mails como chaves e dados do usuário como valores.  
- **Funções**: Cada função corresponde a uma operação (adicionar, remover, etc.).  
- **Loop Principal**: Um menu interativo permite ao usuário escolher ações até sair (opção 5).  

---
