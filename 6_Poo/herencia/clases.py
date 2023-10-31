class Animal:
    def __init__(self, patas, tipo, alimento):
        self.patas = patas
        self.tipo = tipo
        self.alimento = alimento

    
class Perro(Animal):

    def __init__(self, nombre):
        super().__init__(4, 'Mamifero', 'De todo')
        self.nombre = nombre
    def __str__(self):
        return f"Nombre : {self.nombre}, Tipo : {self.tipo}, Patas : {self.patas}, Alimento : {self.alimento}"

perro  = Perro('Cova')

print(perro)