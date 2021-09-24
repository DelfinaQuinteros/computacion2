import threading
from getopt import getopt
from sys import argv
import sys
import time
try:
    (opt, arg) = getopt(argv[1:], 'n:f:r:')
except getopt.GetoptError as error:
    print(error)
    sys.exit(1)


for args in opt:
    if args[0] == '-n':
        hilos = int(args[1])
    elif args[0] == '-f':
        file_name = args[1]
    elif args[0] == '-r':
        iteraciones = int(args[1])
    else:
        sys.exit(2)

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l_hilos = []


def main(lock, iteraciones, num):
    lock.acquire()
    for i in range(iteraciones):
        archivo.write(abecedario[num])
        archivo.flush()
        print(abecedario[num])
        time.sleep(1)
    lock.release()


lock = threading.Lock()
archivo = open(file_name, "w")
for num in range(hilos):
    l_hilos.append(threading.Thread(target=main, args=(lock, iteraciones, num)))
    l_hilos[-1].start()
for l in l_hilos:
    l.join()
archivo.close()

main()
