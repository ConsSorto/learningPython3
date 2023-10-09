"""
Mostrando los tipos de variables

"""

def tipo_dato(dato):
    print (f"la variable es de tipo de dato {type(dato)}")

entero = 1
string = "esto es un string"
float = 1.1
boolean = True
list = [entero, string, float]
dict = {"entero" : entero, "string" : string}
variable = input("ingrese cualquier tipo de valor : ")

tipo_dato(entero)
tipo_dato(string)
tipo_dato(float)
tipo_dato(boolean)
tipo_dato(list)
tipo_dato(dict)
tipo_dato(variable)


