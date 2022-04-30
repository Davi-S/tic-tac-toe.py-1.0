tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tabuleiroexterno = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogador = 1
simbolo1 = 'X'
simbolo2 = 'O'
round = rodadas = 0
j1v = 0
j2v = 0
emp = 0

# estilo
enulo = ';0'
enegrito = ';1'
eitalico = ';3'
esublinhado = ';4'
enegativo = ';7'

# texto
tbranco = ';30'
tvermelho = ';31'
tverde = ';32'
tamarelo = ';33'
tazul = ';34'
tmagenta = ';35'
tciano = ';36'
tcinza = ';37'

# fundo
fbranco = ';40'
fvermelho = ';41'
fverde = ';42'
famarelo = ';43'
fazul = ';44'
fmagenta = ';45'
fciano = ';46'
fcinza = ';47'


def textocor(txt, estilo='', texto='', fundo=''):
    return print(f'\033[{estilo}{texto}{fundo}m{txt}\033[m')


from math import ceil
from random import randint
from cores import *
from time import sleep


# matriz que o programa ira usar
def mesainterna():
    global tabuleiro
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tabuleiro[l][c]:^5}]', end='')
        print()  # #


# matriz que será mostrada para o jogador
def mesaexterna():
    global tabuleiroexterno
    print('\033[1;34m|=====||=====||=====|\033[m')
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'\033[1;34m|{tabuleiroexterno[l][c]:^5}|\033[m', end='')
        print()
        print('\033[1;34m|=====||=====||=====|\033[m')


# troca o jogador que irá jogar
def trocadejogador():
    global jogador
    if jogador == 1:
        jogador = -1
    elif jogador == -1:
        jogador = 1


# aceita apenas a entrada de números 'int'
def leiainteiro(a):
    while True:
        try:
            n = int(input(a))
        except ValueError:
            print('\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO\033[m')
            continue
        else:
            break
    return n


# permite que o jogador faça sua jogada
def jogada():
    global tabuleiro, tabuleiroexterno, simbolo1, simbolo2
    while True:
        pos = leiainteiro('\033[33mOnde deseja jogar? >\033[m')
        # apenas inverte o a matriz para que fique semelhante ao teclado númerico convencional facilitando a jogabilidade
        if pos == 7:
            pos = 1
        elif pos == 8:
            pos = 2
        elif pos == 9:
            pos = 3
        elif pos == 1:
            pos = 7
        elif pos == 2:
            pos = 8
        elif pos == 3:
            pos = 9
        elif pos > 9 or pos < 1:
            textocor('ERRO! Por favor digite apenas números de 1 a 9', enegrito, tvermelho)
            continue
        # esse pedaço faz com que a posição indicada pelo jogador seja encontrada e mudada na matriz(fique a vontade para entende-la)
        dpos = pos / 3
        lpos = ceil(dpos) - 1
        if lpos % 2 == 0:
            vlpos = 0
        else:
            vlpos = 1
        if pos % 2 == 0:
            vpos = 0
        else:
            vpos = 1
        if vpos == vlpos:
            cpos = 1
        else:
            if pos % 3 == 0 or pos % 6 == 0 or pos % 9 == 0:
                cpos = 2
            else:
                cpos = 0
        # faz a mudança das matrizes de acordo com a jogada do player
        if tabuleiro[lpos][cpos] != 0:
            textocor('Essa posição ja está ocupada...'
                     'Tente outra posição...', tmagenta, eitalico)
            continue
        else:
            tabuleiro[lpos][cpos] += 1
            tabuleiroexterno[lpos][cpos] = simbolo1
        break


# mostra de quem é a vez de jogar
def mostrajogador():
    global jogador
    if jogador == 1:
        textocor('SUA VEZ!', tamarelo)
    else:
        textocor('MINHA VEZ!', tamarelo)


# mostra quando alguem ganha a partida
def vervencedor():
    # o jogador 1 recebe o numero -1 e o jogador 2 recebe o número 1. isso significa que é possivel detectar o
    # vencedor quando a soma de alguma linha ou diagonal for igua a 3 ou -3 (o jogador conseguiu uma sequemcia de
    # caracteres
    for l in range(0, 3):
        soma1 = soma2 = 0
        for c in range(0, 3):
            soma1 += tabuleiro[l][c]
            soma2 += tabuleiro[c][l]
        d1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
        d2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
        if soma1 == 3 or soma2 == 3 or d1 == 3 or d2 == 3:
            return 'j1'
        elif soma1 == -3 or soma2 == -3 or d1 == -3 or d2 == -3:
            return 'j2'


