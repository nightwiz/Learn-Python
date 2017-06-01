import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)
    print('task done:',n)
start_time = time.time()
t_objs = []

for i in range(50):
        t = threading.Thread(target=run,args=("t-%s" %i,))
        t.setDaemon(True)
        t.start()
        t_objs.append(t)

#for t in t_objs:
#    t.join()

#打印主线程，以及当前活动进程数
print("threading is ",threading.current_thread(),threading.active_count())

#打印总花费时间
print("cost time: ",time.time() - start_time)