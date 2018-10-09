from abc import *

class Component:

    def __init__(self,name):
        if isinstance(name,str):
            self._name=name


    @abstractmethod
    def add(self ,c):
        pass

    @abstractmethod
    def remove(self,c):
        pass

    @abstractmethod
    def display(self,depth):
        pass

class Leaf(Component):

    def __init__(self,name):
        if isinstance(name,str):
            super().__init__(name)

    def add(self, c):
        print("不能像叶子节点添加一个叶子！")

    def remove(self, c):
        print("不能像叶子节点删除一个叶子！")

    def display(self, depth):
        print('-'*depth+self._name)


class Composite(Component):


    def __init__(self,name):
        if (isinstance(name,str)):
            super().__init__(name)
        self.__children=[]


    def add(self,c):
        if (isinstance(c,Component)):
            self.__children.append(c)

    def remove(self,c):
        if (isinstance(c,Component)):
            self.__children.remove(c)

    def display(self,depth):
        for c in self.__children:
            c.display(depth+2)

    def px(self):
        print(self.__children)


if __name__=="__main__":
    root=Composite("root")

    root.add(Leaf("Leaf A"))
    root.add(Leaf("Leaf B"))

    comp=Composite("Composite X")
    comp.add(Leaf("Leaf XA"))
    comp.add(Leaf("Leaf XB"))

    root.add(comp)

    comp2=Composite("Composite X")
    comp2.add(Leaf("Leaf XYA"))
    comp2.add(Leaf("Leaf XYB"))

    comp.add(comp2)

    root.add(Leaf("Leaf C"))
    # root.px()
    leaf=Leaf("D")
    root.add(leaf)
    root.display(1)
    print('移除D')
    root.remove(leaf)
    root.display(1)
    # root.px()