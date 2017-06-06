from gevent import monkey
import gevent
from urllib import request
import time

monkey.patch_all()      #把当前程序的所有IO操作单独的做上标记

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s." % (len(data), url))

# urls = [
#     'https://www.python.org/',
#     'https://www.baidu.com/',
#     'https://github.com/'
# ]
#
# time_start = time.time()
#
# for url in urls:
#     f(url)
# print("同步爬虫的cost时间：", time.time() - time_start)


time_start = time.time()
gevent.joinall([
    gevent.spawn(f, "https://www.python.org/"),     #生成一个协程，传入函数f以及f的参数
    gevent.spawn(f, "https://www.baidu.com/"),
    gevent.spawn(f, "https://github.com/"),
])

print("多并发cost time:", time.time() - time_start)

'''
运行结果发现同步（串行）爬虫花费的时间比多并发爬虫花费的时间还少
原因是gevent无法识别到urllib的IO时间然后进行切换，所以其实也相当于是串行的
要让gevent知道urllib正在进行IO操作，需要给gevent打个补丁monkey.patch_all()
'''