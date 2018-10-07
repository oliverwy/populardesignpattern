class Proxy:
    __mm=None

    def __init__(self,mm):
        if(isinstance(mm,SchoolGirl)):
            self.__mm=mm

    def giveDolls(self):
        print(self.__mm.name+"送你洋娃娃！")

    def giveFlowers(self):

        print(self.__mm.name+"送你鲜花！")

    def giveChocolate(self):

        print(self.__mm.name+"送你巧克力！")

class SchoolGirl:
    __name=''

    def getName(self):
        return self.__name

    def setName(self,value):
        if value!="":
            self.__name=value

    name=property(getName,setName)

if __name__=="__main__":
    jiaojiao = SchoolGirl()
    jiaojiao.name = "李娇娇"
    daili=Proxy(jiaojiao)

    daili.giveDolls()
    daili.giveFlowers()
    daili.giveFlowers()