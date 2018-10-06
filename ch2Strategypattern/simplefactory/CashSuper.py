from abc import abstractmethod

class CashSuper:
    @abstractmethod
    def acceptCash(self,money):
        pass

class CashNormal(CashSuper):
    def acceptCash(self, money):
        return money

class CashRebate(CashSuper):
    __moneyRebate=1.0

    def __init__(self,moneyRebate):
        self.__moneyRebate=moneyRebate

    def acceptCash(self, money):
        return money*self.__moneyRebate

class CashReturn(CashSuper):
    __moneyCondition=0.0
    __moneyReturn=0.0

    def __init__(self,moneyCondition,moneyReturn):
        self.__moneyCondition=moneyCondition
        self.__moneyReturn=moneyReturn

    def acceptCash(self, money):
        result=0.0
        if(money>self.__moneyCondition):
            result=money-(money/self.__moneyCondition)*self.__moneyReturn
        return result


class CashFactory:
    @staticmethod
    def createCashAccept(type):
        cs=None
        if type=="正常收费":
            cs=CashNormal()
        elif type=="满300返100":
            cs=CashReturn(300,100)
        elif type=="打8折":
            cs=CashRebate(0.8)
        elif type=="打7折":
            cs=CashRebate(0.7)
        elif type=="打5折":
            cs=CashRebate(0.5)
        return cs
