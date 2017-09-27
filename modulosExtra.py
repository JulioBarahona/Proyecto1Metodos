import csv
from texttable import Texttable

days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
daysName = ['Lunes', 'Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
monthDays =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diaFestivo = [0,[1],0,0,[13,14,15],[1],[30],0,[15],[15],[20],[1],[24,25]]
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