# oque o pc irá jogar quando for sua vez na dificuldade facil
def pc():
    global tabuleiro, jogador, tabuleiroexterno
    textocor('Deixe-me pensar na minha jogada...', tamarelo)
    while True:
        sleep(1.5)
        # o pc escolhe sua jogada aleatoriamente
        pos = randint(1, 9)
        # mesmo enquema para achar a posição da jogada na matriz
        dpos = pos / 3
        lpos = ceil(dpos) - 1
        if lpos % 2 == 0:
            vlpos = 0
        else:
            vlpos = 1
        if pos % 2 == 0:
            vpos = 0
        else:
            vpos = 1
        if vpos == vlpos:
            cpos = 1
        else:
            if pos % 3 == 0 or pos % 6 == 0 or pos % 9 == 0:
                cpos = 2
            else:
                cpos = 0
        if tabuleiro[lpos][cpos] != 0:
            continue
        else:
            tabuleiro[lpos][cpos] += -1
            tabuleiroexterno[lpos][cpos] = simbolo2
        break


# oque o pc irá jogar quando for sua vez na dificuldade dificil
# essa parte e a parte seguinte ainda presisa de muitas mudanças pois tudo esta "escrito a mão" até agora
# felizmente essa função está funcionando como esperado
def pcdificil():
    global tabuleiro, jogador, tabuleiroexterno
    textocor('Deixe-me pensar na minha jogada...', tamarelo)
    sleep(0.5)
    if tabuleiro[0][2] == 1 and tabuleiro[0][1] == 1 or tabuleiro[2][2] == 1 and tabuleiro[1][1] == 1 or tabuleiro[1][
        0] == 1 and tabuleiro[2][0] == 1:
        pos = 1
    elif tabuleiro[0][0] == 1 and tabuleiro[0][2] == 1 or tabuleiro[1][1] == 1 and tabuleiro[2][1] == 1:
        pos = 2
    elif tabuleiro[0][0] == 1 and tabuleiro[0][1] == 1 or tabuleiro[2][0] == 1 and tabuleiro[1][1] == 1 or tabuleiro[2][
        2] == 1 and tabuleiro[1][2] == 1:
        pos = 3
    elif tabuleiro[0][0] == 1 and tabuleiro[2][0] == 1 or tabuleiro[1][1] == 1 and tabuleiro[1][2] == 1:
        pos = 4
    elif tabuleiro[0][0] == 1 and tabuleiro[2][2] == 1 or tabuleiro[0][2] == 1 and tabuleiro[2][0] == 1 or tabuleiro[0][
        1] == 1 and tabuleiro[2][1] == 1 or tabuleiro[1][0] and tabuleiro[1][2]:
        pos = 5
    elif tabuleiro[1][0] == 1 and tabuleiro[1][1] == 1 or tabuleiro[0][2] == 1 and tabuleiro[2][2] == 1:
        pos = 6
    elif tabuleiro[0][0] == 1 and tabuleiro[1][0] == 1 or tabuleiro[0][2] == 1 and tabuleiro[1][1] == 1 or tabuleiro[2][
        1] == 1 and tabuleiro[2][2] == 1:
        pos = 7
    elif tabuleiro[0][1] == 1 and tabuleiro[1][1] == 1 or tabuleiro[2][0] == 1 and tabuleiro[2][2] == 1:
        pos = 8
    elif tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1 or tabuleiro[0][2] == 1 and tabuleiro[1][2] == 1 or tabuleiro[2][
        0] == 1 and tabuleiro[2][1] == 1:
        pos = 9
    elif round <= 1:
        pos = 5
    else:
        pos = randint(1, 9)
    while True:
        dpos = pos / 3
        lpos = ceil(dpos) - 1
        if lpos % 2 == 0:
            vlpos = 0
        else:
            vlpos = 1
        if pos % 2 == 0:
            vpos = 0
        else:
            vpos = 1
        if vpos == vlpos:
            cpos = 1
        else:
            if pos % 3 == 0 or pos % 6 == 0 or pos % 9 == 0:
                cpos = 2
            else:
                cpos = 0
        if tabuleiro[lpos][cpos] != 0:
            pos = randint(1, 9)
            continue
        else:
            tabuleiro[lpos][cpos] += -1
            tabuleiroexterno[lpos][cpos] = simbolo2
            break


