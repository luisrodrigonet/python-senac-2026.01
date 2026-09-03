# **Dicionários em Python**

## **1. Introdução**

Um dicionário em Python é uma estrutura de dados que armazena pares de **chave-valor**. É mutável, dinâmico e otimizado para buscas rápidas. Diferente de listas ou tuplas, que usam índices numéricos, os dicionários usam **chaves únicas** (imutáveis) para acessar valores.

**Características Principais:**
- **Não ordenado** (em versões anteriores ao Python 3.7; a partir dessa versão, mantém a ordem de inserção).
- **Chaves devem ser imutáveis** (strings, números, tuplas).
- **Valores podem ser de qualquer tipo** (listas, outros dicionários, etc.).

**Comparação com Listas:**
- Listas: `[1, 2, 3]` (acesso por índice numérico).
- Dicionários: `{"nome": "Alice", "idade": 30}` (acesso por chave).

---

## **2. Criando Dicionários**

### **Sintaxe Básica**
```python
# Dicionário vazio
d1 = {}
d2 = dict()

# Dicionário com elementos
telefones = {"Alice": "1234-5678", "Bob": "8765-4321"}
```

### **Usando o método `dict()`**
```python
# Usando pares chave-valor
d3 = dict(nome="Carlos", idade=25)

# A partir de uma lista de tuplas
lista_tuplas = [("a", 1), ("b", 2)]
d4 = dict(lista_tuplas)
```

#### **Usando o método `fromkeys()`**
Cria um dicionário com chaves e um valor padrão:

```python
chaves = ["nome", "idade", "cidade"]
valor_padrao = "N/A"
usuario = dict.fromkeys(chaves, valor_padrao)
# Resultado: {'nome': 'N/A', 'idade': 'N/A', 'cidade': 'N/A'}
```

---

## **3. Acessando Elementos**

### **Via Colchetes `[]`**
```python
print(telefones["Alice"])  # Saída: "1234-5678"
```

### **Usando o método `get()`**
Retorna `None` (ou um valor padrão) se a chave não existir:
```python
print(telefones.get("Carlos"))                      # Saída: None
print(telefones.get("Carlos", "Não encontrado"))    # Saída: "Não encontrado"
```

#### **Tratamento de `KeyError`**
Evite erros ao acessar chaves inexistentes:
```python
try:
    print(telefones["Carlos"])
except KeyError:
    print("Chave não existe!")
```

---

## **4. Modificando Dicionários**

### **Adicionar/Atualizar Elementos**
```python
telefones["Carlos"] = "9999-9999"  # Adiciona
telefones["Alice"] = "1111-1111"   # Atualiza
```


### **Remover Elementos**

- `del`: Remove uma chave específica.
  ```python
  del telefones["Bob"]
  ```

- `pop()`: Remove e retorna o valor de uma chave.
  ```python
  valor = telefones.pop("Alice")  # Retorna "1234-5678"
  ```
- `popitem()`: Remove e retorna o último par inserido (Python 3.7+).
  ```python
  chave, valor = telefones.popitem()  # Exemplo: ("Carlos", "9999-9999")
  ```

- `clear()`: Limpa o dicionário.
  ```python
  telefones.clear()
  ```

---

## **5. Iterando sobre Dicionários**

### **Loop Simples**
```python
for chave in telefones.keys():
    print(chave)

for valor in telefones.values():
    print(valor)

for chave, valor in telefones.items():
    print(f"{chave}: {valor}")
```

### **Comprehensions**

Crie novos dicionários de forma concisa:

```python
quadrados = {x: x**2 for x in range(1, 6)}
# Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## **6. Métodos Úteis**

### **copy()**

Cria uma cópia superficial:
```python
copia = telefones.copy()
```

### **update()**

Mescla dois dicionários:
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)  # Resultado: {"a": 1, "b": 3, "c": 4}
```

### **setdefault()**

Define um valor padrão se a chave não existir:
```python
contagem = {}
palavras = ["maçã", "banana", "maçã"]
for palavra in palavras:
    contagem.setdefault(palavra, 0)
    contagem[palavra] += 1
# Resultado: {"maçã": 2, "banana": 1}
```

---

## **7. Funcionalidades Avançadas**

### **Dicionários Aninhados**

Armazene estruturas complexas:

```python
usuarios = {
    "alice": {"nome": "Alice Silva", "idade": 30},
    "bob": {"nome": "Bob Santos", "idade": 25}
}
print(usuarios["alice"]["nome"])  # Saída: "Alice Silva"
```

### **Ordem de Inserção (Python 3.7+)**

Dicionários mantêm a ordem de inserção:
```python
d = {"a": 1, "b": 2}
d["c"] = 3
print(list(d.keys()))  # Saída: ["a", "b", "c"]
```

### **Views (keys, values, items)**

Objetos dinâmicos que refletem mudanças no dicionário:

```python
chaves = telefones.keys()
telefones["Eve"] = "5555-5555"
print(chaves)  # Saída incluirá "Eve"
```

---

## **8. Casos de Uso Comuns**

### **Contagem de Frequência**
```python
texto = "maçã banana maçã laranja banana maçã"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)  # Saída: {'maçã': 3, 'banana': 2, 'laranja': 1}
```

### **Armazenamento de Configurações**
```python
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
```

---

## **9. Considerações de Desempenho**

- Dicionários usam **tabelas hash**, tornando buscas, inserções e exclusões muito eficientes (O(1) em média).

- Ideais para cenários com grandes volumes de dados e acesso frequente.

---

## **10. Erros Comuns e Boas Práticas**

### **Evitando `KeyError`**

Use `get()` ou verifique a existência da chave:
```python
if "Carlos" in telefones:
    print(telefones["Carlos"])
```

### **Chaves Mutáveis**
Só use tipos imutáveis como chaves:
```python
# Erro: TypeError
chave_mutavel = [1, 2]
d = {chave_mutavel: "valor"}  # Inválido!
```

---

## **Conclusão**
Dicionários são ferramentas versáteis para organizar dados de forma eficiente. Dominar suas funcionalidades permite resolver problemas complexos com código limpo e legível. Pratique criando projetos como sistemas de cadastro, contadores de palavras ou integrações com APIs (que frequentemente retornam JSON como dicionários).