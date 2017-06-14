import socket
import select
import queue

'''
使用select模拟一个socket服务器
想用多路复用(单进程)实现一个socket server，socket必须得处于一个非阻塞模式
'''

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)

server.setblocking(False)   #设置为非阻塞

inputs = [server, ]  #将需要被select监测的链接传入到inputs列表
outputs = []    #将哪些需要返回数据给客户端的链接存到outputs列表

msg_dic = {}    #初始化一个空字典

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)   #返回可读，可写，错误的链接；例如客户端突然断开，产生exceptional
    print(readable, writeable, exceptional)

    for r in readable:
        if r is server:     #代表来了一个新链接
            conn,addr = server.accept()
            print("来了个新链接", addr)
            inputs.append(conn)  #将这个链接加入到监测队列中；
            # 因为这个新建立的链接现在还没发数据过来，现在就接收程序就报错。所以要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn
            msg_dic[conn] = queue.Queue()   #初始化一个队列，后面存放要返回给客户端的数据
        else:
            data = r.recv(1024)
            print("收到数据", data)
            msg_dic[r].put(data)    #r既是上面的conn
            outputs.append(r)       #放入返回的链接队列里
            # r.send(data)
            # print("send done...")

    for w in writeable:     #要返回给客户端的链接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)  #返回给客户端源数据

        outputs.remove(w)   #确保下次循环的时候writeable不返回已经处理完的链接

    for e in exceptional:   #如果客户端的链接断开了，那么把这个链接从inputs和outputs去掉
        if e in outputs:    #判断e有没有在outputs里面，有就去掉
            outputs.remove(e)

        inputs.remove(e)    #不用判断e有没有在inputs里面，肯定在!

        del msg_dic[e]      #从消息队列中删除e这个链接