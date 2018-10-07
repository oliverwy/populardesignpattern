from abc import *

class Subject:
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("真实的请求，来自"+self.__class__.__name__)

class Proxy(Subject):
    __realSubject=None
    def request(self):
        if self.__realSubject==None:
            self.__realSubject=RealSubject()
        print("我是代理"+self.__class__.__name__+"负责调用"+self.__realSubject.__class__.__name__+"的request",end='')
        self.__realSubject.request()

if __name__=="__main__":
    proxy=Proxy()
    proxy.request()