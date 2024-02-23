from typing import Type

class PessoaA:

    def se_apresentar(self):
        print('Olá, sou a pessoa A')


class PessoaB(PessoaA):

    def __init__(self):
        super().__init__

    def se_apresentar(self):
        print('Estou alterando esse método')


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()


class Animal():

    def comer(self) -> None:
        print('O animal está comendo')
    
    def andar(self) -> None:
        print('O animal está andando')
    
    def dormir(self) -> None:
        print('O animal está dormindo')


class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self) -> None:
        print('O animal está cantando')


class Lobos(Animal):

    def __init__(self):
        super().__init__()
    
    def uivar(self) -> None:
        print('O animal está uivando')


class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self) -> None:
        print('O animal está escorregando')


class Falcao(Aves):

    def __init__(self):
        super().__init__()
    
    def voar(self) -> None:
        print('O animal está voando')


class Pessoa():

    def observar(self, animal: Type[Animal]) -> None:
        animal.comer()


pedro = Pessoa()
pin = Pinguim()

pedro.observar(pin)


class Conexao():

    def conectar(self) -> any:
        print('Conectando ao banco de dados')
    
    def desconectar(self) -> any:
        print('Desconectando ao banco de dados')


class MysqlRepo(Conexao):

    def __init__(self):
        super().__init__()

    def select(self) -> any:
        self.conectar()
        print('SELECT * FROM table')
    
    def insert(self) -> any:
        self.conectar()
        print('Insert Mysql')


class PostgresRepo(Conexao):

    def __init__(self):
        super().__init__()

    def select(self) -> any:
        print('Select Postgres')
    
    def insert(self) -> any:
        print('Insert Postgres')


class CasoDeUso:

    def buscar(self, db_repo: Type[MysqlRepo]) -> any:
        db_repo.select()


mysql = MysqlRepo()
uso = CasoDeUso()

uso.buscar(mysql)