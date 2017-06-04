from multiprocessing import Process, Pool
import time
import os


def foo(i):
    time.sleep(2)
    print("in procss", os.getpid())
    return i + 100


def bar(arg):
    print('-->exec done:', arg, os.getpid())


if __name__ == '__main__':
    #允许进程池同时放入5个进程
    pool = Pool(processes=5)

    #加入getpid可以看到回调是主进程去回调的
    print("主进程", os.getpid())

    for i in range(10):
        #pool的apply()方法是同步，串行
        #pool.apply(func=foo, args=(i,))
        '''
        pool中的apply_async方法是异步，并行。callback是回调，当执行完foo函数之后，回来调用bar函数。
        将foo函数的返回值作为参数传递给bar函数
        '''
        pool.apply_async(func=foo, args=(i,), callback=bar)

    print('end')

    #关闭进程池后再join()
    pool.close()

    #进程池中进程执行完毕后再关闭，如果注释掉pool.join()，那么程序不等进程执行完毕后就直接关闭了。
    pool.join()