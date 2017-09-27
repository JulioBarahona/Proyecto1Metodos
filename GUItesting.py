from easygui import *
import sys
import pylab
import numpy
from funcionesAnalisis import *
from Predicciones import *
from FuncionesGUI import *

ReadDatos()
'''
#Ventana Inicial presenta integrantes
msgbox("                                   Proyecto #1\n"
       "Integrantes\n"
       "       Julio Barahona       141206\n"
       "       Josue Jacobs         15041\n"
       "       Jorgue Suchite       15293\n"
       "       Gerson Samayoa       15337\n"
       "       Kevin Sanchez?       ??????",'Metodos Numericos','Continuar')
'''
#menu principal
msg ="Seleccione la opcion que desea ejecutar \n Selecicones <cancel> para finalizar."
title = "Menu principal"
choices = ["Analizar dia"]

#opciones a ingresar
while 1:

    #salida
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)

    #cuadro desplegado apara analizar dia
    elif choice == 'Analizar dia':

        msg = "Ingrese el mes y el año que desea predecir"
        title = "New Prediction "
        fieldNames = ["Mes", "Año"]
        fieldValues = multenterbox(msg, title, fieldNames)

        x = Prediction(int(fieldValues[0]), int(fieldValues[1]))
        printValuesPrediction(x)


