import socket
se = socket.socket()
ip,port = '18.222.181.227',8000
se.connect((ip,port))
name1 = input('enter your name: ')
se.send(bytes(name1,'utf-8'))
print('connected to the server!')
print(se.recv(1024).decode())
c2name = se.recv(1024).decode()
print(c2name,'is online!')
while 1:
    message = se.recv(1024).decode()
    new_message = input('>>>')
    new_message = new_message.encode()
    se.send(new_message)
    message = se.recv(1024).decode()
    print(c2name+':', message)