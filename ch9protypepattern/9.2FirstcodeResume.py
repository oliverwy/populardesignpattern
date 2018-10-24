class Rusume:

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

if __name__=="__main__":
    a=Rusume("大鸟")
    a.setPersonInfo("男",29)
    a.setWorkExperience("1998-2000","XXX公司")


    b=Rusume("大鸟")
    b.setPersonInfo("男",29)
    b.setWorkExperience("1998-2000","XXX公司")


    c=Rusume("大鸟")
    c.setPersonInfo("男",29)
    c.setWorkExperience("1998-2000","XXX公司")

    a.display()
    b.display()
    c.display()
