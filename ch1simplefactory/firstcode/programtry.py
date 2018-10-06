if __name__=="__main__":
    op=input("请输入操作符+、-、*、/: ")
    opa=eval(input("请输入数字A："))
    opb=eval(input("请输入数字B："))

    if op=="+":
        result=opa+opb
    elif op=="-":
        result=opa-opb
    elif op=="*":
        result=opa*opb
    elif op=="/":
        try:
            result=opa/opb
        except ZeroDivisionError as err:
            result="不能除以0！"
    if not (isinstance(result,str)):
        result=str(result)
    print("计算结果为："+result)
