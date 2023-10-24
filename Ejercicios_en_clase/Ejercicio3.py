"""
Un restaurante desea un sistema para almacenar  la comida que prepara,.
de la comida se desea el nombre del plato, el tipo de plato que puede ser ensalada
, carnes, hamburguesas etc., 
así mismo la comida tendrá una lista de ingredientes y las cantidades 
que se usa de cada ingrediente la unidad de medida y el costo por unidad de medida.
de cada comida se desea saber la receta, en la cual se describe paso a paso la preparación,
para lo cual se desea el orden en el que se realizan los pasos y la descripción de este.
la forma de ingreso de los datos es que primero ingresan la comida luego, a esta comida 
se le ingresaran los ingredientes mediante otro item del menu, de igual forma se realiza con la receta,
 se debera mostrar el listado de todas las comidas y poder ver una comida en especifico
"""

def mostrar_comida(comida):
    return f"Nombre : {comida['nombre']}, Tipo : {comida['tipo']}"


comidas = []
seguir = True
opcion = 0

while(seguir):
    try:
        print('******** Menu ********')
        print('1. Ingrese Comida')
        print('2. Mostrar todos las comidas')
        print('3. Mostrar una Comida')
        print('4. Agregar Ingredientes')
        print('5. Agregar Receta')
        print('6. Salir')
        opcion = int(input('Ingrese opcion :'))
    except:
        print("XXXXX Opcion no valida XXXXX")
    else:
        match opcion:
            case 1:
                comida = {}
                print('****** Ingrese Comida ******')
                comida['nombre'] = input('Nombre de la Comida : ')
                comida['tipo'] = input('Tipo de Comida : ')
                comidas.append(comida)
                print('Producto ingresado con exito')
            case 2:
                print(f"****** Comidas {len(comidas)} ******")
                contador = 1
   
                for comida in comidas:
                    print(f"Comida {contador}")
                    print(mostrar_comida(comida))
                    contador += 1
            case 3:
                print(f"****** Mostrar informacion de una comida ******")
                nombre_comida = input('Ingrese nombre de la comida :')
                
                mostrado = False
                for comida in comidas:
                    if nombre_comida == comida['nombre'] :
                        print(mostrar_comida(comida))    
                        mostrado = True
                 
                if not mostrado:
                    print('XXXXX Comida no encontrada XXXXX')
            case 4:
                print(f"****** Agregar ingredientes de una comida ******")
                nombre_comida = input('Ingrese nombre de la comida :')
 
                indice = 0
                mostrado = False
                for comida in comidas:
                    if nombre_comida == comida['nombre'] :
                        print(mostrar_comida(comida))    
                        mostrado = True 
                        
                    if not mostrado:    
                        indice += 1
                            
                if not mostrado:
                    print('XXXXX Comida no encontrada XXXXX')
                else:
                    print('----- Para salir debe ingresar la palabra "Salir" en el nombre del ingrediente -----')
                    
                    ingredientes = []
                    ingresar = True
                    while(ingresar):
                        ingrediente = {}
                        ingrediente['nombre'] = input('Nombre del ingrediente : ')
                        if ingrediente['nombre'] == "Salir":
                            ingresar = False
                            continue;

                        try :
                            ingrediente['costo'] = float(input('Costo del Ingrediente : '))
                            ingrediente['cantidad'] = float(input('Cantidad del Ingrediente : '))
                            ingrediente['um'] = input('UM del ingrediente : ')
                            ingredientes.append(ingrediente)
                        except:
                            print('XXXXX valor tiene que ser un decimal XXXXX')
                        else:
                            print('Ingrediente ingresado con exito')
                    
                    comidas[indice]['ingredientes'] = ingredientes

            case 5:
                print(f"****** Agregar Receta de una comida ******")
                nombre_comida = input('Ingrese nombre de la comida :')
 
                indice = 0
                mostrado = False
                for comida in comidas:
                    if nombre_comida == comida['nombre'] :
                        print(mostrar_comida(comida))    
                        mostrado = True 
                        
                    if not mostrado:    
                        indice += 1

                if not mostrado:
                    print('XXXXX Comida no encontrada XXXXX')
                else:
                    print('----- Para salir debe ingresar la palabra "Salir" en la descripcion del paso -----')
                    
                    pasos = []
                    ingresar = True
                    while(ingresar):
                        descripcion = input('Ingrese Descripcion : ') 
                        
                        if descripcion == "Salir":
                            ingresar = False
                            continue;
                        else:
                            pasos.append(descripcion)

                    comidas[indice]['receta'] = pasos
            case 6:
                print("****** Hasta Luego ******")
                seguir = False
            case default:
                print("XXXXX Opcion no valida XXXXX")
    print(comidas)