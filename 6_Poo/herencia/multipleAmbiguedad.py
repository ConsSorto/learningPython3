"""
una veterinaria desea hacer un sistema para el ingreso de sus animales,
de esta veterinaria se atienden perro, gatos y aves.
se desea ingresar los animales y listarlos.


Animal
Mascota
Perro 
Gato
Ave

"""



class Animal:
    __tipo = None
    __alimento = None
    __genero = None
   
    def __init__(self, tipo, alimento, genero):
        self.__tipo = tipo
        self.__alimento = alimento
        self.__genero = genero

    def formaDeMoverse(self):
        return "Caminando"

class Mascota:
    __nombre = None
    __dueno = None

    def __init__(self, nombre, dueno):
        self.__tipo = nombre
        self.__alimento = dueno
    
    def formaDeMoverse(self):
        return "Con el dueño"

class Perro(Animal, Mascota):
    def __init__(self, genero, nombre, dueno):
        super().__init__('Perro', 'Carne', None)
        self.__genero = genero
        self.__nombre = nombre
        self.__dueno = dueno

    
class Gato(Animal, Mascota):
    def __init__(self, genero, nombre, dueno):
        super().__init__('Gato', 'Peces', None)
        self.__genero = genero
        self.__nombre = nombre
        self.__dueno = dueno

class Ave(Animal, Mascota):
    vuela = None

    def __init__(self, genero, nombre, dueno, vuela):
        super().__init__('Ave', 'Semillas', None)
        self.__genero = genero
        self.__nombre = nombre
        self.__dueno = dueno
        self.vuela = vuela

    def formaDeMoverse(self):
        return "Volando"


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
        print("3. Salir")
        opcion = int(input("Ingrese una opcion : "))
    except:
        print("xxxxxxx ------ Opcion no valida ------ xxxxxxx\n")
    else:
        match opcion:
            case 1:
                print("\n****** Ingrese Mascota ****** ")
                mascota = {}
                mascota['nombre'] = input("- Nombre de la mascota : ")
                mascota['dueno'] = input("- Dueno : ")
                mascota['genero'] = input("- Genero : ")
                mascota['tipo'] = int(input("1) Perro, 2) Gato, 3) Ave :"))

                if mascota['tipo'] == 1:
                    perro = Perro(mascota['nombre'], mascota['dueno'], mascota['genero'])
                    lista_mascotas.append(perro)
                elif mascota['tipo'] == 2:
                    gato = Gato(mascota['nombre'], mascota['dueno'], mascota['genero'])
                    lista_mascotas.append(gato)
                elif mascota['tipo'] == 3:
                    mascota['vuela'] = input("- Vuela : ")
                    ave = Ave(mascota['nombre'], mascota['dueno'], mascota['genero'], mascota['vuela'] )
                    lista_mascotas.append(ave)
                else:
                    print("xxxxxxx ------ Opcion no valida ------ xxxxxxx\n")
            case 2:
                print("\n****** Mostrar Mascotas ****** ")
                contador = 1

                for mascota in lista_mascotas:
                    print(mascota)
                    contador += 1
            case 3:
                print("Hasta la proxima.")
                seguir = False
            case default:
                print("xxxxxxx ------ Opcion no valida ------ xxxxxxx\n")
          
        