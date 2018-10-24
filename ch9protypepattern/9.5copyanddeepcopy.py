from abc import abstractmethod
from copy import copy,deepcopy
class WorkWExpience:
    def setWorkDate(self,date):
        self.__workDate=date

    def getWorkDate(self):
        return self.__workDate

    def setCompany(self,company):
        self.__company=company

    def getCompany(self):
        return self.__company


class Resume:

    def __init__(self,name):
        self.__name=name
        self.__work=WorkWExpience()

    def setPersonInfo(self,sex,age):
        self.__sex=sex
        self.__age=age

    def setWorkExperience(self,timeArea,company):
        self.__work.setWorkDate(timeArea)
        self.__work.setCompany(company)

    def display(self):
        print(self.__name+"  "+self.__sex+"  "+str(self.__age))
        print("工作经历："+self.__work.getWorkDate()+" "+self.__work.getCompany())

    def clone(self):
        return copy(self)

if __name__=="__main__":
    a=Resume("大鸟")
    a.setPersonInfo("男",29)
    a.setWorkExperience("1998-2000","XXX公司")

    b=a.clone()
    b.setWorkExperience("1998-2006","YY企业")

    c=a.clone()

    c.setPersonInfo("男",24)
    c.setWorkExperience("1998-2006","ZZ企业")

    a.display()
    b.display()
    c.display()