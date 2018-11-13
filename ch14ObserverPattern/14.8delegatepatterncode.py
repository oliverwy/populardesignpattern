from abc import abstractmethod

class ItemStruc():
    def __init__(self,ob,methodName,argvc):
        self.__subject=ob
        self.__methodName=methodName
        self.__argvc=argvc

    def getargvc(self):
        return self.__argvc

    def setargvc(self,argvc):
        self.__argvc=argvc

    def setObject(self,ob):
        self.__subject=ob

    def getObject(self):
        return self.__subject

    def setMethodName(self,methodName):
        self.__methodName=methodName

    def getMethodName(self):
        return self.__methodName

    objectName=property(getObject,setObject)
    methodName=property(getMethodName,setMethodName)
    argcArray=property(getargvc,setargvc)

class Observer:

    @abstractmethod
    def register(self,subject,methodName): #想消息发出这注册我可以有信息怎么通知我
        if isinstance(subject,Subject):
            subject.reciverAttach(methodName)

    @abstractmethod
    def unregistr(self,subject,methodName):
        if isinstance(subject,Subject):
            subject.reciverDetach(methodName)

class StockObserver(Observer):

    def __init__(self,name,subject):
        super().__init__()
        self.__name=name
        self.__subject=subject

    def closeStockMarket(self):
        print(self.__subject.SubjectState+" "+self.__name+ "关闭股票行情，继续工作！")



class NbaObserver(Observer):

    def __init__(self,name,subject):
        super().__init__()
        self.__name=name
        self.__subject=subject

    def closeNbaLive(self):
        print(self.__subject.SubjectState+" "+self.__name+ "关闭NBA直播，继续工作！")



class Subject:

    def __init__(self):
        self._infoReciver=[]
        self.__subjectState=""
    @abstractmethod
    def notify(self):
        pass

    def getSubjectState(self):
        return self.__subjectState

    def setSubjectState(self,subjectState):
        self.__subjectState=subjectState

    SubjectState=property(getSubjectState,setSubjectState)

    @abstractmethod
    def emmiterAttach(self,methodName):
        pass

    @abstractmethod
    def emmiterDetach(self,methodName):
        pass

    @abstractmethod
    def reciverAttach(self,methodName):
        pass

    @abstractmethod
    def reciverDetach(self,methodname):
        pass


class Boss(Subject):
    pass

class Secretatry(Subject):


    def reciverAttach(self,methodName):
        if len(self._infoReciver)==0:
            print(methodName)
            self._infoReciver.append(methodName)
        else:
            for o in self._infoReciver:
                if methodName!=o:
                    self._infoReciver.append(methodName)
                    print(methodName)

    def reciverDetach(self,methodname):
        print(methodname)
        for o in self._infoReciver:
            if methodname == o:
                self._infoReciver.remove(o)
                print('remove')

    def notify(self):
        if len(self._infoReciver)>0:
            for o in self._infoReciver:
                o()




if __name__=="__main__":
    hu=Boss()
    se=Secretatry()
    se.SubjectState="老板回来了"


    t1=NbaObserver("ssd",se)
    t2=StockObserver("ss",se)
    # print(t1.closeNbaLive().__name__)
    t2.register(se,t2.closeStockMarket)
    # t2.unregistr(se,t2.closeStockMarket)
    t1.register(se,t1.closeNbaLive)
    se.notify()
