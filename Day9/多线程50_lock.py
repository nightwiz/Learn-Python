import threading
import time

def run(n):

    #获取锁
    lock.acquire()

    global num
    num += 1

    #释放锁
    lock.release()

t_objs = []

lock = threading.Lock()
num = 0

for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()


#打印主线程，以及当前活动进程数
print("threading is ", threading.current_thread(), threading.active_count())
print("num: ", num)