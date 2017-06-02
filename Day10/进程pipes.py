from multiprocessing import Process, Pipe
'''
通过pipe实现进程间数据的传递（不是真正意义上的共享）
'''

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print("from parent: ", conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("你好")
    p.join()