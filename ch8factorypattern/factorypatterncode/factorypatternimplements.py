from abc import *


class Operationx(object):

    def __init__(self):
        self.__numberA = 0
        self.__numberB = 0

    def getNumberA(self):
        return self.__numberA

    def getNumberB(self):
        return self.__numberB

    def setNumberA(self, value):
        self.__numberA = value

    def setNumberB(self, value):
        self.__numberB = value

    numberA = property(getNumberA, setNumberA)
    numberB = property(getNumberB, setNumberB)

    @abstractmethod
    def get_result(self):
        result = 0
        return result


class OperatinAdd(Operationx):
    def get_result(self):
        result = self.getNumberA() + self.getNumberB()
        return str(result)


class OperationSub(Operationx):
    def get_result(self):
        result = self.getNumberA() - self.getNumberB()
        return str(result)


class OperationMul(Operationx):
    def get_result(self):
        return str(self.getNumberA() * self.getNumberB())


class OperationDiv(Operationx):
    def get_result(self):
        try:
            return str(self.getNumberA() / self.getNumberB())
        except ZeroDivisionError as erro:
            return "不能除以0！"


class IFactory:
    @abstractmethod
    def createOperation(self):
        pass

class AddFactory(IFactory):
    def __init__(self):
        super.__init__(self)

    def createOperation(self):
        return OperatinAdd()


class SubFactory(IFactory):

    def createOperation(self):
        return OperationSub()


class MulFactory(IFactory):
    def createOperation(self):
        return OperationMul


class DivFactory(IFactory):
    def createOperation(self):
        return OperationDiv


if __name__=="__main__":
    operate = input("请输入操作符+、-、*、/: ")
    if operate == "+":
        normF=AddFactory()
    elif operate == "-":
        normF=SubFactory()
    elif operate == "*":
        normF=MulFactory()
    elif operate == "/":
        normF=DivFactory()
    else:
        normF = "输入的算符不正确"


    if not (isinstance(normF,str)):
        operator = normF.createOperation()
        opa = eval(input("请输入数字A："))
        opb = eval(input("请输入数字B："))
        operator.numberA=opa
        operator.numberB=opb
        result=operator.get_result()
    else:
        result=normF
    print("计算结果："+result)
