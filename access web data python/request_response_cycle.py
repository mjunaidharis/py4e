import socket

#AF_INET means gonna go accross the internet
#SOKC_STREAM implies there will be a stream of characters
#not block of texts.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#After creating socket
#we connect it!
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) #512 characters a tim
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()