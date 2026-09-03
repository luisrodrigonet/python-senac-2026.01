# Aula 11 - Tarefa 02 - Orientação a Objetos
> A seguir, vamos explorar o **conceito de Orientação a Objetos (OO)** em Python. 
> 
> Além disso, vamos relembrar os **métodos dos dicionários** – ferramentas poderosas para gerenciar dados – e, ao final, propor uma série de exercícios para fixação. 
> 

## :one:  Conceito de Orientação a Objetos

### :mega: O que é Orientação a Objetos? 

A **Orientação a Objetos** é um paradigma de programação que utiliza *objetos* para modelar entidades do mundo real. Cada objeto possui **atributos** (dados) e **métodos** (comportamentos). No nosso exemplo, um objeto pode ser uma *Conta Bancária*.

A `OO` é amplamente utilizada porque facilita a organização, reutilização e manutenção do código.

### :loudspeaker: Conceitos Básicos de Orientação a Objetos

- **Classe**: 
  - Uma classe é um modelo para criar objetos. 
  - Ela define os atributos (dados) e métodos (comportamentos) que os objetos terão.
  
- **Objeto**: 
  - Um objeto é uma instância de uma classe. 
  - Quando você cria um objeto, você está criando uma "**cópia**" da classe com seus próprios valores para os atributos.

- **Atributos**: 
  - São variáveis que pertencem a um objeto ou classe. 
  - Eles armazenam dados específicos do objeto.

- **Métodos**: 
  - São funções que pertencem a um objeto ou classe.
  - Eles definem o comportamento do objeto.

- **Encapsulamento**: 
  - É o conceito de esconder os detalhes internos de como um objeto funciona, expondo apenas uma interface para interagir com ele.

- **Herança**: 
  - Permite que uma classe herde atributos e métodos de outra classe, promovendo a reutilização de código.

- **Polimorfismo**: 
  - Permite que objetos de diferentes classes sejam tratados como objetos de uma classe base comum, mas cada um pode se comportar de maneira diferente.

Vamos criar um exemplo simples para ilustrar esses conceitos.

### :snake: Criando uma Classe em Python

```python
# Definindo uma classe chamada 'Carro'
class Carro:
    # Método construtor (__init__) para inicializar os atributos
    def __init__(self, marca, modelo, ano):
        self.marca = marca      # Atributo
        self.modelo = modelo    # Atributo
        self.ano = ano          # Atributo
        self.ligado = False     # Atributo com valor padrão

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} está desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    # Método para exibir informações do carro
    def exibir_info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Usando métodos do objeto
meu_carro.exibir_info()  # Exibe as informações do carro
meu_carro.ligar()  # Liga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente
meu_carro.desligar()  # Desliga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente
```

#### :star: Explicação do Código:

1. **Classe `Carro`**: 
   - Definimos uma classe chamada `Carro` com um método construtor `__init__` que inicializa os atributos `marca`, `modelo`, `ano` e `ligado`.

2. **Atributos**: 
    - `marca`, `modelo`, `ano` e `ligado` são atributos da classe `Carro`.

3. **Métodos**: 
   - `ligar()`, `desligar()` e `exibir_info()` são métodos que definem o comportamento do objeto `Carro`.

4. **Objeto `meu_carro`**:
   - Criamos um objeto `meu_carro` da classe `Carro` e utilizamos seus métodos para interagir com ele.

### :snake: Encapsulamento em Python

O `encapsulamento` é alcançado em Python usando convenções de nomenclatura. Atributos e métodos que começam com um sublinhado (`_`) são considerados privados, embora ainda possam ser acessados.

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._ligado = False  # Atributo "privado"

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f"{self.marca} {self.modelo} está desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def exibir_info(self):
        status = "ligado" if self._ligado else "desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.")
```

### :snake: Herança em Python

A `herança` permite que uma classe herde atributos e métodos de outra classe.

```python
# Classe base (superclasse)
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")

