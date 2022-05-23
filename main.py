from Jogo import Jogo
import configs
import json
import os

nomesDiretorios = os.listdir('jogos')

listaJogos = []
for nomeDiretorio in nomesDiretorios:
    infoJogo = json.load(open(configs.DIRETORIO_JOGOS + os.path.sep + nomeDiretorio + os.path.sep + configs.GAME_INFO_FILE))
    listaJogos.append(Jogo(infoJogo['nome'], infoJogo['autores'], nomeDiretorio, infoJogo['arquivo principal']))

while True:
    print('Maritacas gamestation')
    print('Lista de jogos')

    for numJogo, jogo in enumerate(listaJogos):
        print()
        jogo.imprimirJogo(numJogo + 1)
        print()
    
    print('Digite o número do jogo que deseja jogar (0 para finalizar): ', end='')
    try:
        numJogo = int(input())
        if numJogo == 0:
            break
        else:
            listaJogos[numJogo - 1].jogar()
    except:
        print('Ocorreu um erro na seleção do jogo, tente novamente !')
    