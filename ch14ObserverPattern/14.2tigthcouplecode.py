from abc import abstractmethod

class StockObserver:
    def __init__(self,name,sub):

        if isinstance(sub,Secretary):
            self.__sub=sub
        self.__name=name


    def update(self):

        print(self.__sub.SecretaryAction+"  "+self.__name+" 关闭股票行情继续工作！")


class Secretary:

    def __init__(self):
        self.__observers=[]

    def attach(self,observer):
        if (isinstance(observer,StockObserver)):
            self.__observers.append(observer)

    def notify(self):
        for c in self.__observers:
            if isinstance(c,StockObserver):
                c.update()

    def setSecretaryAction(self,action):
        self.__action=action

    def getSecretaryAction(self):
        return self.__action

    SecretaryAction=property(getSecretaryAction,setSecretaryAction)


if __name__=="__main__":
    tongzhizhe=Secretary()

    tongshi1=StockObserver("张飞",tongzhizhe)
    tongshi2=StockObserver("关羽",tongzhizhe)

    tongzhizhe.attach(tongshi1)
    tongzhizhe.attach(tongshi2)

    tongzhizhe.SecretaryAction="老板回来了"
    tongzhizhe.notify()
