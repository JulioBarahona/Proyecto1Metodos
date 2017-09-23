import csv
from texttable import Texttable

# imprime los nomrbes de los integrantes de manera ordenada
def imprimirIntegrantes():
    integrantes = [['Nombre', 'Carnet'], ['Julio Barahona', '141206'],['Josue Jacobs','15041'], ['Jorge Suchite','15293'] , ['Gerson Samayoa','15337']]
    t = Texttable()
    t.add_rows(integrantes)
    print t.draw()


# jala los datos y pregutna si se desa imprimirlos ante el usuario
def imprimirDatos():

    with open('DBmetodos.csv', 'rb') as f:
        reader = csv.reader(f)
        listaGruesa = list(reader)

    print 'Desea imprimir los datos leido? (Y/N)'

    flag = raw_input()
    while (flag != 'Y' and flag != 'N'):
            print 'ingrese solamente Y o N... '
            flag = raw_input()


    if (flag == 'Y'):
        t = Texttable()
        t.add_rows(listaGruesa)
        print t.draw()

#combierte los datos a una lista, eliminando tambien los titulos
def getDatos():
    with open('DBmetodos.csv', 'rb') as f:
        reader = csv.reader(f)
        listaGruesa = list(reader)
        listaGruesa.pop(0)
    return listaGruesa