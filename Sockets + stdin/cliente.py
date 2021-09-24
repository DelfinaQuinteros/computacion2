#!/usr/bin/python3
import getopt
import socket
from sys import argv, exit


def get_Op():
    try:
        (opcion, args) = getopt.getopt(argv[1:], 'a:t:p', [])
        return opcion
    except getopt.GetoptError as error:
        print("Error:", str(error))
        exit()


def socketStructure(host, port, protocol):
    host = host
    protocol = protocol
    port = port
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


def main():
    options = get_Op()
    for (opts, args) in options:
        if opts == '-p':
            port = args
        if opts == '-t':
            protocol = args
        if opts == '-a':
            host = args

    socketStructure(host, port, protocol)


main()
