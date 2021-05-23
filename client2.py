import socket
se = socket.socket()
ip,port = '18.222.181.227',8000
se.connect((ip,port))
name2 = input('enter your name: ')
se.send(bytes(name2,'utf-8'))
print('connected to the server!')
print(se.recv(1024).decode())
c1name = se.recv(1024).decode()
print(c1name,'is online!')
while 1:
    message = se.recv(1024).decode()
    print(c1name+':',message)
    new_message = input('>>>')
    new_message = new_message.encode()
    se.send(new_message)