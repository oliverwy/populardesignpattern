from abc import *
class Target:
    @abstractmethod
    def request(self):
        print("普通请求！")

class Adaptee:
    def specificRequest(self):
        print("特殊请求！")

class Adapter(Target):
    def __init__(self):
        self.__adaptee=Adaptee()

    def request(self):
        self.__adaptee.specificRequest();


if __name__=="__main__":
    target=Adapter()
    target.request()