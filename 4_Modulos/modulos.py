"""
los modulos en python son agrupaciones de codigo que se pueden reutilizar en lugares distintos al que fueron creados
para usar un modulo completo usamos la sentencia import pero para usar solo unas funciones o partes de una modulo usamos la sentencia from

"""

import modFunciones

from modFunciones2 import ValidarNumerosIfElseIf

modFunciones.imprimir_bienvenida()
 
numero1 = int(input("Ingrese numero 1 :"))
numero2 = int(input("Ingrese numero 2 :"))

ValidarNumerosIfElseIf(numero1, numero2)

