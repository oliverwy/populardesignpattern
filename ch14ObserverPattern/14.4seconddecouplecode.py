from abc import abstractmethod


class Subject:

    def __init__(self):
        self.__subjectState = ""

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    def getSubjectState(self):
        return self.__subjectState

    def setSubjectState(self, subjectState):
        self.__subjectState = subjectState

    SubjectState = property(getSubjectState, setSubjectState)

class Boss(Subject):
    def __init__(self):
        super().__init__()
        self.__observers=[]

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for o in self.__observers:
            if isinstance(o,Observer):
                o.update()

class Observer:

    def __init__(self, name, sub):
        if isinstance(sub, Subject):
            self._sub = sub
        self._name = name

    @abstractmethod
    def update(self):
        pass

class StockObserver(Observer):
    def __init__(self,name,sub):

        if isinstance(sub,Subject):
            super().__init__(name,sub)

    def update(self):
        print(self._sub.SubjectState+"  "+self._name+" 关闭股票行情，继续工作！")

class NbaObserver(Observer):
    def __init__(self,name,sub):

        if isinstance(sub,Subject):
            super().__init__(name,sub)

    def update(self):
        print(self._sub.SubjectState+"  "+self._name+" 关闭NBA直播，继续工作！")


if __name__=="__main__":
    tongzhizhe=Boss()

    tongshi1=StockObserver("张飞",tongzhizhe)
    tongshi2=NbaObserver("关羽",tongzhizhe)

    tongzhizhe.attach(tongshi1)
    tongzhizhe.attach(tongshi2)

    tongzhizhe.detach(tongshi2)

    tongzhizhe.SubjectState="老板回来了"
    tongzhizhe.notify()

    tongzhizhe.attach(tongshi2)

    tongzhizhe.notify()
