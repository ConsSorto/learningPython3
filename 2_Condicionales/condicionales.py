"""
if else, is elif else, if if else else

en el caso de switch se puede programar una funcion con el uso de if o usar el match

"""

numero1 = int(input("Ingrese numero1 :"))
numero2 = int(input("Ingrese numero2 :"))

if numero1 > numero2:
    print("El numero1 es mayor al numero2")
else : 
    print("El numero2 es igual o mayor al numero1")


if numero1 > numero2:
    print("El numero1 es mayor que el numero2")
elif numero1 == numero2: 
    print("El numero1 es igual al numero2")
else :
    print("El numero2 es mayor al numero1")


if numero1 > numero2:
    print("El numero1 es mayor que el numero2")
else :
    if numero1 == numero2: 
        print("El numero1 es igual al numero2")
    else :
        print("El numero2 es mayor al numero1")

match numero1:
    case 0:
        print("el numero ingresado es 0")
    case 1:
        print("el numero ingresado es 1")
    case 5:
        print("el numero ingresado es 5")        
    case default:
        print("no hay una opcion para el numero igresado, opciones 0,1,5")        