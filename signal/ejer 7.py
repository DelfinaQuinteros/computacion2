#!/usr/bin/python
import getopt
import os
import signal
import sys
import time


def handlerUSR2(signal, frame):
    print("Soy el PID: ", os.getpid(), "recibí la señal: ", signal, "de mi padre PID: ", os.getppid())


def main():
    (opts, args) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

    if len(opts) != 1:
        print("no se ingreso la cantidad de parametros y argumentos correctos")
        exit()

    for opt, value in opts:
        if opt == "-p" or opt == "--process":
            num_hijos = int(value)
            for x in range(num_hijos):
                pid1 = os.fork()
                if pid1:
                    time.sleep(1)
                    print("Creando proceso: ", pid1, "\n\n")
                    send_signal(pid1)
                    os.wait()
                    print("TERMINADO")
                else:
                    signal.signal(signal.SIGUSR2, handlerUSR2)
                    signal.pause()
                    exit(0)


def send_signal(pid):
    pid = int(pid)
    os.kill(pid, signal.SIGUSR2)


if __name__ == '__main__':
    main()