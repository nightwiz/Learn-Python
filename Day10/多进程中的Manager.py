from multiprocessing import Process, Manager
import os


def f(d, l):
    #往字典里添加key，value
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    #往列表里面添加1
    #l.append(1)
    #往列表里面添加进程号
    l.append(os.getpid())
    #每个执行的进程都打印l这个列表的结果
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        #生成一个可在多个进程之间共享数据的字典，可以同时修改（不需要手动加锁，manager已经加锁）
        d = manager.dict()
        #生成一个可在多个进程之间共享数据的列表，默认列表里有5个数据[0,1,2,3,4]
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            #等待结果
            res.join()

        print(d)
        #最后的结果，10个进程修改同一个字典，结果是一样{0.25: None, 1: '1', '2': 2}

        print(l)
        #最后的结果1，10个进程修改列表，每个进程往列表里面添加了一个1，最后的结果[0, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #最后的结果1，10个进程修改列表，每个进程往列表里面添加进程号，最后的结果[0, 1, 2, 3, 4, 7444, 7140, 10236, 7612, 10636, 296, 11888, 3452, 6016, 5168]