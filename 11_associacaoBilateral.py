class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua dos Limoeiros'
        self.__proprietario = None
    
    def acender_luzes(self) -> None:
        print('Estou acendendo as Luzes')
    
    def get_endereco(self) -> str:
        return self.__endereco

    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario
    
    def get_proprietario(self) -> any:
        return self.__proprietario


class Pessoa:

    def __init__(self, nome: str) -> None:
        self.__local = None
        self.__nome = nome
    
    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

    def se_apresentar(self) -> None:
        print(f'Olá, eu sou {self.__nome}')
    
    def set_local(self, local: any) -> None:
        self.__local = local
    
    def get_local(self) -> any:
        return self.__local
    

casa_da_ana = Casa()
ana = Pessoa('Ana')

ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana)

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()

ana.apresentar_local()