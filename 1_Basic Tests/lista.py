lista = []

for item in range(0,8):
    lista.append(item + 1)

for item in lista :
    print(item)

lista.reverse()

print(lista)

print(len(lista))

busqueda = int(input("ingrese numero a buscar : "))

if lista.index(busqueda):
    print("valor encontrado")

