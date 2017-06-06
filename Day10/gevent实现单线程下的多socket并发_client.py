import socket

HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input(">>:"), encoding="utf-8")
    s.sendall(msg)
    data = s.recv(1024)
    print('recevied', repr(data))   #格式化输出

s.close()