from abc import *

class Company:
    def __init__(self,name):
        if isinstance(name,str):
            self._name=name

    @abstractmethod
    def add(self,c):
        pass

    @abstractmethod
    def remove(self,c):
        pass

    @abstractmethod
    def display(self,depth):
        pass

    @abstractmethod
    def lineOfDuty(self):
        pass

class ConcreteCompany(Company):

    def __init__(self,name):
        super().__init__(name)
        self.__children=[]

    def add(self, c):
        if (isinstance(c,Company)):
            self.__children.append(c)
    def remove(self, c):
        if (isinstance(c,Company)):
            self.__children.remove(c)

    def display(self, depth):
        print('-'*depth+self._name)
        for c in self.__children:
            if isinstance(c,Company):
                c.display(depth+2)
    def lineOfDuty(self):
        for c in self.__children:
            if isinstance(c,Company):
                c.lineOfDuty()

class HRDepartment(Company):
    def __init__(self,name):
        super().__init__(name)

    def add(self, c):
        pass

    def remove(self, c):
        pass

    def display(self, depth):
        print('-'*depth+self._name)

    def lineOfDuty(self):
        print(self._name+'负责招聘培训员工！')

class FinanceDepartment(Company):
    def __init__(self,name):
        super().__init__(name)

    def add(self, c):
        pass

    def remove(self, c):
        pass

    def display(self, depth):
        print('-'*depth+self._name)

    def lineOfDuty(self):
        print(self._name+'公司财务收支管理！')


if __name__=="__main__":
    root=ConcreteCompany("北京总公司")
    root.add(HRDepartment("总公司人力资源部"))
    root.add(FinanceDepartment("总公司财务部"))

    comp=ConcreteCompany("上海华东分公司")
    comp.add(HRDepartment("华东分公司人力资源部"))
    comp.add(FinanceDepartment("华东分公司财务部"))
    root.add(comp)

    comp1=ConcreteCompany("南京办事处")
    comp1.add(HRDepartment("南京办事处人力资源部"))
    comp1.add(FinanceDepartment("南京办事处财务部"))
    comp.add(comp1)

    comp2=ConcreteCompany("杭州办事处")
    comp2.add(HRDepartment("杭州办事处人力资源部"))
    comp2.add(FinanceDepartment("杭州办事处财务部"))
    comp.add(comp2)

    print("结构图：")
    root.display(1)

    print(("职责："))
    root.lineOfDuty()