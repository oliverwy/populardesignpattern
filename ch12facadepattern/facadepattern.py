class SubSystemOne:
    def methodOne(self):
        print("子系统方法一")


class SubSystemTwo:
    def methodTwo(self):
        print("子系统方法二")


class SubSystemThree:
    def methodThree(self):
        print("子系统方法三")


class SubSystemFour:
    def methodFour(self):
        print("子系统方法四")


class Facade:
    def __init__(self):
        self.one=SubSystemOne()
        self.two=SubSystemTwo()
        self.three=SubSystemThree()
        self.four=SubSystemFour()

    def methodA(self):
        print('方法组A（）--------')
        self.one.methodOne()
        self.two.methodTwo()
        self.four.methodFour()

    def methodB(self):
        print('方法组B()-----------')
        self.two.methodTwo()
        self.three.methodThree()

if __name__=="__main__":
    facade=Facade()
    facade.methodA()
    facade.methodB()