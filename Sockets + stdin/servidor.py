#!/usr/bin/python3
import getopt
import socket
import sys

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

for (op, ar) in opt:
    if op in ['-p']:
        port = int(ar)
    elif op in ['-t']:
        protocol = ar
    elif op in ['-f']:
        pathfile = ar
    else:
        sys.exit(2)

if protocol == 'tcp' or protocol == 'TCP':
    print("Protocolo TCP seleccionado")
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    ss.bind((host, port))
    ss.listen(5)
    print("-----Server listening-----")
    clientesocket, addr = ss.accept()

    while True:
        f = open(pathfile, "a")
        d = clientesocket.recv(1024)
        f.write(d.decode("ascii") + "\n")
        if d == "" or len(d) == 0:
            print("Saliendo")
            break
        print("Direccion: %s" % str(addr))
        print("Recibido correctamente:" + d.decode('ascii'))

elif protocol == 'udp' or protocol == 'UDP':
    print("Protocolo UDP seleccionado")
    ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = ""
    ss.bind((host, port))
    print("-----Server listening-----")

    while True:
        f = open(pathfile, "a")
        d, addr = ss.recvfrom(1024)
        msg = d.decode("ascii")
        f.write(msg + "\n")
        address = addr[0]
        port = addr[1]
        if d == "" or len(d) == 0:
            print("Exit")
            break
        print("Direccion: %s - Port %d" % (address, port))
        print("Recibido correctamente:" + d.decode('ascii'))

    else:
        print("No se ha podido reconocer el protocolo, por favor ingrese 'UDP' o 'TCP'")
else:
    sys.exit()
