#!/usr/bin/python3
import getopt
import multiprocessing as mp
import socket
import sys
from tasks import suma, resta, mult, div, pot


def child(cliente):
    con, addr = cliente
    print("addr", addr)
    data = con.recv(1024)
    print(f"Operador: {data[0]}, operando 1: {data[1]}, oerando 2: {data[2]},")
    operator = data[0]
    n = data[1]
    m = data[2]
    if operator == 'suma':
        res = suma.delay(n, m)
    elif operator == 'resta':
        res = resta.delay(n, m)
    elif operator == 'mult':
        res = mult.delay(n, m)
    elif operator == 'pot':
        res = pot.delay(n, m)
    elif operator == 'div':
        res = div.delay(n, m)

    response = res.get(timeout=10)
    print("Respuesta", response)
    con.send(response)
    con.close()


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
