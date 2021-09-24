#!/usr/bin/python3
import socket
import sys
import getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:', [])
for (op, ar) in opt:
    if op in '-a':
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


msg = input('Ingrese una cadena de texto: ')
s.send(msg.encode('utf8'))
msg = s.recv(1024)
print('Server reply : ' + msg.decode("utf8"))
s.close()
