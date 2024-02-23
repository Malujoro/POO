class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if(isinstance(valor, bool)):
            self.__estado = valor

class Pessoa:

    def __init__(self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print(f'Dirigindo um(a) {veiculo}')

    def cantar(self) -> None:
        print('Lalala')

    def apresentar_idade(self) -> int:
        return self.idade