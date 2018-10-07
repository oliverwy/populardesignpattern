from abc import *
class LeiFeng:
    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣")

    def bugRice(self):
        print("买米")

class Undergraduate(LeiFeng):
    pass

class Volunter(LeiFeng):
    pass
class IFactory:
    @abstractmethod
    def createLeiFeng(self):
        pass


class UndergraduateFactory(IFactory):

    def createLeiFeng(self):
        return Undergraduate()

class VolunteerFactory(IFactory):
    def createLeiFeng(self):
        return Volunter()


if __name__=="__main__":
    fact=UndergraduateFactory()
    stu=fact.createLeiFeng()
    stu.wash()
    stu.sweep()
    stu.bugRice()