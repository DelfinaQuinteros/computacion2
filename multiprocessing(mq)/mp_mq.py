import multiprocessing as mp
import os
import time


def hijos(proc, q):
    print('Proceso %d, PID: %d' % (proc, os.getpid()))
    time.sleep(proc)
    q.put(str(os.getpid()) + "\t")


def main():
    q = mp.Queue()
    hijo = []
    for c in range(10):
        j = c + 1
        process = mp.Process(target=hijos, args=(j, q,))
        hijo.append(process)
        hijo[c].start()
        hijo[c].join()
    print("\nCola:\n")
    while not q.empty():
        print(q.get(), end='')
    print("\nHijos terminados, Padre terminando")


if __name__ == '__main__':
    main()