# oque o pc irá jogar quando for sua vez na dificuldade quase impossivel
# essa função esta funcionando em parte; ela é capaz de atacar e defender mas não funciona 100% das vezes como esperado
# ja que quando o jogador começa jogando no meio e os dois escolhem as melhores jogadas é certesa que o jogo irá empatar
# mas não é isso que acontece aqui
# (segue a explicação da funçao)
def pcquaseimpossivel():
    global tabuleiro, jogador, tabuleiroexterno
    textocor('Deixe-me pensar na minha jogada...', tamarelo)
    sleep(0.5)
    # aqui é definido quando o pc irá 'atacar' (ganhar o jogo formando a sequencia)
    # como o pc sempre joga como -1 na matriz interna dá pra saber quando dá pra ganhar o jogo se a soma de alguma linha
    # é -2
    if (tabuleiro[0][2] == -1 and tabuleiro[0][1] == -1) or (tabuleiro[2][2] == -1 and tabuleiro[1][1] == -1) or \
            (tabuleiro[1][0] == -1 and tabuleiro[2][0] == -1):
        pos = 1
    elif (tabuleiro[0][0] == -1 and tabuleiro[0][2] == -1) or (tabuleiro[1][1] == -1 and tabuleiro[2][1] == -1):
        pos = 2
    elif (tabuleiro[0][0] == -1 and tabuleiro[0][1] == -1) or (tabuleiro[2][0] == -1 and tabuleiro[1][1] == -1) or \
            (tabuleiro[2][2] == -1 and tabuleiro[1][2] == -1):
        pos = 3
    elif (tabuleiro[0][0] == -1 and tabuleiro[2][0] == -1) or (tabuleiro[1][1] == -1 and tabuleiro[1][2] == -1):
        pos = 4
    elif (tabuleiro[0][0] == -1 and tabuleiro[2][2] == -1) or (tabuleiro[0][2] == -1 and tabuleiro[2][0] == -1) or \
            (tabuleiro[0][1] == -1 and tabuleiro[2][1] == -1) or (tabuleiro[1][0] == -1 and tabuleiro[1][2] == -1):
        pos = 5
    elif (tabuleiro[1][0] == -1 and tabuleiro[1][1] == -1) or (tabuleiro[0][2] == -1 and tabuleiro[2][2] == -1):
        pos = 6
    elif (tabuleiro[0][0] == -1 and tabuleiro[1][0] == -1) or (tabuleiro[0][2] == -1 and tabuleiro[1][1] == -1) or \
            (tabuleiro[2][1] == -1 and tabuleiro[2][2] == -1):
        pos = 7
    elif (tabuleiro[0][1] == -1 and tabuleiro[1][1] == -1) or (tabuleiro[2][0] == -1 and tabuleiro[2][2] == -1):
        pos = 8
    elif (tabuleiro[0][0] == -1 and tabuleiro[1][1] == -1) or (tabuleiro[0][2] == -1 and tabuleiro[1][2] == -1) or \
            (tabuleiro[2][0] == -1 and tabuleiro[2][1] == -1):
        pos = 9
    # aqui é definido quando o pc irá 'defender' (impedir o oponente de ganhar)
    # como o player sempre joga como 1 na matriz interna dá pra saber quando ele está proximo de ganhar se a soma das linhas
    # e colunas dor igual a 2
    elif (tabuleiro[0][2] == 1 and tabuleiro[0][1] == 1) or (tabuleiro[2][2] == 1 and tabuleiro[1][1] == 1) or \
            (tabuleiro[1][0] == 1 and tabuleiro[2][0] == 1):
        pos = 1
    elif (tabuleiro[0][0] == 1 and tabuleiro[0][2] == 1) or (tabuleiro[1][1] == 1 and tabuleiro[2][1] == 1):
        pos = 2
    elif (tabuleiro[0][0] == 1 and tabuleiro[0][1] == 1) or (tabuleiro[2][0] == 1 and tabuleiro[1][1] == 1) or \
            (tabuleiro[2][2] == 1 and tabuleiro[1][2] == 1):
        pos = 3
    elif (tabuleiro[0][0] == 1 and tabuleiro[2][0] == 1) or (tabuleiro[1][1] == 1 and tabuleiro[1][2] == 1):
        pos = 4
    elif (tabuleiro[0][0] == 1 and tabuleiro[2][2] == 1) or (tabuleiro[0][2] == 1 and tabuleiro[2][0] == 1) or \
            (tabuleiro[0][1] == 1 and tabuleiro[2][1] == 1) or (tabuleiro[1][0] and tabuleiro[1][2]):
        pos = 5
    elif (tabuleiro[1][0] == 1 and tabuleiro[1][1] == 1) or (tabuleiro[0][2] == 1 and tabuleiro[2][2] == 1):
        pos = 6
    elif (tabuleiro[0][0] == 1 and tabuleiro[1][0] == 1) or (tabuleiro[0][2] == 1 and tabuleiro[1][1] == 1) or \
            (tabuleiro[2][1] == 1 and tabuleiro[2][2] == 1):
        pos = 7
    elif (tabuleiro[0][1] == 1 and tabuleiro[1][1] == 1) or (tabuleiro[2][0] == 1 and tabuleiro[2][2] == 1):
        pos = 8
    elif (tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1) or (tabuleiro[0][2] == 1 and tabuleiro[1][2] == 1) or \
            (tabuleiro[2][0] == 1 and tabuleiro[2][1] == 1):
        pos = 9
    # aqui é a jogada do pc quando ele começa, ou seja no roud 1
    elif round <= 1:
        pos = 5
    # caso o pc não possa ganhar, defender ou não esteja no começo do jogo ele joga umas jogada aleatória
    else:
        pos = randint(1, 9)
    # mesmo esquema para mudar as matrizes
    while True:
        dpos = pos / 3
        lpos = ceil(dpos) - 1
        if lpos % 2 == 0:
            vlpos = 0
        else:
            vlpos = 1
        if pos % 2 == 0:
            vpos = 0
        else:
            vpos = 1
        if vpos == vlpos:
            cpos = 1
        else:
            if pos % 3 == 0 or pos % 6 == 0 or pos % 9 == 0:
                cpos = 2
            else:
                cpos = 0
        # caso a jogada aléatoria do pc seja em um lugar da matriz que é diferende de 0 ( ou seja, já está ocupado), ele
        # irá jogar de novo
        if tabuleiro[lpos][cpos] != 0:
            pos = randint(1, 9)
            continue
        else:
            tabuleiro[lpos][cpos] += -1
            tabuleiroexterno[lpos][cpos] = simbolo2
            break
    # infelizmente as vezes, por motivos desconhecidos por mim, mesmo o pc podendo jogar atacando ou defendendo ele 
    # joga aletoriamente. Mesmo que a situação nescessária para que ele complete a ação de atacar ou defender seja 
    # verdadeira ele apenas ignora ela e joga aleatoriamente. Se alguem puder me ajudar será muito bem vindo.


