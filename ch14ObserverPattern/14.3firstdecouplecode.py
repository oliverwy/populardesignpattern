from abc import abstractmethod


class Observer:

    def __init__(self, name, sub):
        if isinstance(sub, Secretary):
            self._sub = sub
        self._name = name

    @abstractmethod
    def update(self):
        pass


class StockObserver(Observer):
    def __init__(self,name,sub):

        if isinstance(sub,Secretary):
            super().__init__(name,sub)

    def update(self):
        print(self._sub.SecretaryAction+"  "+self._name+" 关闭股票行情，继续工作！")

class NbaObserver(Observer):
    def __init__(self,name,sub):

        if isinstance(sub,Secretary):
            super().__init__(name,sub)

    def update(self):
        print(self._sub.SecretaryAction+"  "+self._name+" NBA直播，继续工作！")

class Secretary:

    def __init__(self):
        self.__observers=[]

    def attach(self,observer):
        if (isinstance(observer,Observer)):
            self.__observers.append(observer)

    def notify(self):
        for c in self.__observers:
            if isinstance(c,Observer):
                c.update()
    def detach(self,observer):
        self.__observers.remove(observer)

    def setSecretaryAction(self,action):
        self.__action=action

    def getSecretaryAction(self):
        return self.__action

    SecretaryAction=property(getSecretaryAction,setSecretaryAction)

if __name__=="__main__":
    tongzhizhe=Secretary()

    tongshi1=StockObserver("张飞",tongzhizhe)
    tongshi2=NbaObserver("关羽",tongzhizhe)

    tongzhizhe.attach(tongshi1)
    tongzhizhe.attach(tongshi2)

    tongzhizhe.SecretaryAction="老板回来了"
    tongzhizhe.notify()
