#!/usr/bin/python3
import datetime
import getopt
import socket
import sys
import asyncio


async def main():
    (opcion, arg) = getopt.getopt(sys.argv[1:], "l:")
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    except socket.error:
        print("No se ha podido crear el socket")
        sys.exit()
    print("----------Comando prompt----------")
    comando = ""

    while comando != 'exit':
        comando = input("Comando:")
        msg = comando
        writer.write(msg.encode('ascii'))
        await writer.drain()
        data = await reader.read(10)
        print(f'Received: {data.decode()!r}')
        await writer.wait_closed()

        for (opt, arg) in opcion:
            if opt == "-l":
                file_path = arg
                file = open(str(file_path), "a")
                datetime_today = datetime.datetime.today()
                file.writelines("\n" + str(datetime_today) + "\n" + msg.decode('ascii'))
                file.close()

    exit()


asyncio.run(main())
