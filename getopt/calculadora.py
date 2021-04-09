#!/usr/bin/python3
import sys
import getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

<<<<<<< HEAD
=======

>>>>>>> f8474ff64bb1c0cfabff03b9b09480cfb6d825d8
for (op, ar) in opt:
    if op in '-o':
        operador = ar
    elif op == '-n':
        num1 = ar
    elif op == '-m':
        num2 = ar
    else:
        print("Opcion invalida")

<<<<<<< HEAD

=======
>>>>>>> f8474ff64bb1c0cfabff03b9b09480cfb6d825d8
if operador == '+':
    print("El resultado de la suma de:", num1, "+", num2, "es:", int(num1) + int(num2))
elif operador == '-':
    print("El resultado de la resta de:", num1, "-", num2, "es:", int(num1) - int(num2))
elif operador == '*':
    print("El resultado de la multiplicacion de:", num1, "*", num2, "es:", int(num1) * int(num2))
elif operador == '/':
    print("El resultado de la division de:", num1, "/", num2, "es:", int(num1) / int(num2))
else:
<<<<<<< HEAD
    print("Ingrese una opcion valida")
=======
    print("Ingrese una opcion valida")


>>>>>>> f8474ff64bb1c0cfabff03b9b09480cfb6d825d8
