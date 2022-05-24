
class Jogador:
    def __init__(self, nome, marcador):
        self.__nome = nome
        self.__marcador = marcador
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def marcador(self):
        return self.__marcador