# Classe derivada (subclasse)
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da superclasse
        self.portas = portas

    def exibir_info(self):
        super().exibir_info()  # Chama o método da superclasse
        print(f"Este carro tem {self.portas} portas.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, 4)
meu_carro.exibir_info()
```

### :snake: Polimorfismo em Python

O `polimorfismo` permite que objetos de diferentes classes sejam tratados como objetos de uma classe base comum.

```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

# Função que usa polimorfismo
def fazer_barulho(animal):
    animal.fazer_som()

# Criando objetos
meu_cachorro = Cachorro()
meu_gato = Gato()

# Usando a função com diferentes objetos
fazer_barulho(meu_cachorro)  # Saída: Au Au!
fazer_barulho(meu_gato)  # Saída: Miau!
```

### :bulb:Exemplo Prático: **Classes para Conta e Banco**

Imagine as seguintes classes:

- **Classe `Conta`**: Representa a conta de um cliente. Possui atributos como número da conta, nome do titular e saldo, e métodos para depositar, sacar e exibir informações.

- **Classe `Banco`**: Gerencia várias contas. Utiliza um dicionário para mapear números de contas aos objetos `Conta`.

#### Código Exemplo :snake:

```python
class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado na conta {self.numero}.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado na conta {self.numero}.")

    def exibir_dados(self):
        return f"Conta {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

    def __str__(self):
        return self.exibir_dados()


class Banco:
    def __init__(self):
        # Usamos um dicionário para armazenar as contas: chave é o número da conta
        self.contas = {}

    def adicionar_conta(self, conta):
        if conta.numero in self.contas:
            print("Conta já cadastrada!")
        else:
            self.contas[conta.numero] = conta
            print(f"Conta {conta.numero} adicionada com sucesso!")

    def depositar(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada!")

    def sacar(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada!")

    def transferir(self, origem, destino, valor):
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)
        if not conta_origem or not conta_destino:
            print("Conta(s) não encontrada(s)!")
            return
        if conta_origem.saldo >= valor:
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} de {origem} para {destino} realizada com sucesso!")
        else:
            print("Saldo insuficiente para transferência!")

    def listar_contas(self):
        print("\n--- Lista de Contas ---")
        for conta in self.contas.values():
            print(conta)
        print("-----------------------\n")


# Exemplo de uso:
banco = Banco()
conta1 = Conta("001", "Alice", 1000.0)
conta2 = Conta("002", "Bruno", 1500.0)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

banco.depositar("001", 500.0)
banco.sacar("002", 200.0)
banco.transferir("001", "002", 300.0)

banco.listar_contas()
```

> :robot: **Dica:** Pense na classe `Banco` como um gerente que usa um **dicionário** para mapear cada conta (por seu número) a um objeto `Conta`.


## :two: Lista de Exercícios

### 1. **Criação de Classe Conta:**  
   
   Crie uma classe `Conta` com atributos: número, titular e saldo. Implemente os métodos:
   - `depositar(valor)`
   - `sacar(valor)` (com verificação de saldo)
   - `exibir_dados()`
   
 :snake: Codigo

```python
class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def exibir_dados(self):
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
```

**Explicação:**

1. **Classe `Conta`:**
   - **Atributos:**
     - `numero`: Número da conta.
     - `titular`: Nome do titular da conta.
     - `saldo`: Saldo atual da conta (inicializado com 0.0 por padrão).

2. **Métodos:**
   - **`__init__(self, numero, titular, saldo=0.0)`:**
     - Construtor que inicializa os atributos da conta. O `saldo` é opcional e assume 0.0 se não fornecido.

   - **`depositar(self, valor)`:**
     - Adiciona o `valor` ao saldo da conta.

   - **`sacar(self, valor)`:**
     - Verifica se o saldo é suficiente para o saque. Se sim, subtrai o `valor` do saldo.

   - **`exibir_dados(self)`:**
     - Exibe os dados da conta (número, titular e saldo) formatados.

**Notas:**
- O método `sacar` não realiza o saque se o saldo for insuficiente, garantindo a verificação de saldo.
- O método `exibir_dados` imprime os dados formatados, mas pode ser adaptado para retornar uma string se necessário.  
   

### 2. **Instanciação e Impressão:**  

**Atividade**:
- Instancie dois objetos da classe `Conta` e exiba seus dados usando o método `exibir_dados()`.

:snake: Codigo

```python
# Criando duas contas
conta1 = Conta(12345, "Ana Costa", 1500.0)
conta2 = Conta(67890, "Carlos Oliveira")

# Exibindo os dados das contas
print("=== Conta 1 ===")
conta1.exibir_dados()

print("\n=== Conta 2 ===")
conta2.exibir_dados()
```
**Explicação:**
- O método `exibir_dados()` mostra as informações atualizadas de cada conta
- Os `print("\n")` são usados apenas para separar visualmente as duas contas na saída

### 3. **Criação da Classe Banco com Dicionário:**  

**Atividade**:
 - Crie uma classe `Banco` que possua um atributo dicionário para armazenar as contas. Implemente o método `adicionar_conta(conta)`.

```python
class Banco:
    def __init__(self):
        self.contas = {}  # Dicionário: número da conta -> objeto Conta

    def adicionar_conta(self, conta):
        """Adiciona uma conta ao dicionário usando o número como chave"""
        self.contas[conta.numero] = conta
```

**Explicação:**

1. **Atributo `contas`:**
   - Um dicionário que armazena as contas cadastradas no banco
   - A **chave** é o número da conta (`conta.numero`)
   - O **valor** é o próprio objeto `Conta`

2. **Método `adicionar_conta(conta)`:**
   - Recebe um objeto do tipo `Conta` como parâmetro
   - Adiciona a conta ao dicionário usando seu número como chave
   - Permite acesso rápido às contas pelo número

**Exemplo de uso integrado com a classe `Conta`:**

```python
# Criando um banco
meu_banco = Banco()

# Criando duas contas
conta_a = Conta(111, "Maria Souza", 2000)
conta_b = Conta(222, "Pedro Rocha")

# Adicionando as contas ao banco
meu_banco.adicionar_conta(conta_a)
meu_banco.adicionar_conta(conta_b)

# Acessando uma conta específica pelo número:
minha_conta = meu_banco.contas[111]
minha_conta.exibir_dados()
```

**Funcionalidade adicional implícita:**
- Evita duplicatas naturalmente (se adicionar duas contas com o mesmo número, a última sobrescreve a anterior)
- Permite buscar contas instantaneamente usando `meu_banco.contas[numero]`

### 4. **Operação de Depósito:**  

**Atividade**:
- No objeto `Banco`, implemente um método `depositar(numero, valor)` que encontre a conta e chame o método `depositar` da classe `Conta`.


```python
class Banco:
    def __init__(self):
        self.contas = {}  # Dicionário: número da conta -> objeto Conta

    def adicionar_conta(self, conta):
        """Adiciona uma conta ao dicionário usando o número como chave"""
        self.contas[conta.numero] = conta

    def depositar(self, numero, valor):
        """Deposita um valor em uma conta específica"""
        if numero in self.contas:
            self.contas[numero].depositar(valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")
```

**Explicação detalhada:**

1. **Verificação de existência da conta:**
   - Primeiro verifica se o número da conta existe no dicionário `self.contas`
   - Usa a expressão `numero in self.contas` para esta verificação

2. **Depósito em conta existente:**
   - Se a conta existe, acessa o objeto `Conta` através de `self.contas[numero]`
   - Chama o método `depositar(valor)` da instância de `Conta`

3. **Feedback ao usuário:**
   - Retorna mensagem de sucesso com o valor depositado
   - Formata o valor com 2 casas decimais (`:.2f`)

4. **Tratamento de conta não encontrada:**
   - Se a conta não existir, informa ao usuário com uma mensagem clara

**Exemplo de uso completo:**

```python
# Criando banco e contas
banco = Banco()
banco.adicionar_conta(Conta(123, "João Silva", 500))
banco.adicionar_conta(Conta(456, "Maria Santos"))

# Realizando depósitos
banco.depositar(123, 200)  # Depósito em conta existente
banco.depositar(999, 100)  # Tentativa em conta inexistente

# Verificando saldo
banco.contas[123].exibir_dados()
```

**Melhorias possíveis:**
- Poderíamos retornar `True/False` para indicar sucesso/fracasso
- Poderíamos lançar uma exceção para contas não encontradas
- Poderíamos adicionar validação para valores negativos

### 5. **Operação de Saque:**  

**Atividade**:
- Implemente no `Banco` o método `sacar(numero, valor)` que realize a operação de saque na conta informada.


```python
class Banco:
    def __init__(self):
        self.contas = {}  # Dicionário: número da conta -> objeto Conta

    def adicionar_conta(self, conta):
        self.contas[conta.numero] = conta

    def depositar(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].depositar(valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def sacar(self, numero, valor):
        """Realiza saque em uma conta específica"""
        if numero in self.contas:
            conta = self.contas[numero]
            if conta.saldo >= valor:  # Verifica se há saldo suficiente
                conta.sacar(valor)
                print(f"Saque de R${valor:.2f} realizado na conta {numero}")
            else:
                print(f"Saldo insuficiente na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")
```

**Explicação detalhada:**

1. **Verificação da conta:**
   - Primeiro verifica se a conta existe no dicionário `self.contas`

2. **Verificação de saldo:**
   - Se a conta existe, verifica se o saldo é suficiente para o saque
   - Aproveita a verificação já implementada na classe `Conta`

3. **Operação de saque:**
   - Se todas as condições forem atendidas, chama o método `sacar` da conta

4. **Feedback ao usuário:**
   - Mensagens informativas para cada caso:
     - Saque realizado com sucesso
     - Saldo insuficiente
     - Conta não encontrada

**Exemplo de uso completo:**

```python
# Criando banco e contas
banco = Banco()
banco.adicionar_conta(Conta(123, "João Silva", 1000))
banco.adicionar_conta(Conta(456, "Maria Santos", 500))

# Realizando operações
banco.sacar(123, 300)   # Saque com sucesso
banco.sacar(123, 800)   # Saldo insuficiente
banco.sacar(999, 100)   # Conta inexistente

# Verificando saldo
banco.contas[123].exibir_dados()
```

**Melhorias adicionais:**

1. Poderíamos criar um método `consultar_saldo(numero)` no Banco
2. Implementar um limite diário de saque
3. Registrar um histórico de transações
4. Retornar um booleano indicando sucesso/fracasso da operação


### 6. **Listagem de Contas:**  
**Atividade**:
- Crie um método `listar_contas()` na classe `Banco` que imprima as informações de todas as contas cadastradas.

```python
class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        self.contas[conta.numero] = conta

    def depositar(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].depositar(valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def sacar(self, numero, valor):
        if numero in self.contas:
            conta = self.contas[numero]
            if conta.saldo >= valor:
                conta.sacar(valor)
                print(f"Saque de R${valor:.2f} realizado na conta {numero}")
            else:
                print(f"Saldo insuficiente na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def listar_contas(self):
        """Lista todas as contas cadastradas no banco"""
        print("\n=== LISTA DE CONTAS CADASTRADAS ===")
        if not self.contas:
            print("Nenhuma conta cadastrada no sistema.")
        else:
            for numero, conta in self.contas.items():
                print("\n---")
                conta.exibir_dados()
        print("\n===")
```

**Funcionamento do método `listar_contas()`:**

1. Verifica se existem contas cadastradas (`if not self.contas`)
2. Se não houver contas, exibe uma mensagem informativa
3. Para cada conta no dicionário `self.contas`:
   - Imprime um separador visual (`---`)
   - Chama o método `exibir_dados()` da conta
4. No final, imprime outro separador visual (`===`)

**Exemplo de uso:**

```python
# Criando banco e contas
banco = Banco()
banco.adicionar_conta(Conta(101, "Cliente A", 1500))
banco.adicionar_conta(Conta(202, "Cliente B", 3200))
banco.adicionar_conta(Conta(303, "Cliente C"))

# Listando todas as contas
banco.listar_contas()
```

**Melhorias possíveis:**

1. Adicionar numeração das contas na listagem
2. Incluir o total de contas cadastradas
3. Formatar a saída em forma de tabela
4. Adicionar filtros (por saldo mínimo, por letra do nome, etc.)


### 7. **Transferência entre Contas:**  

- Na classe `Banco`, implemente o método `transferir(origem, destino, valor)` que verifique se a conta de origem possui saldo suficiente para transferir para a conta de destino.


```python
class Banco:
    # ... (métodos anteriores permanecem os mesmos)

    def transferir(self, origem, destino, valor):
        """Realiza transferência entre contas"""
        if origem not in self.contas:
            print(f"Conta de origem {origem} não encontrada!")
            return False
        
        if destino not in self.contas:
            print(f"Conta de destino {destino} não encontrada!")
            return False
        
        if origem == destino:
            print("Não é possível transferir para a mesma conta!")
            return False
        
        conta_origem = self.contas[origem]
        conta_destino = self.contas[destino]
        
        if conta_origem.saldo < valor:
            print(f"Saldo insuficiente na conta {origem} para transferência")
            return False
        
        # Realiza a transferência
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
        
        print(f"Transferência de R${valor:.2f} realizada:")
        print(f"  Origem: {origem} - Novo saldo: R${conta_origem.saldo:.2f}")
        print(f"  Destino: {destino} - Novo saldo: R${conta_destino.saldo:.2f}")
        return True
```

**Funcionamento detalhado:**

1. **Verificação das contas:**
   - Verifica se ambas as contas (origem e destino) existem
   - Verifica se não é a mesma conta

2. **Verificação de saldo:**
   - Confere se a conta de origem tem saldo suficiente

3. **Execução da transferência:**
   - Se todas as condições forem atendidas:
     - Realiza saque na conta de origem
     - Realiza depósito na conta de destino

4. **Feedback:**
   - Retorna `True` se a transferência foi bem-sucedida
   - Retorna `False` se houve algum problema
   - Imprime mensagens detalhadas sobre cada etapa

**Exemplo de uso:**

```python
banco = Banco()
banco.adicionar_conta(Conta(111, "Cliente X", 1000))
banco.adicionar_conta(Conta(222, "Cliente Y", 500))

# Transferência válida
banco.transferir(111, 222, 300)

# Tentativas inválidas
banco.transferir(111, 333, 200)  # Conta destino inexistente
banco.transferir(111, 111, 100)   # Mesma conta
banco.transferir(111, 222, 800)   # Saldo insuficiente

# Verificando saldos
banco.listar_contas()
```

**Melhorias possíveis:**

1. Adicionar taxa de transferência
2. Implementar limite de transferência diário
3. Registrar histórico de transferências
4. Permitir transferências entre bancos diferentes (seria necessário implementar TED/DOC)

### 8. **Menu Interativo:**  

**Atividade**:
- Crie um programa que exiba um menu interativo permitindo:
   - Cadastrar contas
   - Listar contas
   - Realizar depósitos, saques e transferências  
- Utilize as classes `Conta` e `Banco` desenvolvidas.


```python
class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def exibir_dados(self):
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        self.contas[conta.numero] = conta

    def depositar(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].depositar(valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def sacar(self, numero, valor):
        if numero in self.contas:
            if self.contas[numero].sacar(valor):
                print(f"Saque de R${valor:.2f} realizado na conta {numero}")
            else:
                print(f"Saldo insuficiente na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def transferir(self, origem, destino, valor):
        if origem not in self.contas:
            print(f"Conta de origem {origem} não encontrada!")
            return False
        
        if destino not in self.contas:
            print(f"Conta de destino {destino} não encontrada!")
            return False
        
        if origem == destino:
            print("Não é possível transferir para a mesma conta!")
            return False
        
        conta_origem = self.contas[origem]
        conta_destino = self.contas[destino]
        
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
            print(f"  Origem: {origem} - Novo saldo: R${conta_origem.saldo:.2f}")
            print(f"  Destino: {destino} - Novo saldo: R${conta_destino.saldo:.2f}")
            return True
        else:
            print(f"Saldo insuficiente na conta {origem} para transferência")
            return False

    def listar_contas(self):
        print("\n=== LISTA DE CONTAS ===")
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in self.contas.values():
                print("\n---")
                conta.exibir_dados()
        print("\n=====================")


def main():
    banco = Banco()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar nova conta")
        print("2. Listar todas as contas")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Realizar transferência")
        print("6. Sair do sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE CONTA ---")
            numero = int(input("Número da conta: "))
            titular = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial (opcional, pressione Enter para 0): ") or 0)
            banco.adicionar_conta(Conta(numero, titular, saldo_inicial))
            print("Conta cadastrada com sucesso!")
            
        elif opcao == "2":
            banco.listar_contas()
            
        elif opcao == "3":
            print("\n--- DEPÓSITO ---")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a depositar: R$"))
            banco.depositar(numero, valor)
            
        elif opcao == "4":
            print("\n--- SAQUE ---")
            numero = int(input("Número da conta: "))
            valor = float(input("Valor a sacar: R$"))
            banco.sacar(numero, valor)
            
        elif opcao == "5":
            print("\n--- TRANSFERÊNCIA ---")
            origem = int(input("Conta de origem: "))
            destino = int(input("Conta de destino: "))
            valor = float(input("Valor a transferir: R$"))
            banco.transferir(origem, destino, valor)
            
        elif opcao == "6":
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
```

**Funcionalidades do sistema:**

1. **Cadastro de contas**:
   - Solicita número da conta, nome do titular e saldo inicial
   - Cria uma nova instância de `Conta` e adiciona ao `Banco`

2. **Listagem de contas**:
   - Exibe todas as contas cadastradas com seus dados completos

3. **Operações bancárias**:
   - **Depósito**: Adiciona valor a uma conta existente
   - **Saque**: Remove valor de uma conta (com verificação de saldo)
   - **Transferência**: Move valor entre contas (com todas as validações)

4. **Tratamento de erros**:
   - Verifica existência das contas
   - Valida saldo suficiente para saques e transferências
   - Impede transferências para a mesma conta

5. **Interface amigável**:
   - Menu limpo e organizado
   - Mensagens claras para o usuário
   - Formatação de valores monetários

**Como usar:**
1. Execute o programa
2. Escolha as opções do menu usando números de 1 a 6
3. Siga as instruções para cada operação
4. Todas as operações são validadas antes de serem executadas

O sistema mantém todas as contas em memória enquanto estiver em execução, permitindo múltiplas operações até que o usuário escolha sair.


### 9. **Persistência Simples:** 
**Atividade**:
- Modifique o programa para salvar os dados das contas em um arquivo (por exemplo, usando o módulo `json`). Ao iniciar o programa, carregue os dados salvos e, ao sair, salve as alterações.


```python
import json
import os

class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def to_dict(self):
        return {
            'numero': self.numero,
            'titular': self.titular,
            'saldo': self.saldo
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['numero'], data['titular'], data['saldo'])

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def exibir_dados(self):
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")


class Banco:
    ARQUIVO_DADOS = 'contas_bancarias.json'

    def __init__(self):
        self.contas = {}
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.ARQUIVO_DADOS):
            try:
                with open(self.ARQUIVO_DADOS, 'r') as f:
                    contas_data = json.load(f)
                    for conta_data in contas_data.values():
                        conta = Conta.from_dict(conta_data)
                        self.contas[conta.numero] = conta
                print("Dados das contas carregados com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")

    def salvar_dados(self):
        try:
            contas_data = {num: conta.to_dict() for num, conta in self.contas.items()}
            with open(self.ARQUIVO_DADOS, 'w') as f:
                json.dump(contas_data, f, indent=2)
            print("Dados das contas salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def adicionar_conta(self, conta):
        self.contas[conta.numero] = conta

    def depositar(self, numero, valor):
        if numero in self.contas:
            self.contas[numero].depositar(valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def sacar(self, numero, valor):
        if numero in self.contas:
            if self.contas[numero].sacar(valor):
                print(f"Saque de R${valor:.2f} realizado na conta {numero}")
            else:
                print(f"Saldo insuficiente na conta {numero}")
        else:
            print(f"Conta {numero} não encontrada!")

    def transferir(self, origem, destino, valor):
        if origem not in self.contas:
            print(f"Conta de origem {origem} não encontrada!")
            return False
        
        if destino not in self.contas:
            print(f"Conta de destino {destino} não encontrada!")
            return False
        
        if origem == destino:
            print("Não é possível transferir para a mesma conta!")
            return False
        
        conta_origem = self.contas[origem]
        conta_destino = self.contas[destino]
        
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
            print(f"  Origem: {origem} - Novo saldo: R${conta_origem.saldo:.2f}")
            print(f"  Destino: {destino} - Novo saldo: R${conta_destino.saldo:.2f}")
            return True
        else:
            print(f"Saldo insuficiente na conta {origem} para transferência")
            return False

    def listar_contas(self):
        print("\n=== LISTA DE CONTAS ===")
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in self.contas.values():
                print("\n---")
                conta.exibir_dados()
        print("\n=====================")


def main():
    banco = Banco()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar nova conta")
        print("2. Listar todas as contas")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Realizar transferência")
        print("6. Sair do sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE CONTA ---")
            try:
                numero = int(input("Número da conta: "))
                titular = input("Nome do titular: ")
                saldo_inicial = float(input("Saldo inicial (opcional, pressione Enter para 0): ") or 0)
                banco.adicionar_conta(Conta(numero, titular, saldo_inicial))
                print("Conta cadastrada com sucesso!")
            except ValueError:
                print("Erro: Valor inválido inserido!")
            
        elif opcao == "2":
            banco.listar_contas()
            
        elif opcao == "3":
            print("\n--- DEPÓSITO ---")
            try:
                numero = int(input("Número da conta: "))
                valor = float(input("Valor a depositar: R$"))
                banco.depositar(numero, valor)
            except ValueError:
                print("Erro: Valor inválido inserido!")
            
        elif opcao == "4":
            print("\n--- SAQUE ---")
            try:
                numero = int(input("Número da conta: "))
                valor = float(input("Valor a sacar: R$"))
                banco.sacar(numero, valor)
            except ValueError:
                print("Erro: Valor inválido inserido!")
            
        elif opcao == "5":
            print("\n--- TRANSFERÊNCIA ---")
            try:
                origem = int(input("Conta de origem: "))
                destino = int(input("Conta de destino: "))
                valor = float(input("Valor a transferir: R$"))
                banco.transferir(origem, destino, valor)
            except ValueError:
                print("Erro: Valor inválido inserido!")
            
        elif opcao == "6":
            banco.salvar_dados()
            print("Dados salvos. Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
```

**Principais modificações:**

1. **Serialização das contas**:
   - Adicionado método `to_dict()` na classe `Conta` para converter para dicionário
   - Adicionado método de classe `from_dict()` para criar instâncias a partir de dicionários

2. **Persistência de dados**:
   - Classe `Banco` agora tem constante `ARQUIVO_DADOS` com o nome do arquivo JSON
   - Método `carregar_dados()` lê o arquivo ao iniciar o programa
   - Método `salvar_dados()` escreve no arquivo ao sair do programa

3. **Tratamento de erros**:
   - Verifica se o arquivo existe antes de tentar carregar
   - Trata possíveis erros de leitura/escrita do arquivo
   - Adicionado tratamento de erros para entradas inválidas no menu

4. **Mensagens informativas**:
   - Informa quando os dados são carregados/salvos com sucesso
   - Mostra mensagens de erro específicas quando ocorrem problemas

**Funcionamento:**

1. **Ao iniciar**:
   - O programa tenta carregar os dados do arquivo `contas_bancarias.json`
   - Se o arquivo não existir, começa com uma lista vazia de contas

2. **Durante a execução**:
   - Todas as operações são feitas em memória como antes
   - Os dados só são persistidos no arquivo ao sair do programa

3. **Ao sair**:
   - Todos os dados são salvos no arquivo JSON
   - O arquivo é sobrescrito com os dados atuais

O arquivo JSON gerado terá um formato como:
```json
{
  "123": {
    "numero": 123,
    "titular": "João Silva",
    "saldo": 1000.0
  },
  "456": {
    "numero": 456,
    "titular": "Maria Santos",
    "saldo": 2500.0
  }
}
```

Esta implementação mantém todos os dados entre execuções do programa de forma simples e eficiente.

### 10. **Exercício com Dicionários:**  
**Atividade**:
- Crie uma função que receba um dicionário de contas (chave: número da conta, valor: objeto `Conta`) e retorne um novo dicionário onde as chaves sejam os nomes dos titulares e os valores, os saldos.

```python
def contas_por_titular(contas):
    """
    Converte um dicionário de contas (número: objeto Conta) em um dicionário
    com titulares como chaves e saldos como valores.
    
    Args:
        contas (dict): Dicionário original de contas (número: Conta)
        
    Returns:
        dict: Novo dicionário no formato {titular: saldo}
    """
    return {conta.titular: conta.saldo for conta in contas.values()}
```

**Exemplo de uso:**

```python
# Criando algumas contas de exemplo
banco = Banco()
banco.adicionar_conta(Conta(101, "João Silva", 1500.0))
banco.adicionar_conta(Conta(102, "Maria Santos", 3200.0))
banco.adicionar_conta(Conta(103, "João Silva", 500.0))  # Titular repetido

# Usando a função
contas_por_titular = contas_por_titular(banco.contas)
print(contas_por_titular)
```

**Saída:**
```python
{
    'João Silva': 500.0,  # Observação: sobrescreveu o primeiro João Silva
    'Maria Santos': 3200.0
}
```

**Observações importantes:**

1. **Sobrescrita de titulares iguais**:
   - Se houver mais de uma conta com o mesmo titular, a última conta será a que permanecerá no dicionário resultante
   - Isso ocorre porque dicionários não podem ter chaves duplicadas

2. **Versão alternativa que agrupa saldos**:
   ```python
   from collections import defaultdict

   def contas_por_titular_com_agregacao(contas):
       """Versão que soma saldos de titulares iguais"""
       resultado = defaultdict(float)
       for conta in contas.values():
           resultado[conta.titular] += conta.saldo
       return dict(resultado)
   ```

3. **Uso típico**:
   - Essa função é útil para relatórios ou análises onde você precisa agrupar informações por titular
   - Pode ser combinada com outras funções para gerar estatísticas bancárias

**Como integrar na classe Banco:**
Você pode adicionar como método da classe Banco:

```python
class Banco:
    # ... outros métodos ...
    
    def obter_contas_por_titular(self):
        """Retorna dicionário com titulares e seus saldos"""
        return {conta.titular: conta.saldo for conta in self.contas.values()}
```

### 11. **Relatório de Contas:**  
**Atividade**:
- Implemente uma função que gere um relatório ordenado pelo saldo das contas. Utilize métodos dos dicionários e técnicas de ordenação.


```python
def gerar_relatorio_ordenado(contas):
    """
    Gera um relatório das contas ordenado pelo saldo (do maior para o menor)
    
    Args:
        contas (dict): Dicionário de contas (número: objeto Conta)
        
    Returns:
        list: Lista de tuplas (titular, saldo) ordenada por saldo decrescente
    """
    # Converte para lista de tuplas (titular, saldo) e ordena
    contas_lista = [(conta.titular, conta.saldo) for conta in contas.values()]
    
    # Ordena pelo saldo (decrescente) e depois pelo nome (crescente)
    contas_ordenadas = sorted(contas_lista, 
                             key=lambda item: (-item[1], item[0]))
    
    return contas_ordenadas
```

**ersão alternativa como método da classe Banco:**

```python
class Banco:
    # ... (outros métodos existentes)
    
    def gerar_relatorio_saldos(self):
        """
        Gera relatório ordenado de contas por saldo (maior para menor)
        e em caso de empate, ordena por nome do titular (A-Z)
        
        Returns:
            list: Lista de dicionários com os dados ordenados
        """
        # Extrai os dados relevantes de cada conta
        dados_contas = [{'titular': conta.titular,
                         'saldo': conta.saldo,
                         'numero': conta.numero} 
                        for conta in self.contas.values()]
        
        # Ordena por saldo (decrescente) e titular (crescente)
        dados_ordenados = sorted(dados_contas,
                               key=lambda x: (-x['saldo'], x['titular']))
        
        return dados_ordenados
```

**Exemplo de uso:**

```python
# Criando banco e contas de exemplo
banco = Banco()
banco.adicionar_conta(Conta(101, "João Silva", 1500))
banco.adicionar_conta(Conta(102, "Maria Santos", 5000))
banco.adicionar_conta(Conta(103, "Carlos Oliveira", 1500))
banco.adicionar_conta(Conta(104, "Ana Costa", 3000))

# Gerando relatório
relatorio = banco.gerar_relatorio_saldos()

# Exibindo relatório formatado
print("\n=== RELATÓRIO DE CONTAS POR SALDO ===")
print("{:<20} {:<15} {:<10}".format("Titular", "Número", "Saldo"))
print("-" * 45)
for conta in relatorio:
    print("{:<20} {:<15} R${:<10.2f}".format(
        conta['titular'],
        conta['numero'],
        conta['saldo']))
```

**Funcionalidades:**

1. **Ordenação principal**: Por saldo (do maior para o menor)
2. **Critério de desempate**: Por nome do titular (ordem alfabética)
3. **Formatação de saída**: Relatório tabular bem formatado
4. **Flexibilidade**: Retorna tanto uma lista simples quanto um relatório completo

**Técnicas utilizadas:**

1. **List comprehension** para extrair dados das contas
2. **Função sorted()** com chave de ordenação composta
3. **Lambda functions** para definir os critérios de ordenação
4. **Formatação de strings** para alinhamento tabular
5. **Manipulação de dicionários** para organização dos dados


### 12. **Validação de Dados:**  
**Atividade**:
- Ao cadastrar uma nova conta, valide se o número da conta já existe no dicionário. Caso exista, exiba uma mensagem de erro e não cadastre novamente.


```python
class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        """Adiciona uma nova conta, verificando se o número já existe"""
        if conta.numero in self.contas:
            print(f"\nErro: Já existe uma conta com o número {conta.numero} cadastrada!")
            print("Cadastro não realizado. Por favor, use um número diferente.")
            return False
        else:
            self.contas[conta.numero] = conta
            print(f"\nConta {conta.numero} cadastrada com sucesso para {conta.titular}!")
            return True
```

E a modificação correspondente no menu principal:

```python
def main():
    banco = Banco()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar nova conta")
        # ... (outras opções do menu)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE CONTA ---")
            try:
                numero = int(input("Número da conta: "))
                
                # Verifica se a conta já existe antes de prosseguir
                if numero in banco.contas:
                    print(f"\nErro: A conta {numero} já existe!")
                    continue
                    
                titular = input("Nome do titular: ")
                saldo_inicial = float(input("Saldo inicial (opcional, pressione Enter para 0): ") or 0)
                
                nova_conta = Conta(numero, titular, saldo_inicial)
                banco.adicionar_conta(nova_conta)
                
            except ValueError:
                print("Erro: Valor inválido inserido!")
```

**Funcionamento detalhado:**

1. **Validação em duas camadas**:
   - Primeiro verifica no input do usuário
   - Depois valida novamente no método `adicionar_conta`

2. **Mensagens claras**:
   - Informa quando há duplicação
   - Exibe feedback positivo no sucesso

3. **Fluxo controlado**:
   - Retorna `False` em caso de erro
   - Retorna `True` no sucesso
   - Usa `continue` para reiniciar o loop do menu

**Melhorias adicionais:**

1. **Versão com tentativas**:
    ```python
    tentativas = 3
    while tentativas > 0:
        numero = int(input("Número da conta: "))
        if numero not in banco.contas:
            break
        print(f"Conta {numero} já existe! ({tentativas-1} tentativas restantes)")
        tentativas -= 1
    else:
        print("Número máximo de tentativas excedido!")
        continue
    ```

2. **Sugestão automática**:
    ```python
    if numero in banco.contas:
        sugestao = max(banco.contas.keys()) + 1
        print(f"Erro: Conta já existe. Sugestão: {sugestao}")
        continue
    ```


### 14. **Métodos Especiais:**  
**Atividade**:
-  Adicione o método especial `__str__` na classe `Conta` para facilitar a exibição dos dados da conta, e teste-o chamando a função `print()` diretamente sobre o objeto.

```python
class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        """Método especial para representação em string da conta"""
        return (f"Conta Bancária:\n"
                f"  Número: {self.numero}\n"
                f"  Titular: {self.titular}\n"
                f"  Saldo: R${self.saldo:.2f}")

    # ... (outros métodos da classe Conta permanecem iguais)
```

**Testando a implementação:**

```python
# Criando uma conta de teste
minha_conta = Conta(12345, "Ana Silva", 1500.75)

# Chamando print() diretamente no objeto
print("\n=== TESTE DO MÉTODO __str__ ===")
print(minha_conta)

# Saída esperada:
"""
=== TESTE DO MÉTODO __str__ ===
Conta Bancária:
  Número: 12345
  Titular: Ana Silva
  Saldo: R$1500.75
"""
```

**Funcionalidades do método `__str__`:**

1. **Formatação amigável**:
   - Organiza os dados em linhas separadas
   - Formata o saldo com 2 casas decimais

2. **Uso automático**:
   - É chamado automaticamente pelo `print()`
   - Também usado por outras funções que esperam uma representação em string

3. **Vantagens**:
   - Substitui a necessidade do método `exibir_dados()`
   - Permite usar a conta diretamente em f-strings: `f"Detalhes: {minha_conta}"`

**Versão alternativa mais compacta:**

```python
def __str__(self):
    return f"Conta {self.numero} | {self.titular} | Saldo: R${self.saldo:.2f}"
```

**Integração com o sistema existente:**

1. Você pode agora simplificar o método `listar_contas()` da classe `Banco`:

```python
def listar_contas(self):
    print("\n=== LISTA DE CONTAS ===")
    if not self.contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in self.contas.values():
            print("\n" + str(conta))  # Chama __str__ automaticamente
    print("\n=====================")
```

2. E também simplificar outras exibições de conta pelo sistema.


### 15. **Calculadora de Juros:**  
**Atividade**:
-  Crie um método na classe `Conta` que calcule e atualize o saldo com juros simples, recebendo a taxa de juros e o número de períodos como parâmetros.


```python
class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def aplicar_juros_simples(self, taxa, periodos):
        """
        Calcula e aplica juros simples ao saldo da conta
        
        Args:
            taxa (float): Taxa de juros por período (em decimal, ex: 0.05 para 5%)
            periodos (int): Número de períodos de aplicação
            
        Returns:
            float: Valor dos juros calculados
        """
        if taxa < 0 or periodos < 0:
            print("Erro: Taxa e períodos devem ser valores positivos")
            return 0
            
        juros = self.saldo * taxa * periodos
        self.saldo += juros
        return juros

    def __str__(self):
        return (f"Conta Bancária:\n"
                f"  Número: {self.numero}\n"
                f"  Titular: {self.titular}\n"
                f"  Saldo: R${self.saldo:.2f}")

    # ... (outros métodos permanecem iguais)
```

**Demonstração de uso:**

```python
# Criando uma conta
conta_poupanca = Conta(1001, "Carlos Santos", 1000.00)

# Aplicando juros de 2% ao mês por 12 meses
juros = conta_poupanca.aplicar_juros_simples(0.02, 12)

print(f"Juros calculados: R${juros:.2f}")
print(conta_poupanca)
```

**Funcionamento detalhado:**

1. **Fórmula dos juros simples**:
   - `J = P × i × n`
   - Onde:
     - `J` = juros
     - `P` = saldo principal
     - `i` = taxa de juros por período
     - `n` = número de períodos

2. **Validações**:
   - Verifica se taxa e períodos são positivos
   - Retorna 0 e exibe mensagem de erro se valores forem inválidos

3. **Atualização automática**:
   - O saldo da conta é atualizado automaticamente
   - O método retorna o valor dos juros calculados para possível registro

**Exemplo integrado com o menu:**

```python
# Adicione esta opção no menu principal
elif opcao == "7":  # Opção para aplicar juros
    print("\n--- APLICAÇÃO DE JUROS ---")
    try:
        numero = int(input("Número da conta: "))
        taxa = float(input("Taxa de juros (ex: 0.05 para 5%): "))
        periodos = int(input("Número de períodos: "))
        
        if numero in banco.contas:
            conta = banco.contas[numero]
            juros = conta.aplicar_juros_simples(taxa, periodos)
            print(f"Juros de R${juros:.2f} aplicados na conta {numero}")
            print(f"Novo saldo: R${conta.saldo:.2f}")
        else:
            print("Conta não encontrada!")
    except ValueError:
        print("Erro: Valores inválidos inseridos!")
```

### 16. **Simulação de Cenário:**  
**Atividade**:
-  Monte um cenário onde o banco possui pelo menos 5 contas, execute uma série de operações (depósitos, saques, transferências) e, ao final, gere um relatório geral do banco com as informações de todas as contas.

```python
# Criação do banco e cadastro de contas
banco = Banco()

# Cadastrando 5 contas iniciais
contas_iniciais = [
    (1001, "Ana Silva", 5000.00),
    (1002, "Carlos Oliveira", 3200.50),
    (1003, "Mariana Santos", 1500.00),
    (1004, "João Pereira", 800.00),
    (1005, "Fernanda Costa", 12500.75)
]

for numero, titular, saldo in contas_iniciais:
    banco.adicionar_conta(Conta(numero, titular, saldo))

print("=== CONTAS CADASTRADAS COM SUCESSO ===")

# Realizando operações bancárias
print("\n=== REALIZANDO OPERAÇÕES ===")

# Depósitos
banco.depositar(1001, 300.00)   # Ana Silva
banco.depositar(1003, 500.50)    # Mariana Santos
banco.depositar(1005, 1000.25)   # Fernanda Costa

# Saques
banco.sacar(1002, 200.00)        # Carlos Oliveira
banco.sacar(1004, 150.00)        # João Pereira
banco.sacar(1005, 2000.00)       # Fernanda Costa

# Transferências
banco.transferir(1001, 1003, 400.00)  # Ana → Mariana
banco.transferir(1005, 1002, 800.00)   # Fernanda → Carlos
banco.transferir(1003, 1004, 100.00)   # Mariana → João

# Aplicando juros em algumas contas
print("\n=== APLICANDO JUROS ===")
conta1001 = banco.contas[1001]
conta1005 = banco.contas[1005]

juros_ana = conta1001.aplicar_juros_simples(0.02, 6)  # 2% por 6 meses
juros_fernanda = conta1005.aplicar_juros_simples(0.015, 12)  # 1.5% por 12 meses

print(f"Juros aplicados na conta 1001: R${juros_ana:.2f}")
print(f"Juros aplicados na conta 1005: R${juros_fernanda:.2f}")

# Relatório final
print("\n=== RELATÓRIO GERAL DO BANCO ===")
print(f"Total de contas: {len(banco.contas)}")
print("\nDetalhes das contas:")

# Obtendo relatório ordenado por saldo
relatorio = banco.gerar_relatorio_saldos()

# Cabeçalho do relatório
print("\n{:<15} {:<20} {:<15}".format("Número", "Titular", "Saldo"))
print("-" * 50)

# Imprimindo cada conta
for conta in relatorio:
    print("{:<15} {:<20} R${:<10.2f}".format(
        conta['numero'],
        conta['titular'],
        conta['saldo']))

# Saldos consolidados
total_saldos = sum(conta['saldo'] for conta in relatorio)
print("\nTotal em depósitos no banco: R${:.2f}".format(total_saldos))
```

**Análise do cenário:**

1. **Operações realizadas**:
   - 3 depósitos em contas diferentes
   - 3 saques com valores variados
   - 3 transferências entre contas
   - Aplicação de juros em 2 contas

2. **Resultados finais**:
   - Todas as contas com saldos atualizados
   - Relatório ordenado por saldo decrescente
   - Consolidação do total de depósitos no banco

3. **Verificações importantes**:
   - Transferências mantiveram o saldo total do banco
   - Juros foram calculados corretamente
   - Saldos finais refletem todas as operações

