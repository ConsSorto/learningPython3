texto = ""
seguir = True

while (seguir):
    texto = input("Ingresar texto para hacerlo mayusculas : ")
    
    if (not (len(texto) == 0 or texto == "" or texto == None or texto == "Parar")):
        print(texto.upper()+"\n")
    elif texto == "Parar":
        seguir = False
    


    