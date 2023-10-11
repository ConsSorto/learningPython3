"""
realizar ciclo infinito para el menu

1 agregar un arreglo con diccionarios para cada mascota
2 realizar un for para ver el arreglo
3 mostrar del arreglo el indice que sigue.
4 salir seria cambiar a false el control del ciclo infinito

todas las opciones se manejaria con un match o un if


"""
def mostrar_datos_mascota(indice, mascota):
    print(f"N. {indice} : Nombre : {mascota['nombre']}, Tipo : {mascota['tipo']}, Descripcion : {mascota['descripcion']} ")    
    

opcion = 0
lista_mascotas = []
indice_mascota_actual = 0
seguir = True 
while(seguir):
    print("\n******************* LIST *******************")
    print(lista_mascotas)
    try:
        print("\n******************* Menu *******************")
        print("1. Ingresar Mascota")
        print("2. Mostrar Mascotas")
        print("3. Siguiente Mascota")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion : "))
    except:
        print("xxxxxxx ------ Opcion no valida ------ xxxxxxx\n")
    else:
        match opcion:
            case 1:
                print("\n****** Ingrese Mascota ****** ")
                mascota = {}
                mascota['nombre'] = input("- Nombre de la mascota : ")
                mascota['tipo'] = input("- Tipo de la mascota : ")
                mascota['descripcion'] = input("- Descripcion : ")
                lista_mascotas.append(mascota)
            case 2:
                print("\n****** Mostrar Mascotas ****** ")
                contador = 1

                for mascota in lista_mascotas:
                    print(mascota)
                    mostrar_datos_mascota(contador, mascota)
                    contador += 1
            case 3:
                print("\n****** Siguiente Mascota ****** ")

                if (len(lista_mascotas) > 0 and indice_mascota_actual < len(lista_mascotas)) :
                    mostrar_datos_mascota(indice_mascota_actual + 1, lista_mascotas[indice_mascota_actual])
                    indice_mascota_actual += 1 
                else:
                    print("Ya no hay mas mascotas")
            case 4:
                print("Hasta la proxima.")
                seguir = False
            case default:
                print("xxxxxxx ------ Opcion no valida ------ xxxxxxx\n")
          
        