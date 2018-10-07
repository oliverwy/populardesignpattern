class Person:
    __name = ''

    def __init__(self):
        pass

    def __init__(self, name):
        if (isinstance(name, str)):
            self.__name = name

    def show(self):
        print("装扮的" + self.__name)


class Finery(Person):
    _component = None

    def decorate(self, component):
        if (isinstance(component, Person)):
            self._component = component

    def show(self):
        super().show()
        if (self._component != None):
            self._component.show()


class TShirts(Finery):

    def show(self):
        print("大T恤额",end='')
        super().show()


class BigTrousers(Finery):

    def show(self):
        print("垮裤",end='')
        super().show()


class Sneaker(Finery):

    def show(self):
        print("破球鞋",end='')
        super().show()


class Suit(Finery):

    def show(self):
        print("西装",end='')
        super().show()


class Tie(Finery):

    def show(self):
        print("领带",end='')
        super().show()


class LeatherShoes(Finery):

    def show(self):
        print("皮鞋",end='')
        super().show()


if __name__=="__main__":
    xc=Person("小菜")
    print("第一种装扮:")

    pqx=Sneaker()
    kk=BigTrousers()
    dtx=TShirts()

    pqx.decorate(xc)
    kk.decorate(pqx)
    dtx.decorate(kk)
    dtx.show()