class Automovil:
        puertas = 5
        __ruedas = 4

        def __init__(self):
            print("objeto creadp")
        
        # CONSTRUCTOR
        """
        def __init__(self, placa, color, marca, modelo):
            self.placa = placa
            self.color = color
            self.marca = marca
            self.modelo = modelo
        """

            
        def setpuertas(self, puertas):
            self.puertas = puertas

        def getpuertas(self):
            return self.puertas

        def setruedas(self, ruedas):
            self.__ruedas = ruedas
        
        def getruedas(self):
            return self.__ruedas            
        
        # DESTRUCTOR
        def __del__(self):
            print("objeto destruido")