# acha o maior número entre os escolhidos
def maior(*núm):
    cont = maior = 0
    for valor in núm:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    return maior


# mostra um resumo da partida
def dadosdapartida():
    global rodadas, j1v, j2v, vf
    textocor(f'{"DADOS DA PARTIDA:":^42}', enegrito, tazul)
    textocor(f'Rodadas =              {rodadas}', enegrito, tazul)
    textocor(f'Vitórias do Jogador =  {j1v}', enegrito, tazul)
    textocor(f'Vitórias do PC =       {j2v}', enegrito, tazul)
    textocor(f'{"VENCEDOR FINAL":<42}', enegrito, tazul)
    textocor(f'{"|":<42}', enegrito, tazul)
    textocor(f'{"|":<42}', enegrito, tazul)
    textocor(f'{"V":<42}', enegrito, tazul)
    textocor(f'{vf:<42}', enegrito, tazul, fvermelho)


# aqui começa o introdução caso o jogo seja iniciado pela primeira vez. o jogador podera escolher entre jogar e qual 
# nível jogar, ver o manual ou sair do programa 
textocor('------------------------------------------', tazul, enegrito)
textocor(f'{"BEM VINDO AO JOGO DA VELHA!!!":^42}', tazul, enegrito)
textocor('------------------------------------------', tazul, enegrito)
sleep(0.5)
textocor('------------------------------------------', tazul, enegrito)
textocor(f'{"MENU":^42}', tazul, enegrito)
op = leiainteiro("""\033[1;32m[ 1 ] > JOGAR
[ 2 ] > INSTRUÇÕES
[ 3 ] > SAIR
>\033[m""")
textocor('------------------------------------------', tazul, enegrito)
while op != 1 and op != 2 and op != 3:
    textocor('ERRO! Digite apenas 1, 2, ou 3', tvermelho, enegrito)
    op = leiainteiro("""\033[1;32m[ 1 ] > JOGAR
[ 2 ] > INSTRUÇÕES
[ 3 ] > SAIR
>\033[m""")
sleep(0.5)
if op == 2:
    textocor('------------------------------------------', tverde, enegrito)
    textocor(f'{"COMO JOGAR":^42}', tverde, enegrito)
    textocor("""Este é o tabuleiro; quando for sua vez,
digite o número correspondente a casa do
tabuleiro para fazer sua jogada.""", tverde)
    #note que da pra jogar apenas olhando o teclado numerico do seu pc
    textocor("""
    |=====||=====||=====|
    |  7  ||  8  ||  9  |
    |=====||=====||=====|
    |  4  ||  5  ||  6  |
    |=====||=====||=====|
    |  1  ||  2  ||  3  |
    |=====||=====||=====|""", tverde, enegrito)
    textocor('------------------------------------------', tverde, enegrito)
    sleep(1)
    textocor('------------------------------------------', tazul, enegrito)
    textocor(f'{"MENU":^42}', tazul, enegrito)
    op = leiainteiro("""\033[1;32m[ 1 ] > JOGAR
[ 2 ] > INSTRUÇÕES
[ 3 ] > SAIR
> \033[m""")
    textocor('------------------------------------------', tazul, enegrito)
    while op != 1 and op != 2 and op != 3:
        textocor('ERRO! Digite apenas 1, 2, ou 3', tvermelho, enegrito)
        op = leiainteiro("""\033[1;32m[ 1 ] > JOGAR
[ 2 ] > INSTRUÇÕES
[ 3 ] > SAIR
> \033[m""")
    sleep(0.5)
