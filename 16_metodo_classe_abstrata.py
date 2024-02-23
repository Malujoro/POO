from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self):
        self.atributo = 'Olá mundo'

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass


class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Implementando método abstrato')


filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou aqui')
filha.metodo_abstrato()

# abstractClass = AbstractClass()
# abstractClass.metodo('Fazendo algo')