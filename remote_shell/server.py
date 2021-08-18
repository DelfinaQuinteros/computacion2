import subprocess, socket, getopt, sys

#ss = serversocket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
ss.bind((host, port))
ss.listen(5)
print("----------Server listening----------")
clientesocket, addr = ss.accept()

while True:
    data = clientesocket.recv(1024)
    if data.decode('ascii') == 'exit':
        clientesocket.send('Terminado'.encode('ascii'))
        break
    print("Direccion: %s" % str(addr))
    print("Recibido correctamente:" + data.decode('ascii'))
    resultado = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = resultado.communicate()
    if stdout != "":
        msg = "OK\n"+stdout
    elif stderr != "":
        msg = "ERROR\n"+stderr

    clientesocket.send(msg.encode())

