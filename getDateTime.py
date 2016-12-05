# Title: Google Time
# Date: 2016-12-03
# Id : getDateTime.py
# Firmware: 0.9.6.b1
# Copyright: Claus Kuehnel  (ckuehnel.sz@gmail.com)

# Read date & time from Google server

import os, socket

print("Running getDateTime.py on firmware version %s" % os.uname().release)

addr = socket.getaddrinfo('www.google.ch', 80)[0][-1]

debug = False

s = socket.socket()
s.connect(addr)
s.send(b'GET / HTTP/1.1\r\nHost: www.google.ch\n\r\n')
data = s.recv(1000)

if '200 OK' in data:
    print('OK')
else:
    print('Socket error')
    
data = data.decode()
if debug: print(data)

str = 'Date: '
start = data.find(str)
stop = data.find('\r\n', start)

date = data[start+len(str):stop]

if debug :  print(start,  stop)
    
print (date)

s.close()
