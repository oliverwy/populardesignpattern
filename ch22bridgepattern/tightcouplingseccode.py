from abc import *
class HandsetGame:
    @abstractmethod
    def run(self):
        pass

class HandsetNGame(HandsetGame):
    def run(self):
        print("运行N品牌手机游戏")


class HandsetMGame(HandsetGame):
    def run(self):
        print("运行M品牌手机游戏")

if __name__=="__main__":
    n=HandsetNGame()
    n.run()
    m=HandsetMGame()
    m.run()
