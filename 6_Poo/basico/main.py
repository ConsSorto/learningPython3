from Automovil import Automovil

miautomovil = Automovil()
automivil2 = Automovil()

miautomovil.marca = "Datsun"
automivil2.marca = "Nissan"

print(miautomovil.marca)
print(automivil2.marca)

print(automivil2.velocidad)
automivil2.acelerar(5)
print(f"Marca : {automivil2.marca} Velocidad : {automivil2.velocidad}")
print(f"Marca : {miautomovil.marca} Velocidad : {miautomovil.velocidad}")

print(automivil2.gettipo())
print(miautomovil.gettipo())

Automovil.tipo = "Carro"

print(automivil2.gettipo())
print(miautomovil.gettipo())


