import threading
import time

#50个线程，每个sleep2秒，50个的sleep总数也是2秒
def run(n):
    print("task", n)
    time.sleep(2)
    print("task done", n, threading.current_thread())

#计算50个线程的总耗时，开始时间为当前时间
start_time = time.time()

#定义一个空列表，用来存线程实例
t_objs = []

for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
    #每次循环都将线程实例append到t_objs列表中
    t_objs.append(t)

#使用for循环，分别对上面的50个进程做join()
for t in t_objs:
    t.join()

print("-----all threads has finished...", threading.current_thread())

#计算总耗时
print("cost: ", time.time() - start_time)