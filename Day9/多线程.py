import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)

t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))
t3 = threading.Thread(target=run,args=("t3",))

start_time = time.time()
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()

#等待t1执行完毕。相当多进程变成串行的。
#t1.join()
#t2.join()
#t3.join()

#计算总耗时
print("cost=",time.time() - start_time)
# run("t1")
# run("t2")