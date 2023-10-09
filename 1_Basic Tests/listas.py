lista = []

valor = ""

while (valor != "Parar"):
    valor = input("Ingrese un valor para la lista : ")
    if (valor != "Parar" and len(valor) < 120):
        lista.append(valor)


for elemento in lista:
    print(str(lista.index(elemento) + 1) + " " + elemento)


    