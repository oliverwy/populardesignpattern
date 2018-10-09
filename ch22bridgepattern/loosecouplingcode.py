from abc import *

class HandsetSoft:
    @abstractmethod
    def run(self):
        pass


class HandsetGame(HandsetSoft):
    def run(self):
        print("运行手机游戏！")

class HandsetAddressList(HandsetSoft):
    def run(self):
        print("运行手机通讯录！")


class HandsetBrand:
    def __init__(self):
        self._soft=None

    def setHandsetSoft(self,soft):
        if isinstance(soft,HandsetSoft):
            self._soft=soft

    @abstractmethod
    def run(self):
        pass

class HandsetBrandN(HandsetBrand):
    def run(self):
        self._soft.run()

class HandsetBrandM(HandsetBrand):
    def run(self):
        self._soft.run()
class HandBrandS(HandsetBrand):

    def run(self):
        self._soft.run()


class HandsetMP3(HandsetSoft):

    def run(self):
        print("运行手机MP3播放！")


if __name__=="__main__":
    ab=HandsetBrandN()
    # ab.run()
    ab.setHandsetSoft(HandsetGame())
    ab.run()
    ab.setHandsetSoft(HandsetAddressList())
    ab.run()
    ab.setHandsetSoft(HandsetMP3())
    ab.run()

    ab=HandsetBrandM()
    ab.setHandsetSoft(HandsetGame())
    ab.run()
    ab.setHandsetSoft(HandsetAddressList())

    ab.run()
    ab.setHandsetSoft(HandsetMP3())
    ab.run()