from easygui import *
import sys
from Main import *

#Ventana Inicial
msgbox("                                   Proyecto #1\n"
       "Integrantes\n"
       "       Julio Barahona       141206\n"
       "       Josue Jacobs         15041\n"
       "       Jorgue Suchite       15293\n"
       "       Gerson Samayoa       15337\n"
       "       Kevin Sanchez?       ??????",'Metodos Numericos','Continuar')



msg ="Seleccione la opcion que desea ejecutar \n Selecicones <cancel> para finalizar."
title = "Menu principal"
choices = ["Analizar dia", "Agregar Año", ]
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    elif choice == 'Analizar dia':
        print('dia')
    elif choice == "Agregar Año":
        print('año')

        msgbox("You chose: {}".format(choice), "Add year")