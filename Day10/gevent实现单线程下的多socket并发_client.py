import socket

HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input(">>:"), encoding="utf-8")     #输入数据
    s.sendall(msg)                                  #send数据
    data = s.recv(1024)                             #收到数据
    print('Recevied', repr(data))                   #格式化输出

s.close()