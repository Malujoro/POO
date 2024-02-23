class MinhaClasse:

    estatico = 'lhama'

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self) -> None:
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'


# obj1 = MinhaClasse(True)
# obj2 = MinhaClasse(False)

# obj1.mudar_estatico()

# obj1.print_estatico()
# obj2.print_estatico()

class Loja:
    
    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)
    
    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa


loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(1.5)

print(loja_praia.vender())
print(loja_centro.vender())