from easygui import *
import sys
from Main import *

#Ventana Inicial presenta integrantes
msgbox("                                   Proyecto #1\n"
       "Integrantes\n"
       "       Julio Barahona       141206\n"
       "       Josue Jacobs         15041\n"
       "       Jorgue Suchite       15293\n"
       "       Gerson Samayoa       15337\n"
       "       Kevin Sanchez?       ??????",'Metodos Numericos','Continuar')

#menu principal
msg ="Seleccione la opcion que desea ejecutar \n Selecicones <cancel> para finalizar."
title = "Menu principal"
choices = ["Analizar dia", "Agregar Año", ]

#opciones a ingresar
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    elif choice == 'Analizar dia':
        
    elif choice == "Agregar Año":
        msg = "Ingrese el año que desea agregar"
        title = "Agregar un nuevo año de ingresos"
        fieldNames = ["Año"]
        fieldValues = integerbox(msg, title,201, 2015,10000000)
        addYears(fieldValues)
