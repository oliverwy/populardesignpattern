from abc import abstractmethod

class Operationx(object):

    def __init__(self):

        self.__numberA=0
        self.__numberB=0

    def getNumberA(self):
        return self.__numberA

    def getNumberB(self):
        return self.__numberB


    def setNumberA(self,value):
        self.__numberA=value

    def setNumberB(self,value):
        self.__numberB=value

    numberA = property(getNumberA, setNumberA)
    numberB = property(getNumberB, setNumberB)

    @abstractmethod
    def get_result(self):
        result=0
        return result

class OperatinAdd(Operationx):
    def get_result(self):
        result=self.getNumberA()+self.getNumberB()
        return str(result)

class OperationSub(Operationx):
    def get_result(self):
        result=self.getNumberA()-self.getNumberB()
        return str(result)

class OperationMul(Operationx):
    def get_result(self):
        return str(self.getNumberA()*self.getNumberB())

class OperationDiv(Operationx):
    def get_result(self):
        try:
            return str(self.getNumberA()/self.getNumberB())
        except ZeroDivisionError as erro:
            return "不能除以0！"

class SimpleOperationFactory:
    @staticmethod
    def createOperate(operate):
        if operate == "+":
            operator = OperatinAdd()
        elif operate == "-":
            operator = OperationSub()
        elif operate == "*":
            operator = OperationMul()
        elif operate == "/":
            operator = OperationDiv()
        else:
            operator="输入的算符不正确"

        return operator

if __name__=="__main__":
    op = input("请输入操作符+、-、*、/: ")
    operator=SimpleOperationFactory.createOperate(op)
    if not (isinstance(operator,str)):
        opa = eval(input("请输入数字A："))
        opb = eval(input("请输入数字B："))
        operator.numberA=opa
        operator.numberB=opb
        result=operator.get_result()
    else:
        result=operator
    print("计算结果："+result)