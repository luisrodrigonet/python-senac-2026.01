# Aula 11 - Tarefa 1 - Dicionários

## Exercícios Simples

### :one: **Criação Básica:**  

Crie um dicionário representando uma conta bancária com as chaves `"titular"`, `"numero"` e `"saldo"` e imprima o seu conteúdo.  

:snake: Código:   
```python
# Criando o dicionário da conta bancária
conta_bancaria = {
    "titular": "João da Silva",
    "numero": "12345-6",
    "saldo": 2500.00
}

# Imprimindo o conteúdo do dicionário
print("Dados da conta bancária:")
print(f"Titular: {conta_bancaria['titular']}")
print(f"Número da conta: {conta_bancaria['numero']}")
print(f"Saldo: R$ {conta_bancaria['saldo']:.2f}")
```

### :two: **Obtendo dados**

Elabore um programa que simule múltiplas contas bancárias utilizando dicionários, onde cada conta será armazenada em uma posição de um vetor. Cada conta bancária deve conter as seguintes chaves: "titular", "numero" e "saldo". O programa deve solicitar ao usuário os dados de quatro contas bancárias e, ao final, exibir as informações cadastradas.

:snake: Código: 

```python
# Programa para cadastrar e exibir contas bancárias

def cadastrar_contas():
    contas = []  # Lista para armazenar as contas
    
    print("Cadastro de Contas Bancárias")
    print("---------------------------")
    
    for i in range(4):  # Cadastrar 4 contas
        print(f"\nConta {i+1}:")
        titular = input("Nome do titular: ")
        numero = input("Número da conta: ")
        saldo = float(input("Saldo inicial: R$ "))
        
        # Cria o dicionário da conta e adiciona à lista
        conta = {
            "titular": titular,
            "numero": numero,
            "saldo": saldo
        }
        contas.append(conta)
    
    return contas

def exibir_contas(contas):
    print("\nContas cadastradas:")
    print("==================")
    
    for i, conta in enumerate(contas, 1):
        print(f"\nConta {i}:")
        print(f"Titular: {conta['titular']}")
        print(f"Número: {conta['numero']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")

# Programa principal
contas_bancarias = cadastrar_contas()
exibir_contas(contas_bancarias)
```

#### Funcionamento do programa:

1. **Cadastro das contas**:
   - Solicita os dados de 4 contas bancárias (titular, número e saldo)
   - Armazena cada conta como um dicionário dentro de uma lista

2. **Exibição das contas**:
   - Mostra todas as contas cadastradas de forma organizada
   - Formata o saldo com 2 casas decimais

3. **Estrutura dos dados**:
   - Cada conta é um dicionário com as chaves: `titular`, `numero` e `saldo`
   - Todas as contas são armazenadas em uma lista (vetor)


### :three: Salvando os dados

Elabore um programa que simule múltiplas contas bancárias utilizando **dicionários**, onde cada conta será armazenada em uma posição de um **vetor**. Cada conta bancária deve conter as seguintes chaves: `"titular"`, `"numero"` e `"saldo"`.  

O programa deve permitir as seguintes operações:  
- Solicitar ao usuário os dados de uma nova conta.  
- Adicionar os dados inseridos a um arquivo **CSV**.  
- Ler o conteúdo de um arquivo **CSV** e armazená-lo em uma estrutura de dados.  
- Consultar e exibir os dados lidos de um arquivo **CSV**.  


```python
import csv
import os

def adicionar_conta(contas):
    """Solicita os dados de uma nova conta e adiciona ao vetor"""
    print("\nCadastro de nova conta:")
    titular = input("Nome do titular: ")
    numero = input("Número da conta: ")
    saldo = float(input("Saldo inicial: R$ "))
    
    conta = {
        "titular": titular,
        "numero": numero,
        "saldo": saldo
    }
    contas.append(conta)
    print("Conta adicionada com sucesso!")
    return contas

def salvar_para_csv(contas, arquivo='contas.csv'):
    """Salva todas as contas em um arquivo CSV"""
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["titular", "numero", "saldo"])
        writer.writeheader()
        writer.writerows(contas)
    print(f"\nDados salvos no arquivo {arquivo}")

def ler_de_csv(arquivo='contas.csv'):
    """Lê as contas de um arquivo CSV e retorna como lista de dicionários"""
    contas = []
    if os.path.exists(arquivo):
        with open(arquivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Converte saldo para float
                row['saldo'] = float(row['saldo'])
                contas.append(row)
        print(f"\nDados carregados do arquivo {arquivo}")
    else:
        print("\nArquivo não encontrado. Iniciando com lista vazia.")
    return contas

def exibir_contas(contas):
    """Exibe todas as contas cadastradas"""
    print("\nLista de contas bancárias:")
    print("-" * 40)
    for i, conta in enumerate(contas, 1):
        print(f"Conta {i}:")
        print(f"  Titular: {conta['titular']}")
        print(f"  Número: {conta['numero']}")
        print(f"  Saldo: R$ {conta['saldo']:.2f}")
        print("-" * 40)

def menu():
    """Exibe o menu de opções"""
    print("\nSistema Bancário")
    print("1. Adicionar nova conta")
    print("2. Salvar contas em arquivo CSV")
    print("3. Carregar contas de arquivo CSV")
    print("4. Exibir contas cadastradas")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            contas = adicionar_conta(contas)
        elif opcao == '2':
            salvar_para_csv(contas)
        elif opcao == '3':
            contas = ler_de_csv()
        elif opcao == '4':
            exibir_contas(contas)
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
```

#### Funcionamento do programa:

1. **Estrutura de dados**:
   - Cada conta é um dicionário com as chaves `titular`, `numero` e `saldo`
   - Todas as contas são armazenadas em uma lista (vetor)

2. **Operações disponíveis**:
   - **Adicionar nova conta**: Solicita os dados ao usuário e adiciona à lista
   - **Salvar em CSV**: Grava todas as contas em um arquivo `contas.csv`
   - **Ler de CSV**: Carrega as contas do arquivo `contas.csv`
   - **Exibir contas**: Mostra todas as contas cadastradas formatadas

3. **Persistência dos dados**:
   - Usa o módulo `csv` para leitura/gravação
   - O arquivo CSV tem cabeçalhos: titular, numero, saldo
   - Verifica se o arquivo existe antes de tentar ler

4. **Interface do usuário**:
   - Menu interativo com 5 opções
   - Validação básica de entrada

#### Como usar:

1. Execute o programa
2. Use o menu para:
   - Cadastrar novas contas (opção 1)
   - Salvar em arquivo (opção 2)
   - Carregar de arquivo (opção 3)
   - Visualizar contas (opção 4)
3. Os dados são mantidos mesmo após fechar o programa

#### Exemplo de arquivo CSV gerado:
```
titular,numero,saldo
João Silva,12345-6,1500.0
Maria Oliveira,54321-0,2800.5
```


