from abc import *
from ch6decoratorpattern.normaldecoratorpattern.Component import *


class Decorator(Component):
    _component = None

    def setComponent(self, component):
        if (isinstance(component, Component)):
            self._component = component

    def operation(self):
        if (self._component != None):
            self._component.operation()


class ConcreteDecoratorA(Decorator):
    __addedState = ''

    def operation(self):
        super().operation()
        self.__addedState = "New State"
        self.__getAddedState()
        print("具体装饰对象A的操作！")

    def __getAddedState(self):
        print("具体对象A的私有状态"+self.__addedState)


class ConcreteDecoratorB(Decorator):

    def operation(self):
        super().operation()
        self.__addedBehavior()
        print("具体装饰对象B的操作！")

    def __addedBehavior(self):
        print("具体装饰对象B特有的行为")


if __name__=="__main__":

    c=ConcreteComponent()
    d1=ConcreteDecoratorA()
    d2=ConcreteDecoratorB()

    d1.setComponent(c)
    d2.setComponent(d1)
    d2.operation()
