from abc import ABC, abstractmethod
from typing import Type

class AveVoadora:

    @abstractmethod
    def comer(self) -> None:
        raise 'Should Implement comer method'

    @abstractmethod
    def voar(self) -> None:
        raise 'Should Implement voar method'

    @abstractmethod
    def gritar(self) -> None:
        raise 'Should Implement gritar method'


class AveQueNaoVoa:

    @abstractmethod
    def comer(self) -> None:
        raise 'Should Implement comer method'

    @abstractmethod
    def gritar(self) -> None:
        raise 'Should Implement gritar method'

class Canario(AveVoadora):
    
    def comer(self) -> None:
        print('Canário está comendo')
    
    def voar(self) -> None:
        print('Canário está voando')

    def gritar(self) -> None:
        print('Canário está gritando')


class Pinguim(AveQueNaoVoa):
    
    def comer(self) -> None:
        print('Pinguim está comendo')
        self.__acasalar()
    
    def voar(self) -> None:
        None

    def gritar(self) -> None:
        print('Pinguim está gritando')

    def __acasalar(self) -> None:
        print('Agora vou acasalar...')


class Agente():

    def observar(self, ave: any) -> None:
        ave.comer()


agente = Agente()
ave = Canario()
pinguim = Pinguim()

agente.observar(ave)
pinguim.comer()