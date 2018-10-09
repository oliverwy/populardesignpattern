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


if __name__=="__main__":
    b=Forwards("巴蒂尔")
    b.attack()
    m=Guards("麦克格雷迪")
    m.attack()

    ym=Center("姚明")
    ym.attack()
    ym.defence()