import socket
import string
import base64


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
done = True
while done:
    try:
        s.connect(('localhost', 60001))
    except:
        continue
    done = False
    print('connect')

while True:
    message = input()
    s.send(message.encode())
print('all send')
s.close()

