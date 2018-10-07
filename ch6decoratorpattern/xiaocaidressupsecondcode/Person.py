from abc import *


class Person:
    __name = ''

    def __init__(self, name):
        self.__name = name

    def show(self):
        print('装扮的' + self.__name)


class Finery:

    @abstractmethod
    def show(self):
        pass


class TShirts(Finery):
    def show(self):
        print("大T恤额", end="")


class BigTrousers(Finery):
    def show(self):
        print("大裤衩", end="")


class Sneakers(Finery):
    def show(self):
        print("破球鞋", end="")


class Suit(Finery):
    def show(self):
        print("西服", end="")


class Tie(Finery):
    def show(self):
        print("领带", end="")


class LeatherShoes(Finery):
    def show(self):
        print("皮鞋", end="")


if __name__=="__main__":
    xc=Person("小菜")

    print("第一种装扮：",end='')
    dtx=TShirts()
    kk=BigTrousers()
    pqx=Sneakers()

    dtx.show()
    kk.show()
    pqx.show()
    xc.show()

    print("第二种装扮：",end='')

    xz=Suit()
    ld=Tie()
    px=LeatherShoes()
    xz.show()
    ld.show()
    px.show()
    xc.show()

