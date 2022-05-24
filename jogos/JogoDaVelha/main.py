from Jogo import Jogo
from Jogador import Jogador

while True:
    print()
    print('Jogo da Velha')
    print('1 - Começar jogo')
    print('2 - Sair do jogo')
    print()
    print('Digite uma opção (1 ou 2): ', end='')

    resposta = input().strip()
    if resposta == '1':
        print('Digite o nome do 1° jogador(X): ', end='')
        nomeJogador1 = input()
        print('Digite o nome do 2° jogador(O): ', end='')
        nomeJogador2 = input()
        jogo = Jogo(Jogador(nomeJogador1, 'X'), Jogador(nomeJogador2, 'O'))
        print()
        jogo.iniciarJogo()
    elif resposta == '2':
        print()
        break
    else:
        print('Comando inválido, tente novamente')
    