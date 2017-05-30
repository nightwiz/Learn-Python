import threading
import time

event = threading.Event()

def lighter():
    count = 0
    #设定标志位，当前为绿灯
    event.set()
    while True:
        if 5 < count < 10:
            #把标志位清空，现在状态为红灯
            event.clear()
            print("\033[41;1mred light in on...\033[0m")
        elif count > 10:
            #设置标志位，现在状态为绿灯
            event.set()
            #清空count
            count = 0
        else:
            print("\033[42;1mgreen light in on...\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            #判断标志位是否set，如果标志位有设置，代表是绿灯状态
            print("[%s] running..." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..." % name)
            #阻塞，等待设定
            event.wait()
            print("\033[42;1m[%s] green light in on,start going...\033[0m" % name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()
