from ch12facadepattern.stockprotypecode import *
class Fund:

    def __init__(self):
        self.gu1=Stock1()
        self.gu2=Stock2()
        self.gu3=Stock3()
        self.nd1=NationalDebt1()
        self.rt1=Realty1()
    def sellFund(self):

        self.gu1.sell()
        self.gu2.sell()
        self.gu3.sell()
        self.nd1.sell()
        self.rt1.sell()

    def buyFund(self):
        self.gu1.buy()
        self.gu2.buy()
        self.gu3.buy()
        self.nd1.buy()
        self.rt1.buy()

if __name__=="__main__":

    fund=Fund()
    fund.buyFund()
    fund.sellFund()

