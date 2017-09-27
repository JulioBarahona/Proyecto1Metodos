
from modulosExtra import *
import datetime
import math
import numpy


#Funcion para datos con el mismo numero de dia y que comparta mes.
def SimilarDateNumber(day, month, year):
    originalData = GetDatos()
    ans = []

    for i in originalData:
        if (i[4] > month - 2 and i[4] < month + 2 and i[3] == day):
            ans.append(i)

    return ans

#Funcion para obtener datos que compartan fecha y dia de la semana.
def SimilarDateName(day, month, year):
    originalData = GetDatos()
    dateT = datetime.datetime(int(year), int(month), int(day))
    weekDay = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    wd = weekDay[dateT.weekday()]
    ans = []

    for i in originalData:
        if (wd == "Domingo"):
            if (i[2] == wd and i[5] <= year):
                ans.append(i)
        else:
            if (i[2] == wd  and i[3] == day  and i[5] <= year):
                ans.append(i)

    return ans


#Funcion para realizar prediccion de un dia singular
def SingularDayPrediction(day, month, year):

    tempData = SimilarDateName(day, month, year)
    #print(tempData)
    yearMean = []
    count = []
    year = tempData[0][5]
    temp = tempData[0][1]
    cont = 0


    for i in tempData:
        if (i[5] == year):
            if (i[1] > 0):
                temp = (temp + i[1])/2
                cont += 1
        else:
            count.append(cont)
            yearMean.append(temp)
            cont =1
            temp = i[1]
            year = i[5]

    yearMean.append(temp)
    count.append(cont)

    total = (len(yearMean) + 1) * len(yearMean) / 2
    temp = 1
    res = 0

    for i in range(len(yearMean)):
        res = res + yearMean[i]*temp/total
        temp += 1

    desv = 0
    for i in yearMean:
        desv = desv + (res-i)**2

    desv = 1.645*math.sqrt(desv)/math.sqrt(len(yearMean))
    ans = [res, desv]
    return desv



#Funcion para predecir el mes
def Prediction(month, year):
    datosOriginales = GetDatos()
    res = []

    for i in range(monthDays[month]):
        res.append(SingularDayPrediction(i + 1, month, year))
        print(res[i])

    return res

