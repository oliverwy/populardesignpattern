from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from ch2Strategypattern.StrategyPlusFactoryPattern.mainUI import Ui_Form

class Ui_demo(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(Ui_demo,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        pass
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    Ui=Ui_demo()
    Ui.show()
    sys.exit(app.exec_())

