from typing import Dict, Type

class PessoaA:

    def se_apresentar(self):
        print('Olá, sou a pessoa A')


class PessoaB(PessoaA):

    def __init__(self):
        super().__init__

    def se_apresentar(self):
        print('Estou alterando esse método')


class PessoaC(PessoaB):

    def __init__(self):
        super().__init__()


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()


class Repositorio:

    def select(self, nome: str) -> Dict:
        return {"nome": nome, "idade": 32}

    def insert(self, nome: str, idade: int) -> Dict:
        return {"nome": nome, "idade": idade}


class Insersor:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repo = repositorio
    
    def inserir_dado(self, nome: str, idade: int) -> Dict:
        registro = self.__repo.select(nome)
        if(registro):
            raise Exception('O Registro já existe')

        novo_registro = self.__repo.insert(nome, idade)
        return novo_registro
    

class RepositorioFaker(Repositorio):
    
    def __init__(self):
        super().__init__()
    
    def select(self, name: int) -> None:
        return None


repo = RepositorioFaker()
insersor = Insersor(repo)

data = insersor.inserir_dado('Lhama', 26)
print(data)