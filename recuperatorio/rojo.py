# !/usr/bin/python3
import array
import os
import cv2
import numpy as np

def rojo(ruta):
    fd = os.open(ruta + ".ppm", os.O_RDONLY)
    cabecera = os.read(fd, 16)
    cabecera_split = str(cabecera).split("\\n")

    p_image = cabecera_split[0][2] + cabecera_split[0][3]
    width = int(cabecera_split[1].split()[0])
    height = int(cabecera_split[1].split()[1])
    max_value = int(cabecera_split[2])

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"

    imorig = os.read(fd, width * height * 3)
    image = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            image[index + 0] = imorig[index + 0]

    f = open(ruta + 'rojo.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)


ruta = input("ingrese la ruta de la imagen")
rojo(f'{ruta}')
