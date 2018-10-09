class Stock1:
    def sell(self):
        print("股票1卖出")

    def buy(self):
        print("股票1买入")


class Stock2:
    def sell(self):
        print("股票2卖出")

    def buy(self):
        print("股票2买入")


class Stock3:
    def sell(self):
        print("股票3卖出")

    def buy(self):
        print("股票3买入")


class NationalDebt1:
    def sell(self):
        print("国债1卖出")

    def buy(self):
        print("国债1买入")


class Realty1:
    def sell(self):
        print("地产1卖出")

    def buy(self):
        print("地产1买入")

if __name__=="__main__":
    gu1=Stock1()
    gu2=Stock2()
    gu3=Stock3()

    nd1=NationalDebt1()
    r11=Realty1()

    gu1.buy()
    gu2.buy()
    gu3.buy()
    nd1.buy()
    r11.buy()

    gu1.sell()
    gu2.sell()
    gu3.sell()
    nd1.sell()
    r11.sell()
    
