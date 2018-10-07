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

class SimpleFactory:
    @staticmethod
    def createLeiFeng(type):
        result=None
        if type=="学雷锋的大学生":
            result=Undergraduate()
        elif type=="社区志愿者":
            result=Volunter()

        return result

if __name__=="__main__":
    studentA=SimpleFactory.createLeiFeng("学雷锋的大学生")
    studentA.bugRice()
    studentB=SimpleFactory.createLeiFeng("学雷锋的大学生")
    studentB.sweep()
    studentC=SimpleFactory.createLeiFeng("学雷锋的大学生")
    studentC.wash()
