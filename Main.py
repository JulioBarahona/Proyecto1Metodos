'''
Proyecto #1
Julio Barahona  ,   141206
Josue Jacobs    ,   15041
Jorge Suchite   ,   15293
Gerson Samayoa  ,   15337
'''

import pylab
import numpy
from funcionesAnalisis import *
from Predicciones import *
import Predicciones

print('+-------------------------+')
print('+       Proyecto #1       +')
print('+       Integrantes:      +')
imprimirIntegrantes()
#fA.imprimirDatos()

ReadDatos()
#print(GetDatos())

x = pylab.linspace(0,10,100)
y = numpy.sin(x)


#pylab.plot(x,y)
#pylab.show()

#GetFecha(31,7)
#GetFinDeMes(29)
#GetFinDeMes(30)
#GetFinDeMes(31)
GetFechaName("Lunes",2)
#DatoParecido("7/15/2014")

#print(FuncionesPrueba.SingularDayPrediction(15,3, 2015))

'''x = FuncionesPrueba.Prediction(3,2015)
for i in x:
    print(i)'''
#SimilarDate()
#nigga