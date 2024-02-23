from typing import Type
from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def informacoes(self) -> None:
        raise 'Implemente o método informacoes_produto'


class Produto(Item):

    def __init__(self, prod_nome: str, prod_valor: int) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor
    
    def informacoes(self) -> None:
        print(f'Produto: {self.__prod_nome} | Valor: R${self.__prod_valor},00')


class Servico(Item):

    def __init__(self, prod_servico: str, prod_valor: int) -> None:
        self.__prod_servico = prod_servico
        self.__prod_valor = prod_valor
    
    def informacoes(self) -> None:
        print(f'Serviço: {self.__prod_servico} | Valor: R${self.__prod_valor},00')
    

class CarrinhoDeCompras:

    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Item]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print('Compras finalizadas\n')

        for produto in self.__produtos:
            produto.informacoes()
        
        self.__produtos = []


car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)
tv = Produto('TV', 5)
pedreiro = Servico('Pedreiro', 140)

car.adicionar_produto(monitor)
car.adicionar_produto(cerveja)
car.adicionar_produto(tv)
car.adicionar_produto(pedreiro)
car.finalizar_compra()