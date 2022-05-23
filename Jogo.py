import subprocess
import sys
import os
import configs

class Jogo:

    def __init__(self, nomeJogo, autores, nomeDiretorio, arquivoPrincipal):
        self.__nomeJogo = nomeJogo
        self.__autores = autores
        self.__nomeDiretorio = nomeDiretorio
        self.__arquivoPrincipal = arquivoPrincipal
    
    def imprimirJogo(self, numJogo):
        fraseAutores = 'Autores: '
        espacamentoInicial = len(str(numJogo)) + 3
        espacamentoAutores = 4
        espacamentoFinalNomesAutores = espacamentoInicial + espacamentoAutores + len(fraseAutores)

        print(f'{numJogo} - {self.__nomeJogo}')
        if self.__autores:
            print(f'{" " * espacamentoInicial}{" " * espacamentoAutores}{fraseAutores}{self.__autores[0]}')
            for autor in self.__autores[1::]:
                print(f'{" " * espacamentoFinalNomesAutores}{autor}')

    
    def jogar(self):
        caminhoJogo = configs.DIRETORIO_JOGOS + os.path.sep + self.__nomeDiretorio + os.path.sep + self.__arquivoPrincipal
        subprocess.run([sys.executable, caminhoJogo], shell=True)

    @property
    def nomeJogo(self):
        return self.__nomeJogo

    @property
    def autores(self):
        return self.__autores