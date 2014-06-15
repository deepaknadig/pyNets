__author__ = 'Deepak Nadig Anantha'
'''
The unreliable UDP Client and Server simulates random packet drops at the Server.
'''

import socket
import sys
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

PORT = 1060
MAX = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print '%r also %r' % (sys.argv[1], len(sys.argv))

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    interface = sys.argv[2] if len(sys.argv) > 2 else ''
    s.bind((interface, PORT))
    print 'Listening at', s.getsockname()

    while True:
        data, address = s.recvfrom(MAX)
        if random.randint(0,1):
            print bcolors.OKBLUE + '-----------------------------------------\n'
            print bcolors.HEADER + 'FROM IP: %s, PORT: %s \nMESSAGE: %s' % (address[0], address[1], repr(data))
            s.sendto('Your data was %d Bytes' % len(data), address)
            print bcolors.OKBLUE + '\n\n-----------------------------------------'
        else:
            print bcolors.WARNING + 'Packet was dropped!'
            #s.sendto('The packet from %s was dropped' % repr(address[0]), address)
elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    hostname = sys.argv[2]
    print hostname
    print s.getsockname()
    s.connect((hostname, PORT))
    print s.getsockname()
    delay = 1
    while True:
        s.send('This is a client message')
        s.settimeout(delay)
        try:
            data = s.recv(MAX)
        except socket.timeout:
            print 'Waiting for %d seconds for a reply' % delay
            delay += 1
            if delay > 2:
                raise RuntimeError('Server Timeout Occured')
        except:
            raise
        else:
            break

    print 'The Server says %s' % repr(data)
else:
    print 'Usage: python udpClientServerUnreliable.py server'
    print 'Usage: python udpClientServerUnreliable.py client <host>'
