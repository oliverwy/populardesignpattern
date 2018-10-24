import copy
class Resume:

    def __init__(self,name):
        self.__name=name

    def setPersonInfo(self,sex,age):
        self.__sex=sex
        self.__age=age

    def setWorkExperience(self,timeArea,company):
        self.__timeArea=timeArea
        self.__company=company

    def display(self):
        print(self.__name+"  "+self.__sex+"  "+str(self.__age))
        print("工作经历："+self.__timeArea+" "+self.__company)

    def clone(self):
        return copy.copy(self)


if __name__=="__main__":
    a=Resume("大鸟")
    a.setPersonInfo("男",29)
    a.setWorkExperience("1998-2000","XXX公司")

    b=a.clone()
    b.setWorkExperience("1998-2006","YY企业")

    c=a.clone()

    c.setPersonInfo("男",24)

    a.display()
    b.display()
    c.display()