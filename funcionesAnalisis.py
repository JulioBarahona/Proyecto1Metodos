from modulosExtra import *

def todosLosDomingos():
    datosOriginales = getDatos()
    print len(datosOriginales)
    print datosOriginales

    for i in datosOriginales:
        if (i[2] != 'Domingo'):
            print 'el dato ' +  str(i) +  ' se elimina '
            datosOriginales.pop(datosOriginales.index(i))
        else:
            print 'el dato ' +  str(i) +  ' NO se elimina '


    print datosOriginales
    print len(datosOriginales)

todosLosDomingos()