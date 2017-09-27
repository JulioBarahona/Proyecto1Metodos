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
choices = ["Analizar dia", "Agregar Año", "Mes" ]

#opciones a ingresar
while 1:

    #salida
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)

    #cuadro desplegado apara analizar dia
    elif choice == 'Analizar dia':

        msg = "Enter your personal information"
        title = "Credit Card Application"
        fieldNames = ["Mes","Año"]
        fieldValues = multenterbox(msg, title, fieldNames)
        if fieldValues is None:
            sys.exit(0)
        while 1:
            errmsg = ""
            for i, name in enumerate(fieldNames):
                if (fieldValues[i].strip() == "" and not((fieldValues[i].strip() in months)) and not ((fieldValues[i].strip() in years))):
                    errmsg += "{} no valido.\n\n".format(name)
            if errmsg == "":
                break  # no problems found
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
            if fieldValues is None:
                break

    #cuadro desplegado para agregar año
    elif choice == "Agregar Año":
        msg = "Ingrese el año que desea agregar"
        title = "Agregar un nuevo año de ingresos"
        fieldNames = ["Año"]
        fieldValues = integerbox(msg, title,201, 2016,10000000)
        addYears(fieldValues)
