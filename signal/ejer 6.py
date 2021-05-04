#!/usr/bin/python3
import signal
import os
import time


def padre():
    os.kill(hijo_2, signal.SIGUSR1)


def hijo():
    print("Soy el hijo 2 con PID:", os.getpid(), "pong")


fork = os.fork()
if fork == 0:
    time.sleep(0.1)
    for i in range(10):
        print("Soy el hijo 1 con PID:", os.getpid(), "ping")
        os.kill(os.getppid(), signal.SIGUSR1)
        time.sleep(5)
else:
    signal.signal(signal.SIGUSR1, padre)
    hijo_2 = os.fork()
    if hijo_2 == 0:
        signal.signal(signal.SIGUSR1, hijo)
while True:
    signal.pause()
