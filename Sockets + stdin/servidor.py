#!/usr/bin/python3
import getopt
import socket
import sys


def main():
    def get_op():
        try:
            (opcion, arg) = getopt.getopt(sys.argv[1:], "p:t:f")
            return opcion
        except getopt.GetoptError as error:
            print("Error: ", str(error))
            exit()

    opciones = get_op()
    for (opcion, arg) in opciones:
        if opcion == '-p':
            port = int(arg)
        if opcion == '-t':
            protocol = str(arg)
        if opcion == '-f':
            pathfile = arg

    def socket_structure(port, protocol, pathfile):
        port = port
        protocol = protocol
        file = pathfile
        if protocol == 'tcp' or protocol == 'TCP':
            print("Protocolo TCP seleccionado")
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = ""
            ss.bind((host, port))
            ss.listen(5)
            print("-----Server listening-----")
            clientesocket, addr = ss.accept()
            while True:
                f = open(file, "a")
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
                f = open(file, "a")
                d, addr = ss.recvfrom(1024)
                f.write(d.decode("ascii") + "\n")
                address = addr[0]
                port = addr[1]
                if d == "" or len(d) == 0:
                    print("Saliendo")
                    break
                print("Direccion: %s - Port %d" % (address, port))
                print("Recibido correctamente:" + d.decode('ascii'))

        else:
            print("No se ha podido reconocer el protocolo, por favor ingrese 'UDP' o 'TCP'")

            socket_structure(port, protocol, pathfile)


main()
