from abc import abstractmethod
import copy

class ProtoType:

    def __init__(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    @abstractmethod
    def clone(self):
        pass

class ConcreteProtoType(ProtoType):

    def __init__(self,id):
        super().__init__(id)


    def clone(self):
        return copy.copy(self) #浅层拷贝

if __name__=="__main__":

    p1=ConcreteProtoType("I")
    c1=p1.clone()
    print("P1.ID="+p1.getId())
    print("C1.ID="+c1.getId())