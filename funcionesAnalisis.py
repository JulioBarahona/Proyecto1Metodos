from PIL import Image, ImageDraw
from modulosExtra import *

def todosLosDomingos():
    datosOriginales = GetDatos()
    datosNuevos = []

    for i in range(len(datosOriginales)):
        if datosOriginales[i][2] == "Domingo":
            datosNuevos.append(datosOriginales[i][1])

    img = Image.open('blank.png')
    draw_img = ImageDraw.Draw(img)
    x = 0

    print(datosNuevos)


    for i in datosNuevos:
        x = x + 30
        print(max(datosNuevos))
        print(max(datosNuevos) + 500)
        y = (max(datosNuevos) + 500 ) - float(i)
        draw_img.line((x, 200, x, y), width=10, fill=(0, 0, 255, 0))

    img.show()

    return datosNuevos


def DatoParecido(info):
    datosOriginales = GetDatos()
    res = []

    try:
        amount = int(info)
    except:
        amount = GetAmount(info)[0]
        print(amount)
        amount = float(amount[1])


    for i in datosOriginales:
        if (i[1] > (amount - 10000) and i[1] < (amount + 10000)):
            res.append(i[1])
            print(i)

    return res

def GetFecha(day, month):
    originalData = GetDatos()

    year = originalData[0][5]
    temp = 0
    mean = []
    for i in originalData:
        if (i[3] >= day and i[3] <= day +7 and i[4] == month):
            if (i[5] == year):
                temp = (temp + i[1])/2
            else:
                print(temp)
                temp =  0
                year = i[5]

    print(temp)

def GetFinDeMes(day):
    originalData = GetDatos()

    print(day)
    year = originalData[0][5]
    temp = 0
    for i in originalData:
        if (i[3] == day):
            #print(i)
            if (i[5] == year):
                if (i[1] > 0):
                    temp = (temp + i[1])/2
            else:
                print(temp)
                temp =  0
                year = i[5]

    print(temp)


#Funcion para obtener datos que comparten dia y fecha
def GetFechaName(info, day):
    originalData = GetDatos()

    year = originalData[0][5]
    temp = 0
    for i in originalData:
        if (i[2] == info and i[1] > 0 and i[3] ==day):
            print(i)
            if (i[5] == year):
                temp = (temp + i[1])/2
            else:
                print(temp)
                temp =  0
                year = i[5]

    print(temp)

#Funcion para obtener los datos de un mes especifico
def GetMonth(month, year):
    originalData = GetDatos()

    for i in originalData:
        if (i[4] == month and i[5] ==  year):
            print(i[1])

def GetDay(day, month):
    orinalData = GetDatos()

    for i in orinalData:
        if (i[3] == day and i[4] == month):
            print(i)



