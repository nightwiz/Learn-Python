import gevent

'''
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程。
在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
'''

def foo():
    print("Running in foo")
    gevent.sleep(2)     #模仿IO，触发切换
    print("Explicit context switch to foo again")


def bar():
    print("Explicit context to bar")
    gevent.sleep(1)     #模仿IO，触发切换
    print("Implicit context switch back to bar")

def func3():
    print("running fun3")
    gevent.sleep(0)     #模拟IO，触发操作
    print("runnning func3 again")

gevent.joinall([
    gevent.spawn(foo),      #生成一个协程foo
    gevent.spawn(bar),      #生成一个协程bar
    gevent.spawn(func3),
])

'''
输出结果：
Running in foo
Explicit context to bar
running fun3
runnning func3 again
Implicit context switch back to bar
Explicit context switch to foo again

foo() sleep2秒，bar() sleep1秒，func3 sleep0秒

foo开始运行，遇到sleep切换到bar，bar运行，遇到sleep切换到func3，func3遇到sleep切换，但此时foo和bar都在sleep中，所以func3运行完剩下的
然后切换到foo，foo还在sleep中，切换到bar，运行完bar，切换到foo
'''