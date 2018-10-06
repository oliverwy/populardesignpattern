class Person:
    __name=""

    def __init__(self,name):
        self.__name=name

    def wearTShirts(self):
        print("大T恤",end='')
    def wearBigTrouser(self):
        print("垮裤",end='')
    def wearSneakers(self):
        print("破球鞋",end='')
    def wearSuit(self):
        print("西装",end='')
    def wearTie(self):
        print("领带",end='')
    def wearLeatherShoes(self):
        print("皮鞋",end='')

    def show(self):
        print("装扮的",self.__name)

if __name__=="__main__":
    xc=Person("小菜")

    print("\n第一种装扮")
    xc.wearTShirts()
    xc.wearBigTrouser()
    xc.wearSneakers()
    xc.show()

    print("\n第二种装扮：")
    xc.wearSuit()
    xc.wearTie()
    xc.wearLeatherShoes()
    xc.show()
