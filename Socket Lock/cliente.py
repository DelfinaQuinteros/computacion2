#!/usr/bin/python3
import socket
import sys
import getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:c:n', [])
for (op, ar) in opt:
    if op in '-h':
        host = ar
    elif op == '-p':
        port = int(ar)
    elif op == '-c':
        letra = str(ar)
    elif op == '-n':
        num = ar
    else:
        print("Opcion invalida")
        sys.exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit(2)
s.connect((host, port))


if __name__ == '__main__':
    letra = letra.encode('utf-8')
    s.send(letra)
    num = num.encode('utf-8')
    s.send(num)
