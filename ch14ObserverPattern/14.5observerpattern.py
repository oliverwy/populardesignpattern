from abc import abstractmethod


class Subject:

    def __init__(self):
        self.__observers = []

    @abstractmethod
    def attach(self, observer):
        self.__observers.append(observer)

    @abstractmethod
    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for o in self.__observers:
            if (isinstance(o, Observer)):
                o.update()


class Observer:
    @abstractmethod
    def update(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.__subjectState=''

    def getSubjectState(self):

        return self.__subjectState

    def setSubjectState(self,subjectState):
        self.__subjectState=subjectState

    SubjectState=property(getSubjectState,setSubjectState)


class ConcreteObserver(Observer):
    def __init__(self,subject,name):
        self.__name=name
        self.__subject=subject

    def setSubject(self,subject):
        if isinstance(subject,Subject):
            self.__subject=subject

    def getSubject(self):
        return self.__subject

    Subject=property(getSubject,setSubject)

    def update(self):
        self.__observerState=self.__subject.SubjectState
        print("观察者"+self.__name+"的新状态是"+self.__observerState)


if __name__=="__main__":

    s=ConcreteSubject()
    s.attach(ConcreteObserver(s,"X"))
    s.attach(ConcreteObserver(s,"Y"))
    s.attach(ConcreteObserver(s,"Z"))
    s.SubjectState="ABC"

    s.notify()
