from abc import *

class Implementor: #这个是具体业务逻辑操作接口
    @abstractmethod
    def operation(self):
        pass


class ConcreteImplementorA(Implementor): #具体业务逻辑的执行器
    def operation(self):
        print("具体A的方法的执行！要是系统就是真实的业务逻辑")

class ConcreteImplementorB(Implementor): #具体业务逻辑的执行器
    def operation(self):
        print("具体B的方法的执行！要是系统就是真实的业务逻辑")


class Abstraction: #这个是接口

    def __init__(self):
        self._implementor=None

    def setImplementor(self,implementor):
        if isinstance(implementor,Implementor):
            self._implementor=implementor

    @abstractmethod
    def operation(self):
        self._implementor.operation()

class RefineAbstraction(Abstraction): #这个是具体的业务逻辑组合的对象
    def operation(self):
        self._implementor.operation()

if __name__=="__main__":
    ab=RefineAbstraction()
    ab.setImplementor(ConcreteImplementorA())
    ab.operation()
    ab.setImplementor(ConcreteImplementorB())
    ab.operation()