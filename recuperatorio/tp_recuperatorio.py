from rojo import Rojo
from verde import Verde
from azul import Azul
from PIL import Image

if __name__ == '__main__':
    op = int(input("""
    [1] Para ver la imagen roja
    [2] Para ver la imagen verde
    [3] Para ver la imagen azul
    [4] Para ver la imagen unida
    [5] Para salir
    :
    """))
    ruta = input("ingrese la ruta de la imagen:")
    if op == 1:
        Rojo().rojo(ruta)
    elif op == 2:
        Verde().verde(ruta)
    elif op == 3:
        Azul().azul(ruta)
    elif op == 4:
        red = Image.open(ruta+'rojo.ppm').convert('L')
        blue = Image.open(ruta+'azul.ppm').convert('L')
        green = Image.open(ruta+'verde.ppm').convert('L')
        merged = Image.merge("RGB", (red, green, blue)).rotate(90).show()
    elif op == 5:
        exit()
    else:
        print("Ingrese una opcion valida")
