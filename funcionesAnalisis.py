from modulosExtra import *

def todosLosDomingos():
    datosOriginales = getDatos()
    datosNuevos = []
    print len(datosOriginales)
    print datosOriginales


    for i in range(len(datosOriginales)):
        if datosOriginales[i][2] == "Domingo":
            datosNuevos.append(datosOriginales[i])

    print datosNuevos
todosLosDomingos()