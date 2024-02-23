class Mae:

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'
    
    def comer(self) -> None:
        print('Estou comendo...')
    
    def estudar(self) -> None:
        print('Estou estudando...')


class Filha(Mae):

    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)
    
    def brincar(self, brinquedo: str) -> None:
        print(f'Estou brincando com {brinquedo}')


class Neta(Filha):

    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)
    
    def correr(self) -> None:
        print(f'Estou correndo')


ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')
julia = Neta('Rua da Caneca')

clara.brincar('Boneca')

print(ana.endereco)
print(clara.endereco)
print(julia.endereco)
julia.correr()