#!/usr/bin/python3
import socket
import sys
import getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:', [])
for (op, ar) in opt:
    if op in '-h':
        host = ar
    elif op == '-p':
        port = int(ar)
    else:
        print("Opcion invalida")
        sys.exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit(2)
s.connect((host, port))


def comando():
    if respuesta == '200':
        print("200: OK")
    elif respuesta == '400':
        print("400: Comando válido, pero fuera de secuencia.")
    elif respuesta == '500':
        print("500: Comando inválido.")
    elif respuesta == '404':
        print("404: Clave errónea.")
    elif respuesta == '405':
        print("405: Cadena nula.")


while True:
    msgin = input('Ingrese su nombre: ')
    msg = 'hello|' + msgin
    s.send(msg.encode('utf8'))
    respuesta = s.recv(1024).decode("utf8")
    comando()
    if respuesta == '200':
        while True:
            msgin = input('Ingrese el email: ')
            msg = 'email|' + msgin
            s.send(msg.encode('utf8'))
            respuesta = s.recv(1024).decode("utf8")
            comando()
            if respuesta == '200':
                while True:
                    msgin = input('Ingrese la key : ')
                    msg = 'key|' + msgin
                    s.send(msg.encode('utf8'))
                    respuesta = s.recv(1024).decode("utf8")
                    comando()
                    if respuesta == '200':
                        msg = 'exit'
                        s.close()
