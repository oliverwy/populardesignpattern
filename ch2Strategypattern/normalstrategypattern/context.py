from ch2Strategypattern.normalstrategypattern.stratege import *

class Context:

    __strategy=None

    def __init__(self,strategy):
        self.__strategy=strategy

    def ContextInterface(self):
        self.__strategy.AlgorithmInsterface()