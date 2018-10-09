from abc import *


class HandsetBrand:
    @abstractmethod
    def run(self):
        pass


class HandsetBrandM(HandsetBrand):
    pass


class HandsetBrandN(HandsetBrand):
    pass


class HandsetBrandMGame(HandsetBrandM):
    def run(self):
        print("运行M品牌手机游戏！")


class HandsetBrandNGame(HandsetBrandN):
    def run(self):
        print("运行N品牌手机游戏！")


class HandsetBrandMAddressList(HandsetBrandM):
    def run(self):
        print("运行M品牌手机通讯录")


class HandsetBrandNAddressList(HandsetBrandN):
    def run(self):
        print("运行N品牌手机通讯录")


if __name__ == "__main__":
    ab = HandsetBrandMAddressList()
    ab.run()
    ab = HandsetBrandMGame()
    ab.run()
    ab = HandsetBrandNAddressList()
    ab.run()
    ab = HandsetBrandNGame()
    ab.run()
