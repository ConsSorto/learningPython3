"""
Funciones 
Funciones con parametros
Funciones con Parametros opcionales
Funciones lamdba 

"""

def imprimir_bienvenida():
    print("Bienvenidos a Python3")

def imprimir_bienvenida_custom(nombre):
    print(f"Bienvenido a Python3 {nombre}")

def imprimir_bienvenida_custom_2(nombre, genero = "M"):
    texto = ""
    if genero == "M" :
      texto = "Bienvenido"
    else :
      texto = "Bienvenida"

    print(f"{texto} a Python3 {nombre}")


imprimir_bienvenida()
imprimir_bienvenida_custom("Cons")
imprimir_bienvenida_custom_2("ASIS","F")
bienvenida = lambda nombre : print(f"Bienvenido {nombre} desde funciones lambda ")
bienvenida("CONS SORTO")

