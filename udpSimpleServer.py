import socket
import sys

__author__ = 'Deepak Nadig Anantha'
'''
This server runs only on localhost
'''


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
else:
    print 'USAGE: python udpSimpleServer.py server'