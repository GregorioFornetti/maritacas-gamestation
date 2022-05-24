from Posicao import Posicao

class Tabuleiro:
    def __init__(self, marcadorJogador1='X', marcadorJogador2='O', espacamentoVertical=0, espacamentoHorizontal=1, imprimirCabeçalhos=True):
        self.__posicoes = [[Posicao(), Posicao(), Posicao()],
                           [Posicao(), Posicao(), Posicao()],
                           [Posicao(), Posicao(), Posicao()]]
        self.__marcadorJogador1 = marcadorJogador1
        self.__marcadorJogador2 = marcadorJogador2
        self.__jogadorAtual = 1
        self.__espacamentoVertical = espacamentoVertical
        self.__espacamentoHorizontal = espacamentoHorizontal
        self.__imprimirCabeçalhos = imprimirCabeçalhos
    
    def __imprimirLinhaVertical(self):
        for _ in range(self.__espacamentoVertical):
            if self.__imprimirCabeçalhos:
                print('  ', end='')
            print(f'{" " * (self.__espacamentoHorizontal * 2 + 1)}|{" " * (self.__espacamentoHorizontal * 2 + 1)}|')
    
    def imprimirTabuleiro(self):
        if self.__imprimirCabeçalhos:
            print(f'{" " * (self.__espacamentoHorizontal + 2)}1{" " * (self.__espacamentoHorizontal * 2 + 1)}2{" " * (self.__espacamentoHorizontal * 2 + 1)}3')
            print()
        
        for numeroLinha in range(1, 4):
            self.__imprimirLinhaVertical()
            
            if self.__imprimirCabeçalhos:
                print(f'{numeroLinha} ', end='')
            print(f'{" " * self.__espacamentoHorizontal}{self.__posicoes[numeroLinha-1][0]}{" " * self.__espacamentoHorizontal}|', end='')
            print(f'{" " * self.__espacamentoHorizontal}{self.__posicoes[numeroLinha-1][1]}{" " * self.__espacamentoHorizontal}|', end='')
            print(f'{" " * self.__espacamentoHorizontal}{self.__posicoes[numeroLinha-1][2]}')

            self.__imprimirLinhaVertical()

            if numeroLinha != 3:
                if self.__imprimirCabeçalhos:
                    print('  ', end='')
                print(f'{"-" * (self.__espacamentoHorizontal * 2 + 1)} {"-" * (self.__espacamentoHorizontal * 2 + 1)} {"-" * (self.__espacamentoHorizontal * 2 + 1)}')
    
    def marcarPosicao(self, indiceLinha, indiceColuna):
        if not type(indiceLinha) is int or not type(indiceColuna) is int:
            raise TypeError('Os indices precisam ser inteiros !')
        
        if indiceLinha > 3 or indiceLinha < 0 or indiceColuna > 3 or indiceColuna < 0:
            raise ValueError('Os indices precisam estar entre 0 e 2 !')
        
        if self.__posicoes[indiceLinha][indiceColuna].marcada:
            raise Exception('A posição selecionada já está marcada !')
        
        if self.__jogadorAtual == 1:
            self.__posicoes[indiceLinha][indiceColuna].marcarPosicao(self.__marcadorJogador1)
            self.__jogadorAtual = 2
        else:
            self.__posicoes[indiceLinha][indiceColuna].marcarPosicao(self.__marcadorJogador2)
            self.__jogadorAtual = 1
    
    @staticmethod
    def __verificarMarcacoesIguais(listaPosicoes):
        marcacao = listaPosicoes[0].marcacao
        return all([posicao.marcada for posicao in listaPosicoes]) and all([posicao.marcacao == marcacao for posicao in listaPosicoes])

    @property
    def vitorioso(self):
        for i in range(3):
            # Verificar se ocorreu alguma vitoria na horizontal
            if self.__verificarMarcacoesIguais(self.__posicoes[i]):
                return self.__posicoes[i][0].marcacao
            
            # Verificar se ocorreu alguma vitorina na vertical
            if self.__verificarMarcacoesIguais([self.__posicoes[0][i], self.__posicoes[1][i], self.__posicoes[2][i]]):
                return self.__posicoes[0][i].marcacao
        
        # Verificando vitoria na diagonal principal
        if self.__verificarMarcacoesIguais([self.__posicoes[0][0], self.__posicoes[1][1], self.__posicoes[2][2]]):
            return self.__posicoes[0][0].marcacao
        
        # Verificando vitoria na diagonal secundaria
        if self.__verificarMarcacoesIguais([self.__posicoes[0][2], self.__posicoes[1][1], self.__posicoes[2][0]]):
            return self.__posicoes[0][2].marcacao
        
        return False


    @property
    def empatado(self):
        for linha in self.__posicoes:
            for posicao in linha:
                if not posicao.marcada:
                    return False
        return True
