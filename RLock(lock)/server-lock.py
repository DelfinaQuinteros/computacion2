import threading
from getopt import getopt
from sys import argv
import sys
import time
import socket

try:
    (opt, arg) = getopt(argv[1:], 'p:f:')
except:
    sys.exit(1)

for args in opt:
    if args[0] == '-p':
        port = int(args[1])
    elif args[0] == '-f':
        file_name = args[1]
    else:
        sys.exit(2)