if op == 1:
    textocor(f'{"DIFICULDADE":^42}', tazul, enegrito)
    dificuldade = leiainteiro("""\033[1;32m[ 1 ] > FÁCIL
[ 2 ] > DIFÍCIL
[ 3 ] > QUASE IMPOSSÍVEL
> \033[m""")
    while dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
        textocor('ERRO! Digite apenas 1 ou 2', tvermelho, enegrito)
        dificuldade = leiainteiro("""\033[1;32m[ 1 ] > FÁCIL
[ 2 ] > DIFÍCIL
[ 3 ] > QUASE IMPOSSÍVEL
> \033[m""")
    #jogo na dificildade 1
    #o jogador pode escolher começar ou não e pode escolher com qual simbolo jogar
    if dificuldade == 1:
        sleep(0.3)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        sleep(0.5)
        textocor('Você quer jogar como "X" ou como "O"?', tazul)
        sleep(0.5)
        simbolo1 = str(input("""\033[36mDigite "X" e aperte "Enter" para jogar
com "X, ou digite "O" e aperte "Enter" para
jogar como "O": \033[m""")).strip().upper()
        while simbolo1 not in 'XO':
            sleep(0.3)
            textocor('ERRO! Por favor digite apenas "X" ou "O"', tvermelho, enegrito)
            sleep(0.5)
            simbolo1 = str(input("""\033[36mDigite "X" e aperte "Enter" para jogar
com "X, ou digite "O" e aperte "Enter" para
jogar como "O": \033[m""")).strip().upper()
        if simbolo1 == 'X':
            simbolo2 = 'O'
        elif simbolo1 == 'O':
            simbolo2 = 'X'
        sleep(0.5)
        textocor(f'Muito bem, já que você escolheu "{simbolo1}", eu fico com "{simbolo2}".', tazul)
        sleep(1)
        textocor('Agora...', tazul)
        sleep(1)
        textocor('Você quer começar jogando ou quer que eu começe?', tazul)
        sleep(0.5)
        vez = str(input("""\033[36mDigite "EU" e precione "Enter" se você quer
começar, ou digite "PC" e precione "Enter" se
você quer que eu começe: \033[m""")).upper().strip()
        while vez not in 'EU PC':
            sleep(0.3)
            textocor('ERRO! Por favor digite apenas "EU" ou "PC"', tvermelho, enegrito)
            sleep(0.5)
            vez = str(input("""\033[36mDigite "EU" e precione "Enter" se você quer
começar, ou digite "PC" e precione "Enter" se
você quer que eu começe: \033[m""")).upper().strip()
        if vez == 'EU':
            textocor(f'Muito bem, então você vai começar.', tazul)
            jogador = 1
        elif vez == 'PC':
            textocor(f'Muito bem, então eu vou começar.', tazul)
            jogador = -1
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('3', tmagenta)
        sleep(1)
        textocor('2', tmagenta)
        sleep(1)
        textocor('1', tmagenta)
        sleep(1)
        textocor('JÁÁÁÁ!!!', tmagenta)
        sleep(1)
        #o jogo realmente começa aqui
        while True:
            tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tabuleiroexterno = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            round = 0
            #apos 9 rouds, ou seja, todos os quadrados foram preenchidos o jogo terminar com empate
            while round < 9:
                mesaexterna()
                sleep(0.3)
                mostrajogador()
                if jogador == -1:
                    pc()
                else:
                    jogada()
                # caso não empate é porque alquem ganhou antes
                if vervencedor() == 'j1':
                    j1v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('VOCÊ VENCEU ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    break
                elif vervencedor() == 'j2':
                    j2v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('EU VENCI ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    mesaexterna()
                    break
                else:
                    pass
                trocadejogador()
                sleep(0.5)
                round += 1
            rodadas += 1
            if round >= 9:
                mesaexterna()
                sleep(0.3)
                emp += 1
                #pergunta se quer jogar de novo e depois mostra o resumo da partida
                textocor('ISSO FOI UM EMPATE!!!', tvermelho, enegrito, fverde)
            textocor('Esse round terminou, você quer jogar de novo?', tazul)
            verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            while verificacao not in 'SN':
                sleep(0.3)
                textocor('ERRO! Por favor digite apenas "SIM" ou "NÃO"', tvermelho, enegrito)
                sleep(0.5)
                verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            if verificacao == 'S':
                trocadejogador()
                continue
            elif verificacao == 'N':
                break
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"FIM DO JOGO...":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        vf = maior(j1v, j2v)
        if vf == j1v:
            if vf == j1v:
                vf = 'VOCÊ'
            else:
                vf = 'EU'
            dadosdapartida()
        # quse igual a dificuldade 1, mas agora o pc sempre irá tentar te impedir de ganhar porém ira jogar 
        # eleatoriamente caso não haja nescesidade de te impedir de ganhar
    if dificuldade == 2:
        sleep(0.3)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        sleep(0.5)
        textocor('Você quer jogar como "X" ou como "O"?', tazul)
        sleep(0.5)
        simbolo1 = str(input("""\033[36mDigite "X" e aperte "Enter" para jogar
com "X, ou digite "O" e aperte "Enter" para
jogar como "O": \033[m""")).strip().upper()
        while simbolo1 not in 'XO':
            sleep(0.3)
            textocor('ERRO! Por favor digite apenas "X" ou "O"', tvermelho, enegrito)
            sleep(0.5)
            simbolo1 = str(input("""\033[36mDigite "X" e aperte "Enter" para jogar
com "X, ou digite "O" e aperte "Enter" para
jogar como "O": \033[m""")).strip().upper()
        if simbolo1 == 'X':
            simbolo2 = 'O'
        elif simbolo1 == 'O':
            simbolo2 = 'X'
        sleep(0.5)
        textocor(f'Muito bem, já que você escolheu "{simbolo1}", eu fico com "{simbolo2}".', tazul)
        sleep(1)
        textocor('Agora...', tazul)
        sleep(1)
        #note que vc não tem a opção de começar
        textocor('Eu vou começar', tazul)
        jogador = -1
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('3', tmagenta)
        sleep(1)
        textocor('2', tmagenta)
        sleep(1)
        textocor('1', tmagenta)
        sleep(1)
        textocor('JÁÁÁÁ!!!', tmagenta)
        sleep(1)
        #jogo começa igual a dificuldade 1
        while True:
            tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tabuleiroexterno = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            round = 0
            while round < 9:
                mesaexterna()
                sleep(0.3)
                mostrajogador()
                if jogador == -1:
                    pcdificil()
                else:
                    jogada()
                if vervencedor() == 'j1':
                    j1v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('VOCÊ VENCEU ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    break
                elif vervencedor() == 'j2':
                    j2v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('EU VENCI ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    mesaexterna()
                    break
                else:
                    pass
                trocadejogador()
                sleep(0.5)
                round += 1
            rodadas += 1
            if round >= 9:
                emp += 1
                mesaexterna()
                sleep(0.3)
                textocor('ISSO FOI UM EMPATE!!!', tvermelho, enegrito, fverde)
            textocor('Esse round terminou, você quer jogar de novo?', tazul)
            verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            while verificacao not in 'SN':
                sleep(0.3)
                textocor('ERRO! Por favor digite apenas "SIM" ou "NÃO"', tvermelho, enegrito)
                sleep(0.5)
                verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            if verificacao == 'S':
                trocadejogador()
                continue
            elif verificacao == 'N':
                break
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"FIM DO JOGO...":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        vf = maior(j1v, j2v)
        if vf == j1v:
            if vf == j1v:
                vf = 'VOCÊ'
            else:
                vf = 'EU'
            dadosdapartida()
    # aqui começa a dificuldade 3
    #o jogador não pode começar e obrigado a jogar com "O"
    if dificuldade == 3:
        sleep(0.3)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        sleep(0.5)
        textocor('Você vai jogar como "O"', tazul)
        simbolo1 = 'O'
        simbolo2 = 'X'
        sleep(1)
        textocor('Agora...', tazul)
        sleep(1)
        textocor('Eu vou começar', tazul)
        jogador = -1
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"VAMOS COMEÇAR!!!":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        sleep(1)
        textocor('3', tmagenta)
        sleep(1)
        textocor('2', tmagenta)
        sleep(1)
        textocor('1', tmagenta)
        sleep(1)
        textocor('JÁÁÁÁ!!!', tmagenta)
        sleep(1)
        #jogo começa
        while True:
            tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            tabuleiroexterno = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            round = 0
            jogador = -1
            while round < 9:
                mesaexterna()
                sleep(0.3)
                mostrajogador()
                if jogador == -1:
                    # aqui é a função que não está funcionando corretamente. as veses ela relmente vai ganhar o jogo 
                    # quando tiver oportunidade e vai te bloquear de vencer tambem ,mas tem vez que ela não faz 
                    # nenhuma dessas coisa e simplesmente ignora e joga algo aleátorio, oq faz ficar até mais facil 
                    # do que a dificuldade 2 
                    pcquaseimpossivel()
                else:
                    jogada()
                if vervencedor() == 'j1':
                    j1v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('VOCÊ VENCEU ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    break
                elif vervencedor() == 'j2':
                    j2v += 1
                    sleep(0.3)
                    mesaexterna()
                    sleep(0.2)
                    textocor('EU VENCI ESSA RODADA!!!', tvermelho, enegrito, fverde)
                    mesaexterna()
                    break
                else:
                    pass
                trocadejogador()
                sleep(0.5)
                round += 1
            rodadas += 1
            # daqui pra baixo é pra ver se quer jogar de novo e mostrar o resumo da partida
            if round >= 9:
                emp += 1
                mesaexterna()
                sleep(0.3)
                textocor('ISSO FOI UM EMPATE!!!', tvermelho, enegrito, fverde)
            textocor('Esse round terminou, você quer jogar de novo?', tazul)
            verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            while verificacao not in 'SN':
                sleep(0.3)
                textocor('ERRO! Por favor digite apenas "SIM" ou "NÃO"', tvermelho, enegrito)
                sleep(0.5)
                verificacao = str(input("""\033[36mDigite "SIM" e precione "Enter" se você quer
jogar de novo, ou digite "NÃO" e precione "Enter" se
você não quer jogar de novo: \033[m""")).upper().strip()[0]
            if verificacao == 'S':
                trocadejogador()
                continue
            elif verificacao == 'N':
                break
        textocor('------------------------------------------', tazul, enegrito)
        textocor(f'{"FIM DO JOGO...":^42}', tazul, enegrito)
        textocor('------------------------------------------', tazul, enegrito)
        vf = maior(j1v, j2v)
        if vf == j1v:
            vf = 'VOCÊ'
        else:
            vf = 'EU'
        dadosdapartida()
#opção 3 finaliza o programa
if op == 3:
    quit()
    
#qualquer ajuda é bem vinda
