#!/usr/bin/python3
import subprocess, socket
import asyncio
import socket

loop = asyncio.get_event_loop()


async def handle_client(cliente, addr):
    print(f"Cliente conectado: {addr}")
    while True:
        data = clientesocket.recv(1024)
        msg = data.decode("ascii")
        if data.decode('ascii') == 'exit':
            clientesocket.send('Terminado'.encode('ascii'))
            break
        print("Direccion: %s" % str(addr))
        print("Recibido correctamente:" + data.decode('ascii'))
        resultado = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = resultado.communicate()
        if stdout != "":
            msg = "OK\n" + stdout
        elif stderr != "":
            msg = "ERROR\n" + stderr

        clientesocket.send(msg.encode("ascii"))


if __name__ == "__main__":
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8000
    ss.bind((host, port))
    ss.listen(5)
    print("----------Server listening----------")

    while True:
        cliente = ss.accept()
        clientesocket, addr = cliente
