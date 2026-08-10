
# **Tarefa 02: Criando um repositório local 🚀🐙**  

## 🎯 **Objetivo**: 
Aprender e praticar as principais funcionalidades do **Git**, focando no trabalho com Branches .  

## 📌 **Pré-requisitos**:  

✅ **Git instalado**: Se ainda não instalou, baixe  [aqui](https://git-scm.com/).

✅ **Conta no GitHub**  (ou GitLab/Bitbucket, se preferir).

✅ Conhecimento básico de uso de  **terminal**  (Prompt de Comando, PowerShell ou Terminal Linux/Mac).


## **🔹 Passo 1: Criando e Trabalhando com Branches**
Branches são como "realidades alternativas" do seu código, permitindo que você experimente novas ideias sem comprometer a versão principal.

> ☢️ **Atenção:** Os comandos utilizados nesta atividade devem ser executados no mesmo diretório do repositório utilizado na tarefa anterior.

1️⃣ Criar uma nova branch

```bash
git branch nova_funcionalidade
```

2️⃣ Trocar para essa branch

```bash
git checkout nova_funcionalidade
```

🔥 Agora estamos trabalhando em um ambiente isolado!

```bash
Switched to branch 'nova_funcionalidade'
```
Ainda podemos verificar o status do branch

```bash
git status
```
Neste momento não temos commits pendentes:

```bash
On branch nova_funcionalidade
nothing to commit, working tree clean
```


3️⃣ Realizando e registrando uma alteração no repositório

```bash
echo "Nova funcionalidade adicionada em 15/02/2025" >> NovaFuncionalidade.txt  
git add NovaFuncionalidade.txt  
git commit -m "Adiciona nova funcionalidade"
```
Pronto,  agora já  temos nosso primeiro commit no branch atual 

```bash 
[nova_funcionalidade 6e4d5bf] Adiciona nova funcionalidade
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 NovaFuncionalidade.txt
```

Confirmando que as modificações foram publicadas

```bash 
git log
```
Verificamos que há dois branchs ativos.

```bash 
commit 6e4d5bf430d7efcb3987a23fcb7a8f3d6158f822 (HEAD -> nova_funcionalidade)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 12:35:12 2025 -0300

    Adiciona nova funcionalidade

commit e93737d0ab51943afee00598cf7571e2034bff84 (master)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 11:58:06 2025 -0300

    Primeiro commit: adicionei o arquivo README.txt
```


4️⃣ Voltar para a branch principal

```bash
git checkout master
```

Estamos de volta no branch principal, que no nosso caso é o **master**

```bash
Switched to branch 'master'
```
Confirmando a mudança

```bash
git status
git log
```
As linhas abaixo representam o estado do nosso repositório:

```bash 
commit 6e4d5bf430d7efcb3987a23fcb7a8f3d6158f822 (HEAD -> master, nova_funcionalidade)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 12:35:12 2025 -0300

    Adiciona nova funcionalidade

commit e93737d0ab51943afee00598cf7571e2034bff84
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 11:58:06 2025 -0300

    Primeiro commit: adicionei o arquivo README.txt
```


5️⃣ Juntar as mudanças da branch nova para a principal

```bash
git merge nova_funcionalidade
```

Desta forma atualizamos o branch **atual** com as informações do branch  **nova_funcionalidade**

```bash
Updating e93737d..6e4d5bf
Fast-forward
 NovaFuncionalidade.txt | Bin 0 -> 94 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 NovaFuncionalidade.txt
```



6️⃣ Excluir a branch que não precisamos mais

```bash
git branch -d nova_funcionalidade
```
Com isto removemos a branch

```bash 
Deleted branch nova_funcionalidade (was 6e4d5bf)
```
Confirmando o log do nosso repositório

```bash 
git log
```
Percebemos que branch, realmente, sumiu... 🙈

```bash 
commit 6e4d5bf430d7efcb3987a23fcb7a8f3d6158f822 (HEAD -> master)
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 12:35:12 2025 -0300

    Adiciona nova funcionalidade

commit e93737d0ab51943afee00598cf7571e2034bff84
Author: Papagaio - Luis Rodrigo de O Gonçalves <luis.rodrigo.net@gmail.com>
Date:   Wed Feb 12 11:58:06 2025 -0300

    Primeiro commit: adicionei o arquivo README.txt
```


 🧩 Com isto finalizamos a nossa primeira atividade 🏆 

