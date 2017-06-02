from multiprocessing import Process
import os

def info(title):
    print(title)
    print("module name: ", __name__)
    print("parent process: ", os.getppid())     #获取父进程ID
    print("process id: ", os.getpid())          #获取自己的ID
    print("\n\n")

def f(name):
    info('\033[31mcalled from child process function f\033[0m')
    print("hello", name)

if __name__ == "__main__":
    info("\033[32mmain process line\033[0m")
    p = Process(target=f, args=('bob',))
    p.start()