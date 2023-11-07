
from abc import ABC, abstractmethod

class Animal(ABC):
    def saludar(self):
        print("hola")

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def comosealimenta(self):
        pass

class Perro(Animal):

    def mover(self):
        print('corre')

    def comosealimenta(self):
        print("le da comida su amo")

class Gato(Animal):

    def mover(self):
        print('suben al techo')
    
    def comosealimenta(self):
        print("se roba la comida")


class Sabueso(Perro):
    pass
    
perro = Perro()

perro.mover()
perro.comosealimenta()


gato = Gato()

gato.mover()
gato.comosealimenta()

sabueso = Sabueso()

sabueso.mover()
sabueso.comosealimenta()
sabueso.saludar()

#animal = Animal()
