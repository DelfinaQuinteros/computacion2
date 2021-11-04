#!/usr/bin/python3
import asyncio
import subprocess


async def servidor(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Cliente conectado: {addr}")
    data = await reader.read(10)
    message = data.decode('ascii')
    if data.decode('ascii') == 'exit':
        writer.write('Terminado'.encode('ascii'))
        writer.close()
    print("Direccion: %s" % str(addr))
    print("Recibido correctamente:" + data.decode('ascii'))
    resultado = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = resultado.communicate()
    if stdout != "":
        message = "OK\n" + stdout
    elif stderr != "":
        message = "ERROR\n" + stderr
        writer.write(message.encode("ascii"))
    await writer.drain()


async def main():
    server = await asyncio.start_server(
        servidor, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    print("------------------servidor escuchando------------------")
    asyncio.run(main())

