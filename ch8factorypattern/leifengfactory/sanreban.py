class LeiFeng:
    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣")

    def bugRice(self):
        print("买米")

class Undergraduate(LeiFeng):
    pass

if __name__=="__main__":
    student1=Undergraduate()
    student1.wash()
    student2=Undergraduate()
    student2.sweep()
    student3=Undergraduate()
    student3.bugRice()