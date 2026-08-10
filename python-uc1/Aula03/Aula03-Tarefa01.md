
# **Tarefa 01: Criando um repositório local 🚀🐙**  

## 🎯 **Objetivo**: 
Aprender e praticar as principais funcionalidades do **Git**, focando na criação de um repositório local.  

## 📌 **Pré-requisitos**:  

✅ **Git instalado**: Se ainda não instalou, baixe  [aqui](https://git-scm.com/).

✅ **Conta no GitHub**  (ou GitLab/Bitbucket, se preferir).

✅ Conhecimento básico de uso de  **terminal**  (Prompt de Comando, PowerShell ou Terminal Linux/Mac).

## **🔹 Passo 1: Configurar o Git**
Antes de mais nada, vamos garantir que o Git reconheça sua identidade! No terminal, digite o seguinte comando:

```bash
git config --global user.name "Papagaio - Luis Rodrigo de O Gonçalves"
git config --global user.email "luis.rodrigo.net@gmail.com"
```

Agora, verifique se deu certo:  

```bash
git config --list
```
Ao executar o comando, devemos receber uma saída semelhante as linhas abaixo:

```bash
user.name=Papagaio - Luis Rodrigo de O Gonçalves
user.email=luis.rodrigo.net@gmail.com
```


## **🔹 Passo 2: Criando um Repositório Git**

Vamos criar nosso primeiro repositório!

1️⃣ **Crie uma pasta para o projeto**

```bash
mkdir projeto_python_uc1
cd projeto_python_uc1
```

2️⃣ **Inicie o Git dentro da pasta**

```bash
git init
```

Ao executar o comando, devemos receber uma saída semelhante as linhas abaixo:

```bash
Initialized empty Git repository in 
D:/LRodrigo-Prog-GitHub/Python-UC1-Aulas/projeto_python_uc1/.git/
```

Pronto! Agora essa pasta é um repositório Git! 🎉

3️⃣ **Crie um arquivo de teste**

```bash
echo "Olá, Git!" > README.txt
```

4️⃣ **Verifique o status do repositório**

```bash
git status
```

➡️ O Git vai mostrar que há um arquivo não rastreado.

```bash
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.txt

nothing added to commit but untracked files present (use "git add" to track)
```

5️⃣ Adicionando o arquivo realizando seu Commit 🤓

Primeiro precisamos adicionar o arquivo ao *staging area* (área de preparação):
```bash
git add README.txt
```
Em seguida podemos realizar o commit (salve a versão):

```bash  
git commit -m "Primeiro commit: adicionei o arquivo README.txt"
```
Devemos receber a seguinte saída:

```bash
[master (root-commit) e93737d] Primeiro commit: adicionei o arquivo README.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt
```

Finalmente podemos verificar o histórico de commits:

```bash
git log
```
Devemos receber a seguinte saída:

```
commit e93737d0ab51943afee00598cf7571e2034bff84 (HEAD -> master)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 11:58:06 2025 -0300

    Primeiro commit: adicionei o arquivo README.txt
```

 🧩 Com isto finalizamos a nossa primeira atividade 🏆 

