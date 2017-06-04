from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print("hello world", i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

'''
进程锁的作用：因为所有进程都是共享同一块屏幕，打印的时候可能会出现上一个进程的结果还没打印完下一个进程的结果就打印出来了。
加上进程锁就可以避免上述这种情况。

'''
