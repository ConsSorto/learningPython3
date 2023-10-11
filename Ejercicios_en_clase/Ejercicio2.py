"""
ciclo infinito con while
diccionario para productos, dentro de un list
for para recorrer el list y encontrar el producto
funcion para encontrar el producto y funciones para sumar o restar del inventario

"""

def mostrar_producto(producto):
    return f"Nombre : {producto['nombre']}, Codigo : {producto['codigo']}, Costo : {producto['costo']}, Precio Venta : {producto['precio_venta']}, Cantidad en inventario : {producto['cantidad_inventario']} "

def acciones_inventario(accion):
    print(f"****** {accion} al inventario de un producto ******")
    nombre_producto = input('Ingrese nombre del producto :')

    indice = 0
    mostrado = False
    for producto in productos:
        if nombre_producto == producto['nombre'] :
            print(mostrar_producto(producto))    
            mostrado = True
            
        if not mostrado:    
            indice += 1

    if not mostrado:
        print('XXXXX Producto no encontrado XXXXX')
    else :
        try:
            cantidad = float(input('Ingrese cantidad :'))
        except:
            print('XXXXX valor tiene que ser un decimal XXXXX')
        else:
            if accion == "Agregar":
                productos[indice]['cantidad_inventario'] += cantidad
            else:
                productos[indice]['cantidad_inventario'] -= cantidad


productos = []
seguir = True
opcion = 0

while(seguir):
    try:
        print('******** Menu ********')
        print('1. Ingrese un producto')
        print('2. Mostrar todos los productos')
        print('3. Mostrar un producto')
        print('4. Agregar al inventario de un producto')
        print('5. Restar del inventario de un producto')
        print('6. Salir')
        opcion = int(input('Igrese opcion :'))
    except:
        print("XXXXX Opcion no valida XXXXX")
    else:
        match opcion:
            case 1:
                try :
                    producto = {}
                    print('****** Ingrese el producto ******')
                    producto['nombre'] = input('Nombre del Producto : ')
                    producto['codigo'] = input('Codigo del Producto : ')
                    producto['costo'] = float(input('Costo del Producto : '))
                    producto['precio_venta'] = float(input('Precio de venta del Producto : '))
                    producto['cantidad_inventario'] = float(input('Cantidad en inventario del Producto : '))
                    productos.append(producto)
                except:
                    print('XXXXX valor tiene que ser un decimal XXXXX')
                else:
                    print('Producto ingresado con exito')
            case 2:
                print(f"****** Productos {len(productos)} ******")
                contador = 1

                for producto in productos:
                    print(f"Producto {contador}")
                    print(mostrar_producto(producto))
                    contador += 1
            case 3:
                print(f"****** Mostrar informacion de un producto ******")
                nombre_producto = input('Ingrese nombre del producto :')
                
                mostrado = False
                for producto in productos:
                    if nombre_producto == producto['nombre'] :
                        print(mostrar_producto(producto))    
                        mostrado = True 
                if not mostrado:
                    print('XXXXX Producto no encontrado XXXXX')
            case 4:
                acciones_inventario("Agregar")
            case 5:
                acciones_inventario("Restar")

            case 6:
                print("****** Hasta Luego ******")
                seguir = False
            case default:
                print("XXXXX Opcion no valida XXXXX")