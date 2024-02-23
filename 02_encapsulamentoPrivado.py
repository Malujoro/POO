class Calculadora:

    def calcular(self, op, num1, num2):
        if(op == '+'):
            return self.__adicionar(num1, num2)
        elif (op == '-'):
            return self.__subtrair(num1, num2)
        else:
            print('Operação Inválida')
    
    def __adicionar(self, num1, num2):
        return num1 + num2
    
    def __subtrair(self, num1, num2):
        return num1 - num2

 
calculadora = Calculadora()
resultado = calculadora.calcular('+', 3, 2)
print(resultado)
# print(calculadora.calcular('-', 4, 2))
# calculadora.calcular(1, 1, 2)

class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        
    def correr(self):
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('Bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)

ronaldo = Pessoa('Ronaldo', 32, '123456789ab')
ronaldo.beber('água')