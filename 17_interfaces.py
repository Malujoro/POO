from abc import ABC, abstractmethod
from typing import Type

class FormasInterface(ABC):

    @abstractmethod
    def get_perimetro(self) -> int:
        pass

    @abstractmethod
    def get_area(self) -> int:
        pass


class Quadrado(FormasInterface):

    def __init__(self, lado: int):
        self.lado = lado
    
    def get_perimetro(self) -> int:
        return self.lado * 4

    def get_area(self) -> int:
        return self.lado * self.lado


class Retangulo(FormasInterface):

    def __init__(self, comprimento: int, largura: int):
        self.comprimento = comprimento
        self.largura = largura
    
    def get_perimetro(self) -> int:
        return (self.comprimento * 2) + (self.largura * 2)

    def get_area(self) -> int:
        return self.comprimento * self.largura


class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def medir_perimetro(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu o perímetro: {terreno.get_perimetro()}m')

    def medir_area(self, terreno: Type[FormasInterface]):
        print(f'{self.nome} mediu a área: {terreno.get_area()}m²')


engenheiro = Engenheiro('Geraldo')
terrenoQuadrado = Quadrado(4)
terrenoRetangular = Retangulo(2, 3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoQuadrado)
print()
engenheiro.medir_area(terrenoRetangular)
engenheiro.medir_perimetro(terrenoRetangular)