import socket
<<<<<<< HEAD
=======
import time
>>>>>>> 45c7c6fb8b458d5c1885afc7f48901c775fb5e94

def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
<<<<<<< HEAD
    client.send(bytes("Hello,SB", encoding='utf-8'))

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
=======
    f = open('index.html', 'rb')
    date = f.read()
    t = str(time.time())
    date.replace("@@@@@", t)
    f.close()
    client.send(date)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
>>>>>>> 45c7c6fb8b458d5c1885afc7f48901c775fb5e94
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 45c7c6fb8b458d5c1885afc7f48901c775fb5e94
