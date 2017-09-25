from PIL import Image, ImageDraw
from modulosExtra import *

def todosLosDomingos():
    datosOriginales = getDatos()
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


def DatoParecido(amount):
    datosOriginales = getDatos()
    res = []

    for i in datosOriginales:
        if (i[1] > (amount - 1000) and i[1] < (amount + 1000)):
            res.append(i[1])
            print(i)

    return res

