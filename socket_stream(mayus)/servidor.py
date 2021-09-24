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


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
serversocket.bind((host, port))
serversocket.listen(5)
print("Esperando conexiones")
clientsocket, addr = serversocket.accept()

while True:
    data = clientsocket.recv(1024)
    print("Address: %s " % str(addr))
    print("Recibido: "+data.decode("ascii").upper())

