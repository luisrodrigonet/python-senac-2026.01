

# **Tarefa 05: Clonado um repositório do GitHub 🚀🐙**  

## 🎯 **Objetivo**: 
Aprender e praticar as principais funcionalidades do **Git**, focando no trabalho em conjunto com o  GitHub  .  

## 📌 **Pré-requisitos**:  

✅ **Git instalado**: Se ainda não instalou, baixe  [aqui](https://git-scm.com/).

✅ **Conta no GitHub**  (ou GitLab/Bitbucket, se preferir).

✅ Conhecimento básico de uso de  **terminal**  (Prompt de Comando, PowerShell ou Terminal Linux/Mac).

## **🔹 Passo 1: Criar um Repositório no GitHub**

Antes de sincronizar, precisamos de um repositório no GitHub:

1️⃣ Acesse [GitHub](https://github.com/) e faça login.  
2️⃣ **Copie a URL do repositório** que será exibida (algo como `https://github.com/seu-usuario/nome-do-repo.git`).

## **🔹 Passo 2:  Acessando a pasta local**

Agora, vamos conectar seu repositório local ao GitHub.

1️⃣ **Abra o terminal** (Prompt de Comando, PowerShell ou Terminal Linux/Mac).  

2️⃣ **Acesse a pasta do seu repositório local**:

```bash 
cd caminho/do/seu/repo
```

## **🔹 Passo 3: Clonando um Repositório do GitHub**

Se você quiser baixar um repositório que já existe no GitHub e trabalhar nele localmente, use:

```bash 
git clone https://github.com/seu-usuario/nome-do-repo.git
```
No nosso caso, utilizaremos o seguinte comando:

```bash 
git clone https://github.com/luisrodrigonet/Python-UC01-Clone.git
```
Isso cria uma cópia completa do repositório no seu computador! 🚀

```bash 
Cloning into 'Python-UC01-Clone'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
```

## **🔹 Passo 5: Manter o Repositório Sincronizado**

Agora que o repositório local está conectado ao GitHub, sempre que quiser atualizar seu código, siga este fluxo:

🔄 Baixar mudanças do GitHub (caso alguém tenha alterado o código)

```bash 
git pull origin main
```

📤 Enviar novas alterações para o GitHub

```
git add .  
git commit -m "Descrição das mudanças"  
git push origin main
```
 🧩 Com isto finalizamos a nossa primeira atividade 🏆 
