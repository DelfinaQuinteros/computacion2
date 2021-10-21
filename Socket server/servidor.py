#!/usr/bin/python3
import getopt
import threading
import socket
import subprocess
import socketserver
import os
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024)
            msg = data.decode("ascii")
            resultado = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = resultado.communicate()
            if stdout != "":
                msg = "OK\n" + stdout
            elif stderr != "":
                msg = "ERROR\n" + stderr


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def main():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'm:')
    for (op, ar) in opt:
        if op == ['m']:
            opcion = ar
        else:
            sys.exit(1)
    address = ('0.0.0.0', 8000)
    if opcion == 'p':
        server = ForkedTCPServer(address, MyTCPHandler)
        print("Server loop running in process:", os.getpid())
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente = ss.accept()
        ss.connect(address)
        sock, addr = cliente
    elif opcion == 't':
        server = ThreadedTCPServer(address, MyTCPHandler)
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente = ss.accept()
        th = threading.Thread(target=server.serve_forever, args=(cliente,))
        th.setDaemon(True)
        th.start()
        ss.connect(address)
        sock, addr = cliente
        print("Server loop running in thread:", th.getName())
    print("..............servidor escuchando.............")

    while True:
        msg = input("Ingrese un mensaje: ")
        ss.send(msg.encode('ascii'))
        data = ss.recv(1024).decode('ascii')
        print(data)
        if msg == 'exit':
            server.shutdown()
            ss.close()
            server.socket.close()


if __name__ == "__main__":
    main()
