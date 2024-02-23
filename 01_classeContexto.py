# Define/Declara a classe
class MinhaClasse:
    # Inicializa os atributos da classe (as "variáveis")
    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo'
        self.meu_atributo2 = att

    # Inicializa os métodos da classe (as "funções")
    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        return num * mult
    
class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avançado')
    
    def voltar_canal(self):
        print('Voltar o canal')
    
    def escolher_canal(self, canal):
        print(f'Alterado para o canal: {canal}')


controle_sala = ControleRemoto('Samsung', 'Sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal() 
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('LG', 'Quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
controle_quarto.voltar_canal()
controle_quarto.escolher_canal(20)