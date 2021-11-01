#!/usr/bin/python3
import threading
import getopt
import socket
import sys
import time

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:')
for (op, ar) in opt:
    if op == '-p':
        port = ar
    if op == '-f':
        file_name = ar

ss = socket.socket(socket.AF_INET)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "127.0.0.1"
ss.bind((host, int(port)))
ss.listen()


def main(clientesocket):
    letra = clientesocket.recv(1024).decode('utf-8')
    num = clientesocket.recv(1024).decode('utf-8')
    lock.acquire()
    archivo = open(file_name, "w")
    for i in range(num):
        archivo.write(letra[num])
        archivo.flush()
        print(letra[num])
        time.sleep(1)
    lock.release()


if __name__ == "__main__":
    lock = threading.Lock()

    while True:
        print("----------Server listening----------")
        clientesocket, addr = ss.accept()
        print("Conexion de %s" % str(addr))
        s = threading.Thread(target=main, args=(clientesocket,))
