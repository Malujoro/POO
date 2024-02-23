from typing import Type
from abc import ABC, abstractmethod


class Repositorio(ABC):

    @abstractmethod
    def inserir(self, dado) -> None:
        raise 'Deve implementar o método inserir'
    
    @abstractmethod
    def deletar(self, dado) -> None:
        raise 'Deve implementar o método deletar'


class MySqlRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f'Inserindo {dado} no banco MySql')

    def deletar(self, dado) -> None:
        print(f'deletando {dado} no banco MySql')


class MongoRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f'Inserindo {dado} no banco Mongo')

    def deletar(self, dado) -> None:
        print(f'deletando {dado} no banco Mongo')


class Usuario:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dado(self, dado: any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)


usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dado(23)

usuario = Usuario(MongoRepositorio())
usuario.armazenar_dado(23)