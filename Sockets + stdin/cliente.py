#!/usr/bin/python3
import getopt
import socket
import sys
from sys import argv, exit

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:', [])
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for (op, ar) in opt:
    if op in ['-a']:
        host = ar
    elif op in ['-p']:
        port = int(ar)
    elif op in ['-t']:
        protocol = ar
    else:
        sys.exit(2)

if protocol == 'tcp' or protocol == 'TPC':
    print("Protocolo TCP seleccionado")
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("No se pudo crear el socket")
        exit()
    ss.connect((host, port))
    while True:
        try:
            msgin = input('Ingresar mensaje: ')
            ss.send(msgin.encode('ascii'))
            if msgin == 'exit' or msgin == 'EXIT':
                ss.close()
                break
        except EOFError:
            break
elif protocol == 'udp' or protocol == 'UDP':
    print("Protocolo UDP seleccionado")
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print('No se pudo crear el socket')
        exit()
    while True:
        msgin = input("Ingresar mensaje:").encode()
        ss.sendto(msgin, (host, port))
        if msgin.decode() == 'exit':
            ss.close()
            break
    else:
        print("No se ha podido reconocer el protocolo, por favor ingrese 'UDP' o 'TCP'")


