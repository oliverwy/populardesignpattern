from abc import *

class IGiveGift:
    @abstractmethod
    def giveDolls(self):
        pass

    @abstractmethod
    def giveFlowers(self):
        pass

    @abstractmethod
    def giveChocolate(self):
        pass

class SchoolGirl:
    __name=''

    def getName(self):
        return self.__name

    def setName(self,value):
        if value!="":
            self.__name=value

    name=property(getName,setName)


class Pursuit(IGiveGift):
    __mm=None

    def __init__(self,mm):
        if (isinstance(mm,SchoolGirl)):
            self.__mm=mm

    def giveDolls(self):
        print(self.__mm.name+"送你个洋娃娃！")

    def giveFlowers(self):
        print(self.__mm.name+"送你鲜花！")

    def giveChocolate(self):
        print(self.__mm.name+"送你巧克力！")

class Proxy(IGiveGift):
    __gg=None

    def __init__(self,mm):
        if (isinstance(mm,SchoolGirl)):
            self.__gg=Pursuit(mm)

    def giveDolls(self):
        self.__gg.giveDolls()

    def giveFlowers(self):
        self.__gg.giveFlowers()

    def giveChocolate(self):
        self.__gg.giveChocolate()

if __name__=="__main__":
    jiaojiao=SchoolGirl()
    jiaojiao.name="李娇娇"

    daili=Pursuit(jiaojiao)
    daili.giveDolls()
    daili.giveFlowers()
    daili.giveChocolate()

