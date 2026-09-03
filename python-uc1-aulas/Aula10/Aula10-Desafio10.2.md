# Aula 10 - Desafio 10.2

> Agora vamos a um segundo desafio.

## :snake: Desafio 1: Jogo de Batalha Naval

### :bell: Objetivo:

Criar uma versão simplificada do jogo Batalha Naval para ser jogada no terminal. O jogo deve permitir que o jogador tente acertar a posição de um ou mais navios escondidos em um tabuleiro.

### :loudspeaker: Requisitos:

1. Tabuleiro:
    - Crie um tabuleiro representado por uma matriz (lista de listas) de tamanho 5x5 (ou outro tamanho de sua escolha).
    - Cada posição do tabuleiro deve ser inicialmente marcada com um símbolo (por exemplo, '-').

2. Posicionamento dos Navios:
	- Posicione um ou mais navios no tabuleiro de forma aleatória.
	- Cada navio pode ocupar uma única célula ou, se desejar, mais de uma (por exemplo, navios de tamanho 2 ou 3).
	- Utilize funções da biblioteca random para posicionar os navios sem sobreposição.

3. Interação com o Jogador:
	- Solicite ao jogador que informe coordenadas (linha e coluna) para atacar.
	- Verifique se o ataque acertou um navio ou errou.
	- Exiba mensagens apropriadas ("Acertou!", "Errou!").
	- Atualize o tabuleiro com marcas, como por exemplo: 
		1. X para acertos,
		1.  O para erros.

4. Condição de Vitória:
	-  O jogo termina quando o jogador conseguir acertar todas as posições dos navios.

5. Exibição do Tabuleiro:
	- Após cada jogada, exiba o tabuleiro atualizado para que o jogador possa visualizar seus acertos e erros.
	
### :pushpin: Dicas:

1. Utilize loops para permitir várias jogadas até o término do jogo.
2.  Crie funções para separar as funcionalidades, por exemplo: criar_tabuleiro(), posicionar_navios(), verificar_ataque(), etc.
3. Considere validar as entradas do usuário para evitar coordenadas inválidas.


## :snake: Desafio 2: Quadrado Mágico 3x3

### :bell: Objetivo:

Desenvolver um programa que permita ao usuário montar ou verificar um quadrado mágico 3x3. Um quadrado mágico é uma matriz 3x3 onde a soma dos números de cada linha, cada coluna e das diagonais é sempre a mesma.

### :loudspeaker: Requisitos:

1. Definição do Quadrado Mágico:
	-  Considere os números de 1 a 9. Em um quadrado mágico 3x3 clássico, cada número deve aparecer exatamente uma vez.
	- A soma mágica, no caso, é 15 (pois 1+2+…+9 = 45 e 45/3 = 15).
	
2. Opção 1 – Construção Interativa:
	-  Permita que o usuário insira os números para cada posição da matriz (três linhas com três números cada).
	-  Após a entrada, verifique se o quadrado formado é mágico (ou seja, se todas as linhas, colunas e as duas diagonais somam 15).
	-  Exiba uma mensagem informando se o quadrado é ou não mágico.
	
3. Opção 2 – Desafio de Rearranjo:
	-  Gere uma matriz 3x3 com os números de 1 a 9 em ordem aleatória.
	-  Exiba o quadrado e peça ao usuário para tentar rearranjar os números (através de trocas ou reposicionamento) até formar um quadrado mágico.
	-  A cada tentativa, o programa verifica se a soma das linhas, colunas e diagonais é 15 e informa o progresso.
	-  O jogo termina quando o quadrado se torna mágico.
	
4. Exibição e Validação:
	-  Mostre o quadrado em formato tabular para facilitar a visualização.
	-  Certifique-se de validar as entradas do usuário para que não haja números repetidos ou números fora do intervalo permitido (1 a 9).

### :pushpin: Dicas:

- Crie funções para separar tarefas, como verificar_quadrado_magico(matriz), imprimir_quadrado(matriz) e funções para manipulação de entradas.
-  Para a verificação, utilize loops ou compreensões de listas para calcular a soma de cada linha, coluna e diagonal.

No desafio interativo, permita que o usuário faça múltiplas tentativas e forneça dicas (por exemplo, informe quais linhas ou colunas não atingiram a soma correta)

