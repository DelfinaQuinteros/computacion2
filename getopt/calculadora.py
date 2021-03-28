#!/usr/bin/python3
import sys
import getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

print("opciones: ", opt)

for (op, ar) in opt:
    if op in '-o':
        print("Opcion -o seteada: ", ar)
        operador = ar
    elif op == '-n':
        print("Opcion -n seteada: ", ar)
        num1 = ar
    elif op == '-m':
        print("Opcion -m seteada: ", ar)
        num2 = ar
    else:
        print("Opcion invalida")




