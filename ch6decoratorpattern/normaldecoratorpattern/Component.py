from abc import *

class Component:
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("具体对象操作！")

