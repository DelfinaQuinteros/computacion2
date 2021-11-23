#!/usr/bin/python3
import array
import os


def azul(ruta):
    fd = os.open(ruta+".ppm", os.O_RDONLY)
    cabecera = os.read(fd, 15)
    cabecera_split = str(cabecera).split("\\n")
    p_image = cabecera_split[0][2] + cabecera_split[0][3]
    width = int(cabecera_split[1].split()[0])
    height = int(cabecera_split[1].split()[1])
    max_value = int(cabecera_split[2])
    # centerY, centerX = height//2, width//2

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"
    imorig = os.read(fd, width*height*3)

    image = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            image[index + 2] = imorig[index + 2]

    f = open(ruta+'azul.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)


# ruta = input("ingrese la ruta de la imagen")
azul('img/ppal-gatos')



"""
    imagen = cv2.imread('img/ppal-gatos.ppm')
    M = cv2.getRotationMatrix2D((width//2, height//2), -90, 1)
    img = cv2.warpAffine(imagen, M, (width, height))
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
        for i in range(image//2):
        for j in range(i, image-1-i):
            image[i][j], image[j][n - 1 - i], image[n - 1 - i][n - 1 - j], image[n - 1 - j][i] = \
                image[n - 1 - j][i], image[i][j], image[j][n - 1 - i], image[n - 1 - i][n - 1 - j]
"""