import threading

#定义一个MyThread类，继承threading的Thread
class MyThread(threading.Thread):
    def __init__(self,n):
        #重写init方法
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("running task",self.n)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()
