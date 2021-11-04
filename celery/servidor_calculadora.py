#!/usr/bin/python3
import getopt
import multiprocessing as mp
import socket
import sys
import tasks


def child():
    pass


if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')
    for (op, ar) in opt:
        if op == '-h':
            host = ar
        if op == '-p':
            port = int(ar)
        else:
            print("Opcion invalida")
            sys.exit(1)
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit(2)

    ss.bind((host, port))
    ss.listen(5)
    print("----------Server listening----------")
    while True:
        cliente = ss.accept()
        clientesocket, addr = cliente
        print(f"Se realizo una nueva conneccion con: {addr}")
        p1 = mp.Process(target=child, args=(cliente,))
        p1.start()
