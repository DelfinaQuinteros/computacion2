import datetime, socket, getopt, sys


def main():
    (opcion, arg) = getopt.getopt(sys.argv[1:], "l:")
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("No se ha podido crear el socket")
        sys.exit()
    host = "0.0.0.0"
    port = 8000
    ss.connect((host, port))
    print("----------Comando prompt----------")
    comando = ""

    while comando != 'exit':
        comando = input("Comando:")
        msg = comando
        ss.send(msg.encode('ascii'))
        msg = ss.recv(1024)
        print("Respuesta del servidor: " + msg.decode())

        for (opt, arg) in opcion:
            if opt == "-l":
                file_path = arg
                file = open(str(file_path), "a")
                datetime_today = datetime.datetime.today()
                file.writelines("\n" + str(datetime_today) + "\n" + msg.decode())
                file.close()

    exit()


main()
