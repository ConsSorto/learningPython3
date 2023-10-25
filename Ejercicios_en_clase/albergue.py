"""
Un albergue de perros desea realizar un sistema para el control
de los animales que en el se encuentran, para llevar este control
se desea saber de los perros, el nombre, la raza, el peso, si es
docil o no, si es peligroso o no, y si esta aun disponible para su adopcion,

El sistema presentara la funcionalidad de ingresar animales, ver todos los animales,
ver un animal en especifico y cambiar el estado de disponible para adopcion.
"""

class Perro:
    nombre = None
    raza = None
    peso = None
    
    def __init__(self):
        self.docil = False
        self.peligroso = True
        self.__disponible = True

    def adoptado(self):
        if self.__disponible:
            label = "Si"
        else:
            label = "No"
        
        return label
    
    def descripcion(self):
        return f"Nombre : {self.nombre} Raza : {self.raza}"

    def __str__(self):
        return f"Nombre : {self.nombre} Raza : {self.raza} Disponible : {self.adoptado()}"


perro = Perro()

perro.nombre = "Clifor"
perro.raza = "Mestizo"
perro.peso = 100

print(perro)
