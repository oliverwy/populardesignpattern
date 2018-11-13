# def job(self):
#     print("%s is working" % self.name)
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print("%s is eating %s." % (self.name, food))
#
#
# d = Person('liming')
# choice = input(">>:").strip()
#
# if hasattr(d, choice):
#     func = getattr(d, choice)  # 输入 eat
#     func("apple")  # 调用 eat 方法
# else:
#     setattr(d, choice, job)  # 添加反射方法 输入work
#     d.work(d)

# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:CarsonLi、
'''
hasattr(obj,name_str) 判断一个obj对象是否有对应name_str的方法
getattr(obj,name_str) 根据字符串name_str获取Obj对象中对应方法的内存地址
setattr(obj,key,value) 为对象Obj新增或修改属性或者方法
delattr(obj,name_str) 删除对象obj中名为name_str的属性或者方法
'''


def bulk(self):
    print("%s is yelling" % self.name)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

def fuc(a,b,c):
    print(a+b+c)
print(fuc.__code__.co_varnames)

jim = Dog("Jim")
choise = input(">>输入需要执行的操作:").strip()
if hasattr(Dog, choise):
    func = getattr(jim, choise)
    print(func)
    print(func.__code__.co_argcount)
    print(func.__code__.co_varnames)
    func("巧克力")
    # delattr(jim,choise)
else:
    # 动态装配一个方法 choise为方法名，bulk为方法的内存地址
    setattr(jim, choise, bulk)
    # 调用时用转配的方法名，即传入的choise值,这里需要传入对象本身
    getattr(jim, choise)(jim)
    # 动态装配一个属性,也可以修改属性
    setattr(jim, choise, "新装配的属性")
    print(getattr(jim, choise))
# print(jim.name)
# jim.eat("狗粮")

