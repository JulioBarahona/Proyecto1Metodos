from modulosExtra import *
from easygui import *

def printValuesPrediction(list):
    if len(list) == 28:
        # Ventana que presenta valores y su rango
        msgbox("                                   Resultados #1\n"
               "       Esperado                Rango\n"
               "1      "+str(list[0][0])+"       "+str(list[0][1])+'\n'
               "2      "+str(list[1][0])+"       "+str(list[1][1])+'\n'
               "3      "+str(list[2][0])+"       "+ str(list[2][1])+'\n'
               "4      "+str(list[3][0])+"       "+ str(list[3][1])+'\n'
               "5      "+str(list[4][0])+"       "+ str(list[4][1])+'\n'
               "6      "+str(list[5][0])+"       "+ str(list[5][1])+'\n'
               "7      "+str(list[6][0])+"       "+ str(list[6][1])+'\n'
               "8      "+str(list[7][0])+"       "+ str(list[7][1])+'\n'
               "9      "+str(list[8][0])+"       "+ str(list[8][1])+'\n'
               "10     "+str(list[9][0])+"       "+ str(list[9][1])+'\n'
               "11     "+str(list[10][0])+"       "+ str(list[10][1])+'\n'
               "12     "+str(list[11][0])+"       "+ str(list[11][1])+'\n'
               "13     "+str(list[12][0])+"       "+ str(list[12][1])+'\n'
               "14     "+str(list[13][0])+"       "+ str(list[13][1])+'\n'
               "15     "+str(list[14][0])+"       "+ str(list[14][1])+'\n'
               "16     "+str(list[15][0])+"       "+ str(list[15][1])+'\n'
               "17     "+str(list[16][0])+"       "+ str(list[16][1])+'\n'
               "18     "+str(list[17][0])+"       "+ str(list[17][1])+'\n'
               "19     "+str(list[18][0])+"       "+ str(list[18][1])+'\n'
               "20     "+str(list[19][0])+"       "+ str(list[19][1])+'\n'
               "21     "+str(list[20][0])+"       "+ str(list[20][1])+'\n'
               "22     "+str(list[21][0])+"       "+ str(list[21][1])+'\n'
               "23     "+str(list[22][0])+"       "+ str(list[22][1])+'\n'
               "24     "+str(list[23][0])+"       "+ str(list[23][1])+'\n'
               "25     "+str(list[24][0])+"       "+ str(list[24][1])+'\n'
               "26     "+str(list[25][0])+"       "+ str(list[25][1])+'\n'
               "27     "+str(list[26][0])+"       "+ str(list[26][1])+'\n'
               "27     "+str(list[27][0])+"       "+ str(list[27][1])+'\n'
          , 'Metodos Numericos', 'Continuar')
    elif len(list) == 29:
        # Ventana que presenta valores y su rango
        msgbox("                                   Resultados #1\n"
               "       Esperado                Rango\n"
               "1      "+str(list[0][0])+"       "+str(list[0][1])+'\n'
               "2      "+str(list[1][0])+"       "+str(list[1][1])+'\n'
               "3      "+str(list[2][0])+"       "+ str(list[2][1])+'\n'
               "4      "+str(list[3][0])+"       "+ str(list[3][1])+'\n'
               "5      "+str(list[4][0])+"       "+ str(list[4][1])+'\n'
               "6      "+str(list[5][0])+"       "+ str(list[5][1])+'\n'
               "7      "+str(list[6][0])+"       "+ str(list[6][1])+'\n'
               "8      "+str(list[7][0])+"       "+ str(list[7][1])+'\n'
               "9      "+str(list[8][0])+"       "+ str(list[8][1])+'\n'
               "10     "+str(list[9][0])+"       "+ str(list[9][1])+'\n'
               "11     "+str(list[10][0])+"       "+ str(list[10][1])+'\n'
               "12     "+str(list[11][0])+"       "+ str(list[11][1])+'\n'
               "13     "+str(list[12][0])+"       "+ str(list[12][1])+'\n'
               "14     "+str(list[13][0])+"       "+ str(list[13][1])+'\n'
               "15     "+str(list[14][0])+"       "+ str(list[14][1])+'\n'
               "16     "+str(list[15][0])+"       "+ str(list[15][1])+'\n'
               "17     "+str(list[16][0])+"       "+ str(list[16][1])+'\n'
               "18     "+str(list[17][0])+"       "+ str(list[17][1])+'\n'
               "19     "+str(list[18][0])+"       "+ str(list[18][1])+'\n'
               "20     "+str(list[19][0])+"       "+ str(list[19][1])+'\n'
               "21     "+str(list[20][0])+"       "+ str(list[20][1])+'\n'
               "22     "+str(list[21][0])+"       "+ str(list[21][1])+'\n'
               "23     "+str(list[22][0])+"       "+ str(list[22][1])+'\n'
               "24     "+str(list[23][0])+"       "+ str(list[23][1])+'\n'
               "25     "+str(list[24][0])+"       "+ str(list[24][1])+'\n'
               "26     "+str(list[25][0])+"       "+ str(list[25][1])+'\n'
               "27     "+str(list[26][0])+"       "+ str(list[26][1])+'\n'
               "28     "+str(list[27][0])+"       "+ str(list[27][1])+'\n'
               "29     "+str(list[28][0])+"       "+ str(list[28][1])+'\n'
          , 'Metodos Numericos', 'Continuar')
    elif len(list) == 30:
        # Ventana que presenta valores y su rango
        msgbox("                                   Resultados #1\n"
               "       Esperado                Rango\n"
               "1      "+str(list[0][0])+"       "+str(list[0][1])+'\n'
               "2      "+str(list[1][0])+"       "+str(list[1][1])+'\n'
               "3      "+str(list[2][0])+"       "+ str(list[2][1])+'\n'
               "4      "+str(list[3][0])+"       "+ str(list[3][1])+'\n'
               "5      "+str(list[4][0])+"       "+ str(list[4][1])+'\n'
               "6      "+str(list[5][0])+"       "+ str(list[5][1])+'\n'
               "7      "+str(list[6][0])+"       "+ str(list[6][1])+'\n'
               "8      "+str(list[7][0])+"       "+ str(list[7][1])+'\n'
               "9      "+str(list[8][0])+"       "+ str(list[8][1])+'\n'
               "10     "+str(list[9][0])+"       "+ str(list[9][1])+'\n'
               "11     "+str(list[10][0])+"       "+ str(list[10][1])+'\n'
               "12     "+str(list[11][0])+"       "+ str(list[11][1])+'\n'
               "13     "+str(list[12][0])+"       "+ str(list[12][1])+'\n'
               "14     "+str(list[13][0])+"       "+ str(list[13][1])+'\n'
               "15     "+str(list[14][0])+"       "+ str(list[14][1])+'\n'
               "16     "+str(list[15][0])+"       "+ str(list[15][1])+'\n'
               "17     "+str(list[16][0])+"       "+ str(list[16][1])+'\n'
               "18     "+str(list[17][0])+"       "+ str(list[17][1])+'\n'
               "19     "+str(list[18][0])+"       "+ str(list[18][1])+'\n'
               "20     "+str(list[19][0])+"       "+ str(list[19][1])+'\n'
               "21     "+str(list[20][0])+"       "+ str(list[20][1])+'\n'
               "22     "+str(list[21][0])+"       "+ str(list[21][1])+'\n'
               "23     "+str(list[22][0])+"       "+ str(list[22][1])+'\n'
               "24     "+str(list[23][0])+"       "+ str(list[23][1])+'\n'
               "25     "+str(list[24][0])+"       "+ str(list[24][1])+'\n'
               "26     "+str(list[25][0])+"       "+ str(list[25][1])+'\n'
               "27     "+str(list[26][0])+"       "+ str(list[26][1])+'\n'
               "28     "+str(list[27][0])+"       "+ str(list[27][1])+'\n'
               "29     "+str(list[28][0])+"       "+ str(list[28][1])+'\n'
               "20     "+str(list[29][0])+"       "+ str(list[29][1])+'\n'
          , 'Metodos Numericos', 'Continuar')
    elif len(list) == 31:
        # Ventana que presenta valores y su rango
        msgbox("                                   Resultados #1\n"
               "       Esperado                Rango\n"
               "1      "+str(list[0][0])+"       "+str(list[0][1])+'\n'
               "2      "+str(list[1][0])+"       "+str(list[1][1])+'\n'
               "3      "+str(list[2][0])+"       "+ str(list[2][1])+'\n'
               "4      "+str(list[3][0])+"       "+ str(list[3][1])+'\n'
               "5      "+str(list[4][0])+"       "+ str(list[4][1])+'\n'
               "6      "+str(list[5][0])+"       "+ str(list[5][1])+'\n'
               "7      "+str(list[6][0])+"       "+ str(list[6][1])+'\n'
               "8      "+str(list[7][0])+"       "+ str(list[7][1])+'\n'
               "9      "+str(list[8][0])+"       "+ str(list[8][1])+'\n'
               "10     "+str(list[9][0])+"       "+ str(list[9][1])+'\n'
               "11     "+str(list[10][0])+"       "+ str(list[10][1])+'\n'
               "12     "+str(list[11][0])+"       "+ str(list[11][1])+'\n'
               "13     "+str(list[12][0])+"       "+ str(list[12][1])+'\n'
               "14     "+str(list[13][0])+"       "+ str(list[13][1])+'\n'
               "15     "+str(list[14][0])+"       "+ str(list[14][1])+'\n'
               "16     "+str(list[15][0])+"       "+ str(list[15][1])+'\n'
               "17     "+str(list[16][0])+"       "+ str(list[16][1])+'\n'
               "18     "+str(list[17][0])+"       "+ str(list[17][1])+'\n'
               "19     "+str(list[18][0])+"       "+ str(list[18][1])+'\n'
               "20     "+str(list[19][0])+"       "+ str(list[19][1])+'\n'
               "21     "+str(list[20][0])+"       "+ str(list[20][1])+'\n'
               "22     "+str(list[21][0])+"       "+ str(list[21][1])+'\n'
               "23     "+str(list[22][0])+"       "+ str(list[22][1])+'\n'
               "24     "+str(list[23][0])+"       "+ str(list[23][1])+'\n'
               "25     "+str(list[24][0])+"       "+ str(list[24][1])+'\n'
               "26     "+str(list[25][0])+"       "+ str(list[25][1])+'\n'
               "27     "+str(list[26][0])+"       "+ str(list[26][1])+'\n'
               "28     "+str(list[27][0])+"       "+ str(list[27][1])+'\n'
               "29     "+str(list[28][0])+"       "+ str(list[28][1])+'\n'
               "30     "+str(list[29][0])+"       "+ str(list[29][1])+'\n'
               "31     "+str(list[30][0])+"       "+ str(list[30][1])+'\n'
          , 'Metodos Numericos', 'Continuar')