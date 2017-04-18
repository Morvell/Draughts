

import socket
import string
import base64



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost', 60001))
s.listen(2)



connect,adress = s.accept()
while 1:

    data=connect.recv(1024)
    print(data.decode())



print("all get")
s.close()


