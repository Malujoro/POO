class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')

class Palhaco:

    def apresentar_show(self):
        print('Palhaco apresentando seu show')

class Domador:

    def apresentar_show(self):
        print('Domador apresentando seu show')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(domador)