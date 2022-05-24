class Posicao:
    def __init__(self):
        self.__marcada = False
        self.__marcacao = ' '
    
    def __str__(self):
        return self.__marcacao
    
    def marcarPosicao(self, caractereMarcacao):
        self.__marcada = True
        self.__marcacao = caractereMarcacao
    
    @property
    def marcada(self):
        return self.__marcada
    
    @property
    def marcacao(self):
        return self.__marcacao