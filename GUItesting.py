from easygui import *
import sys
from funcionesAnalisis import *

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

        print(int(fieldValues[0])+2)
        print((fieldValues[1])+2)
