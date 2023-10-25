
class Metodos:
        # CONSTRUCTOR
        def __init__(self, nombre):
            self.nombre = nombre

        def metodoinstancia(self):
            print("este es un metodo de la instancia")

        #DECORADOR CLASE
        #No pueden acceder a los atributos de la instancia.
        #Pero si pueden modificar los atributos de la clase  
        @classmethod
        def metodoclase(cls):
            print("metodo de la clase")
       
        #DECORADOR ESTATICO
        #no pueden modificar el estado ni de la clase ni de la instancia.
        @staticmethod
        def metodoestatico():
            print("este es un metodo estatico")
       
        
        # DESTRUCTOR
        def __del__(self):
            print("objeto destruido")

