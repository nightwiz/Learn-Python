import sys
import socket
import time
import gevent

from gevent import socket,monkey
monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)   #启动一个协程，传入handle_request函数以及函数的参数cli

def handle_request(conn):       #conn 就是上面代码中的cli
    try:
        while True:
            data = conn.recv(1024)
            print("recv", str(data, encoding='utf-8'))
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__ == '__main__':
    server(8001)
