from Tabuleiro import Tabuleiro

class Jogo:
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__jogadorAtual = jogador1
        self.__tabuleiro = Tabuleiro()

    def iniciarJogo(self):
        while True:
            self.__tabuleiro.imprimirTabuleiro()
            print()
            print(f'Vez do jogador(a) {self.__jogadorAtual.nome}({self.__jogadorAtual.marcador})')

            while True:
                indiceLinha = -1
                indiceColuna = -1
                while True:
                    print('Digite o número da linha: ', end='')
                    resposta = input().strip()
                    if resposta.isdigit():
                        indiceLinha = int(resposta) - 1
                        break
                while True:
                    print('Digite o número da coluna: ', end='')
                    resposta = input().strip()
                    if resposta.isdigit():
                        indiceColuna = int(resposta) - 1
                        break
                
                try:
                    self.__tabuleiro.marcarPosicao(indiceLinha, indiceColuna)
                    print()
                    break
                except Exception as err:
                    print(err)

            if self.__tabuleiro.vitorioso == self.__jogadorAtual.marcador:
                self.__tabuleiro.imprimirTabuleiro()
                print()
                print(f'O jogador {self.__jogadorAtual.nome} ganhou !')
                break
                
            if self.__tabuleiro.empatado:
                self.__tabuleiro.imprimirTabuleiro()
                print()
                print('O jogo empatou !')
                break

            if self.__jogadorAtual == self.__jogador1:
                self.__jogadorAtual = self.__jogador2
            else:
                self.__jogadorAtual = self.__jogador1