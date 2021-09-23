import subprocess, socket, getopt, sys
import multiprocessing as mp

#ss = serversocket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
host = ""
port = int(sys.argv[1])
ss.bind((host, port))
ss.listen(5)
print("----------Server listening----------")
clientesocket, addr = ss.accept()

while True:
    data = clientesocket.recv(1024)
    msg = data.decode("utf-8")
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

    clientesocket.send(msg.encode("utf-8"))

