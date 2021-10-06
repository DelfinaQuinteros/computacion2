from getopt import getopt
from sys import argv
import sys
import socket

try:
    (opt, arg) = getopt(argv[1:], 'h:p:c:r')
except:
    sys.exit(1)

for args in opt:
    if args[0] == '-h':
        host = args[1]
    elif args[0] == '-p':
        port = int(args[1])
    elif args[0] == '-c':
        letra = args[1]
    elif args[0] == '-r':
        iteraciones = args[1]
    else:
        sys.exit(2)

