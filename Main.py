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
#GetFechaName("Lunes",2)
#GetMonth(11,2014)
#GetDay(24,12)
#DatoParecido("7/15/2014")

#SingularDayPrediction(30,3,2015)

#print(FuncionesPrueba.SingularDayPrediction(15,3, 2015))

x = Prediction(3,2015)
#SimilarDate()
#nigga