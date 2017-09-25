import csv
from texttable import Texttable

month = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# imprime los nomrbes de los integrantes de manera ordenada
def imprimirIntegrantes():
    integrantes = [['Nombre', 'Carnet'], ['Julio Barahona', '141206'],['Josue Jacobs','15041'], ['Jorge Suchite','15293'] , ['Gerson Samayoa','15337']]
    t = Texttable()
    t.add_rows(integrantes)
    print(t.draw())


# jala los datos y pregutna si se desa imprimirlos ante el usuario
def imprimirDatos():

    with open('DBmetodos.csv', 'r') as f:
        reader = csv.reader(f)
        listaGruesa = list(reader)

    for i in range(1,len(listaGruesa),1):
        listaGruesa[i][1] = float(listaGruesa[i][1])

    print('Desea imprimir los datos leido? (Y/N)')

    flag = input()
    while (flag != 'Y' and flag != 'N'):
            print('ingrese solamente Y o N... ')
            flag = input()


    if (flag == 'Y'):
        t = Texttable()
        t.add_rows(listaGruesa)
        print(t.draw())

#combierte los datos a una lista, eliminando tambien los titulos
def getDatos():
    with open('DBmetodos.csv', 'r') as f:
        reader = csv.reader(f)
        l = []
        listaGruesa = list(reader)
        listaGruesa.pop(0)
        for i in listaGruesa:
            try:
                l.append(i + [month[int(i[0][0:2]) - 1]] )
            except:
                l.append(i + [month[int(i[0][0:1]) - 1]])

        for i in range(0, len(listaGruesa), 1):
            listaGruesa[i][1] = float(listaGruesa[i][1])

    return listaGruesa