from abc import abstractmethod


class Strategy:

    @abstractmethod
    def AlgorithmInsterface(self):
        pass


class ConreteStrategyA(Strategy):
    def AlgorithmInsterface(self):
        print("算法A的实现！")


class ConreteStrategyB(Strategy):
    def AlgorithmInsterface(self):
        print("算法B的实现！")


class ConreteStrategyC(Strategy):
    def AlgorithmInsterface(self):
        print("算法C的实现！")
