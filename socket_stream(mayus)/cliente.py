#!/usr/bin/python3
import socket
import sys
import getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
for (op, ar) in opt:
    if op in '-a':
        host = ar
    elif op == '-p':
        port = ar
    else:
        print("Opcion invalida")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

sys.exit()
s.connect((host, port))

while 1:
    msg = input('Ingrese el mensaje: ')
    s.send(msg.encode('ascii'))
    msg = s.recv(1024)
    print('Server reply : ' + msg.decode("ascii"))

