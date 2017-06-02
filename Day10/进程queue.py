from multiprocessing import Process,Queue

'''
通过进程queue（有别于线程queue）实现进程间数据的传递（不是真正意义上的共享）
'''

def f(q):
    q.put([42,None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    #将q作为参数传给函数f
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()