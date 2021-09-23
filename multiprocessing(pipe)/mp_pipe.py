import multiprocessing as mp
import os
import signal
import sys


def reader(r):
    print("Leyendo, presione Ctrl+D para salir")
    sys.stdin = open(0)
    while True:
        msg = input()
        r.send(msg)


def PIPE_reader(w):
    while True:
        msg = w.recv()
        print('Leyendo (pid: %d): %s' % (os.getpid(), msg))


def main():
    a, b = mp.Pipe()
    proceso1 = mp.Process(target=reader, args=(a,))
    proceso2 = mp.Process(target=PIPE_reader, args=(b,))
    proceso1.start()
    proceso2.start()
    proceso2.join()
    os.kill(proceso2.pid, signal.SIGTERM)


if __name__ == '__main__':
    main()
