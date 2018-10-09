from abc import *

class Player:
    def __init__(self,name):
        self._name=name
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defence(self):
        pass


class Forwards(Player):
    def __init__(self,name):
        super().__init__(name)

    def attack(self):
        print("前锋"+self._name+"进攻！")

    def defence(self):
        print("前锋"+self._name+"防守！")

class Center(Player):
    def __init__(self,name):
        super().__init__(name)

    def attack(self):
        print("前锋"+self._name+"进攻！")

    def defence(self):
        print("前锋"+self._name+"防守！")

class Guards(Player):
    def __init__(self,name):
        super().__init__(name)

    def attack(self):
        print("前锋"+self._name+"进攻！")

    def defence(self):
        print("前锋"+self._name+"防守！")

class ForeignCenter:
    __name=''
    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    name=property(getName,setName)

    def wattack(self):
        print("外籍中锋"+self.__name+"进攻！")

    def wdefense(self):
        print("外籍中锋"+self.__name+"防守！")


class Translator(Player):
    def __init__(self,name):
        super().__init__(name)
        self.__wjzf=ForeignCenter()
        self.__wjzf.name=name

    def attack(self):
        self.__wjzf.wattack()

    def defence(self):
        self.__wjzf.wdefense()

if __name__=="__main__":
    b=Forwards("巴蒂尔")
    b.attack()
    m=Guards("麦克格雷迪")
    m.attack()

    ym=Translator("姚明")
    ym.attack()
    ym.defence()