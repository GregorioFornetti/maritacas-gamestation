from genericpath import isdir
from os import listdir

nomes_jogos = listdir('jogos')
nomes_jogos.remove('__pycache__')
nomes_jogos.remove('__init__.py')

__all__ = [*nomes_jogos, 'nomes_jogos']