import csv
from texttable import Texttable

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
years = []
datos = []

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
def ReadDatos():
    with open('DBmetodosTest.csv', 'r') as f:
        reader = csv.reader(f)
        listaGruesa = list(reader)
        listaGruesa.pop(0)
        for i in listaGruesa:
            i[1] = float(i[1])
            date = i[0]
            month = date[0:date.index('/')]
            date = date[date.index('/')+1:]
            day = date[0:date.index('/')]
            year = date[date.index('/')+1:]
            datos.append(i + [int(day)] + [int(month)] + [int(year)])
            if year not in years:
                years.append(year)

    return listaGruesa

def GetDatos():

    return datos


def GetAmount(date):

    return [x for x in datos if (x[0] == date)]

def addYears(year):
    years.append(year)