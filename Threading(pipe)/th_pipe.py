import threading as th
import os
import sys


def reader(a):
    print("Hilo %s: Este es el hilo (%d)" % (th.current_thread().getName(), th.current_thread()._ident))
    a = os.fdopen(a, 'w')
    print("Leyendo, presione Ctrl+D para salir")
    print("Ingrese el texto:")
    sys.stdin = open(0)
    while True:
        try:
            msg = input() + "\n"
            a.write(msg)
            a.flush()
        except EOFError:
            print("saliendo")
            break


def PIPE_reader(b):
    hilo = th.current_thread()._ident
    b = os.fdopen(b, 'r')
    while True:
        linea = b.readline()
        if linea:
            print("Leyendo:", linea, "Del hilo:", hilo)
        else:
            break


def main():
    print("-----------------------------------")
    print("iniciando el programa")
    print("-----------------------------------")
    b, a = os.pipe()
    hilo1 = th.Thread(target=reader, args=(a,), daemon=True)
    hilo2 = th.Thread(target=PIPE_reader, args=(b,), daemon=True)
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()


if __name__ == '__main__':
    main()

