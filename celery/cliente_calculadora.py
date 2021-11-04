"""
-h ip_server
-p port
-o "operacion" (suma, resta, mult, div, pot)
-n ## (primer operando)
-m ## (segundo operando)
"""
import getopt
import multiprocessing as mp
import socket
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:o:n:m:')
for (op, ar) in opt:
    if op == '-h':
        host = ar
    if op == '-p':
        port = int(ar)
    if op == '-o':
        operacion = ar
    if op == '-n':
        num1 = int(ar)
    if op == '-m':
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
