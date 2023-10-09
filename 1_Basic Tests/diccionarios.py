""" crear un dict con la siguiente tabla 
    SISTEMAS    CIVIL      MATEMATICAS
    PROGRA2     SUELOS        MM110
    ALGO        DIBUJO        MM111
    POO         CARGAS        CALCULO
"""

tabla = [
        {"carrera" : "SISTEMAS",
        "clases" : ['PROGRA2', 'ALGO', 'POO']},
        {"carrera" : "CIVIL",
        "clases" : ['SUELOS', 'DIBUJO', 'CARGAS']},
        {"carrera" : "MATEMATICAS",
        "clases" :  ['MM110', 'MM111', 'CALCULO']}
]

print(tabla)

for carrera in tabla:
    print ("Estan son las clases de de la carrera" + carrera['carrera'])
    for clase in carrera['clases']:
        print(f"clase : {clase}")