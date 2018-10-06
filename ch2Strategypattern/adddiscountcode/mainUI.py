# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    total=0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 59, 16))
        self.label_2.setObjectName("label_2")
        self.txtPrice = QtWidgets.QLineEdit(Form)
        self.txtPrice.setGeometry(QtCore.QRect(100, 30, 231, 21))
        self.txtPrice.setText("")
        self.txtPrice.setObjectName("txtPrice")
        self.txtNum = QtWidgets.QLineEdit(Form)
        self.txtNum.setGeometry(QtCore.QRect(100, 60, 231, 21))
        self.txtNum.setObjectName("txtNum")
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(350, 20, 114, 40))
        self.btnOK.setObjectName("btnOK")
        self.btnReset = QtWidgets.QPushButton(Form)
        self.btnReset.setGeometry(QtCore.QRect(350, 50, 114, 40))
        self.btnReset.setObjectName("btnReset")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 400, 59, 16))
        self.label_3.setObjectName("label_3")
        self.lblResult = QtWidgets.QLabel(Form)
        self.lblResult.setGeometry(QtCore.QRect(130, 400, 341, 16))
        self.lblResult.setTextFormat(QtCore.Qt.PlainText)
        self.lblResult.setObjectName("lblResult")
        self.lbxList = QtWidgets.QListWidget(Form)
        self.lbxList.setGeometry(QtCore.QRect(30, 130, 431, 251))
        self.lbxList.setObjectName("lbxList")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 59, 16))
        self.label_4.setObjectName("label_4")
        self.cbxType = QtWidgets.QComboBox(Form)
        self.cbxType.setGeometry(QtCore.QRect(90, 90, 250, 32))
        self.cbxType.setObjectName("cbxType")
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.cbxType.addItem("")

        self.retranslateUi(Form)
        self.btnOK.clicked.connect(self.on_click)
        self.btnReset.clicked.connect(self.on_reset_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def on_click(self):  # 未做错误保护，写实际应用的时候注意业务逻辑异常保护
        if (self.cbxType.currentIndex()==0):
            totalPrice = eval(self.txtPrice.text()) * eval(self.txtNum.text())
        elif (self.cbxType.currentIndex()==1):
            totalPrice = eval(self.txtPrice.text()) * eval(self.txtNum.text())*0.8
        elif (self.cbxType.currentIndex()==2):
            totalPrice = eval(self.txtPrice.text()) * eval(self.txtNum.text()) * 0.7
        elif (self.cbxType.currentIndex()==3):
            totalPrice = eval(self.txtPrice.text()) * eval(self.txtNum.text()) * 0.5

        self.total = self.total + totalPrice
        self.lbxList.addItem("单价：" + self.txtPrice.text() + "  数量：" + self.txtNum.text() + "  合计：" + str(totalPrice))
        self.lblResult.setText(str(self.total))
        self.lblResult.repaint()
        print(str(self.total))

    def on_reset_click(self):
        print("Reset is Clicked")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "单价："))
        self.label_2.setText(_translate("Form", "数量："))
        self.btnOK.setText(_translate("Form", "确定"))
        self.btnReset.setText(_translate("Form", "重置"))
        self.label_3.setText(_translate("Form", "总计："))
        self.lblResult.setText(_translate("Form", "0.0"))
        self.label_4.setText(_translate("Form", "折扣："))
        self.cbxType.setItemText(0, _translate("Form", "正常收费"))
        self.cbxType.setItemText(1, _translate("Form", "打8折"))
        self.cbxType.setItemText(2, _translate("Form", "打7折"))
        self.cbxType.setItemText(3, _translate("Form", "打5折"))

