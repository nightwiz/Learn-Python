import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        #yield接受一个赋值
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    #调用消费者的next方法，第一次调用是生成器，所以需要next
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        #send，唤醒生成器的同时给它传值
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    #启动两个consumer，一个producer
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()