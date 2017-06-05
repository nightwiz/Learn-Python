from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)   #启动一个协程
gr2 = greenlet(test2)
gr1.switch()    #切换，依次输出12,56,34,78
#gr2.switch()   #输出56,12,78