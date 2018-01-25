"""
#coding=utf-8
#python2中的代码

def test(a, b, func):
    result = func(a, b)
    return result


func_new = input("请输入一个函数：")    #此处输入一个匿名函数,lambda x,y:x+y 可以得到a+b的和。只限在py2中，在py3中会将输入的函数当成字符串报错
print(num)

"""

# python3中实现输入函数并得到结果


def test(a,b,func):
    result = func(a,b)
    return result


func_new = input("请输入一个函数：")


# 使用eval函数获取返回值，相当于把 "lambda x,y:x+y" 的双引号删除，得到一个表达式
func_new = eval(func_new)

num = test(11,22,func_new)
print(num)


# 动态语言和静态语言的区别
# 静态语言需要先确定功能再执行


