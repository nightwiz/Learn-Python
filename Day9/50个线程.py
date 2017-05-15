import threading
import time

#50个线程，每个sleep2秒，50个的sleep总数也是2秒
def run(n):
    print("task",n)
    time.sleep(2)

for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i,))
    t.start()
