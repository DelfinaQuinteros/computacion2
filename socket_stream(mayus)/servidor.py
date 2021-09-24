#!/usr/bin/python3
import getopt
import socket
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], "p:")
for (op, ar) in opt:
    if op == '-p':
        port = int(ar)
    else:
        print("Opcion invalida")


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
ss.bind((host, port))
ss.listen(5)
print("Esperando conexiones")
clientsocket, addr = ss.accept()

data = clientsocket.recv(1024)
clientsocket.close()
print("Address: %s " % str(addr))
print("Recibido: "+data.decode("utf8").upper())

