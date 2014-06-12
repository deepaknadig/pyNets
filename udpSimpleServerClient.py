__author__ = 'Deepak Nadig Anantha'

import socket
import sys

PORT = 55555
MAX = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print 'Server is listening at: %s' % repr(s.getsockname())
    while True:
        data, address = s.recvfrom(MAX)
        print 'FROM: %s: \nMESSAGE: %s' % (address, repr(data))
        s.sendto('Your data was %s Bytes' % len(data), address)
elif sys.argv[1:] == ['client']:
    s.sendto('This is a Client Message', ('127.0.0.1', PORT))
    data, address = s.recvfrom(MAX)
    print 'The Server at %s says: %s' % (address[0], repr(data))
else:
    print 'USAGE: python udpSimpleServerClient.py server|client'