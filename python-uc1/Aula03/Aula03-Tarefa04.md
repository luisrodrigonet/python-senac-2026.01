
# **Tarefa 04: Publicando no GitHub 🚀🐙**  

## 🎯 **Objetivo**: 
Aprender e praticar as principais funcionalidades do **Git**, focando no trabalho em conjunto com o  GitHub  .  

## 📌 **Pré-requisitos**:  

✅ **Git instalado**: Se ainda não instalou, baixe  [aqui](https://git-scm.com/).

✅ **Conta no GitHub**  (ou GitLab/Bitbucket, se preferir).

✅ Conhecimento básico de uso de  **terminal**  (Prompt de Comando, PowerShell ou Terminal Linux/Mac).

## **🔹 Passo 1: Criar um Repositório no GitHub**

Antes de sincronizar, precisamos de um repositório no GitHub:

1️⃣ Acesse [GitHub](https://github.com/) e faça login.  
2️⃣ Clique no botão **"New Repository"** (Novo Repositório).  
3️⃣ Dê um nome ao repositório e clique em **"Create Repository"**.  
4️⃣ **Copie a URL do repositório** que será exibida (algo como `https://github.com/seu-usuario/nome-do-repo.git`).

## **🔹 Passo 2: Configurar o Repositório Local**

Agora, vamos conectar seu repositório local ao GitHub.

1️⃣ **Abra o terminal** (Prompt de Comando, PowerShell ou Terminal Linux/Mac).  

2️⃣ **Acesse a pasta do seu repositório local**:

```bash 
cd caminho/do/seu/repo
```

3️⃣ **Verifique se o Git está inicializado** (caso ainda não tenha feito isso):

```bash
git init
```
Com isto o repositório é iniciado

```bash 
Initialized empty Git repository in 
D://Python-UC1-Aulas/Python-UC01-Teste/.git/
```

## **🔹 Passo 3: Conectar ao Repositório Remoto**

Agora, precisamos dizer ao Git que queremos conectar nosso repositório local ao GitHub.

1️⃣ **Adicionar o repositório remoto**:


```bash
git remote add origin https://github.com/seu-usuario/nome-do-repo.git`
```

🔹 Substitua `seu-usuario` pelo seu nome no GitHub e `nome-do-repo` pelo nome do repositório criado.

Por exemplo

```bash
git remote add origin https://github.com/luisrodrigonet/Python-UC01-Teste.git
```

2️⃣ **Verifique se a conexão foi feita corretamente**:

```bash
git remote -v
```

Se estiver tudo certo, ele mostrará algo como:

```bash 
origin  https://github.com/seu-usuario/nome-do-repo.git (fetch)
origin  https://github.com/seu-usuario/nome-do-repo.git (push)
```

## **🔹 Passo 4: Enviar os Arquivos para o GitHub**

1️⃣ **Adicionar os arquivos ao Git (caso ainda não tenha feito)**

Primeiro vamos criar um arquivo de teste

```bash
echo "teste" > teste.txt
```

Em seguida podemos adicionar os arquivos

```bash
git add .
```

Isso adiciona todos os arquivos à área de staging.


2️⃣ **Criar um commit com uma mensagem explicativa**

```bash
git commit -m "Primeiro commit - Enviando arquivos para o GitHub"
```
Confirmando o commit

```bash 
[master (root-commit) 80f6373] Primeiro commit - Enviando arquivos para o GitHub
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 teste.txt
```
Em seguida devemos renomear o branch para main, mantendo a compatibilidade com o GitHub

```bash 
git branch -M main 
git log
```

Podemos verificar que o nome do brach mudou de master para main

```bash 
commit 80f63736c61d37a7df396546ead6874d61c4e8c9 (HEAD -> main)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 16:50:56 2025 -0300

    Primeiro commit - Enviando arquivos para o GitHub
```

3️⃣ **Enviar os arquivos para o GitHub (primeiro push)**

🔹 Se for a primeira vez que você está usando GitHub no terminal, pode ser necessário autenticar com seu **token de acesso pessoal** (caso tenha ativado autenticação via HTTPS).

```bash 
git push -u origin main
```
Confirmando que conseguimos sincronizar a pasta local com o repositório remoto

```bash 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 281 bytes | 281.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/luisrodrigonet/Python-UC01-Teste.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```
Caso a branch principal do seu repositório no GitHub seja chamada de master, use 

```bash
git push -u origin master.
```

## **🔹Passo 5: Manter o Repositório Sincronizado**

Agora que o repositório local está conectado ao GitHub, sempre que quiser atualizar seu código, siga este fluxo:

🔄 Baixar mudanças do GitHub (caso alguém tenha alterado o código)

```bash 
git pull origin main
```

Por entanto não há atualizações a serem baixadas

```bash 
From https://github.com/luisrodrigonet/Python-UC01-Teste
 * branch            main       -> FETCH_HEAD
Already up to date.
```

📤 Enviar novas alterações para o GitHub

```bash 
git add .  
git commit -m "Descrição das mudanças"  
git push origin main
```
Assim como não há atualizações a serem enviadas

```bash 
Everything up-to-date
```
 🧩 Com isto finalizamos a nossa primeira atividade 🏆 
