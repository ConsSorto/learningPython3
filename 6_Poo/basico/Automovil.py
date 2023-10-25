

class Automovil:
        tipo = "automovil"
        puertas = 5
        ruedas = 4
        placa = "HCF12345"
        color = "blanco/amarillo"
        marca = "Toyota"
        modelo = "corolla"
        velocidad = 0

        def gettipo (self):
             return Automovil.tipo

        def encender(self):
            return "el automovil esta encendido"

        def apagar(self):
            return "el automovil esta apagado"

        def acelerar(self, numero):
            self.velocidad += numero 
            return f"el automovil acelero, velocidad : {self.velocidad}"

        def frenar(self):
            self.velocidad -= 1 
            return f"el automovil freno, velocidad : {self.velocidad}"
        

