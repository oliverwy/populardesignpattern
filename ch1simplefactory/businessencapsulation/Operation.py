class Operation:
    def __init__(self):
        super.__init__()

    @staticmethod
    def getResult(numberA,numberB,operator):
        result=0
        if operator=="+":
            result=numberA+numberB
        elif operator=="-":
            result=numberA-numberB
        elif operator=="*":
            result=numberA*numberB
        elif operator=="/":
            try:
                result=numberA/numberB
            except ZeroDivisionError as erro:
                result="不能被0整除"
        else:
            result=operator+"是无效运算符！"
        if not (isinstance(result,str)):
            result=str(result)

        return  result

if __name__=="__main__":
    op=input("请输入操作符+、-、*、/: ")
    opa=eval(input("请输入数字A："))
    opb=eval(input("请输入数字B："))

    strResult=Operation.getResult(opa,opb,op)
    print(strResult)
