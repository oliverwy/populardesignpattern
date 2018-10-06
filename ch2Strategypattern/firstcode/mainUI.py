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
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 400, 341, 16))
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.lbxList = QtWidgets.QListWidget(Form)
        self.lbxList.setGeometry(QtCore.QRect(30, 90, 431, 291))
        self.lbxList.setObjectName("lbxList")

        self.retranslateUi(Form)
        self.btnOK.clicked.connect(self.on_click)
        self.btnReset.clicked.connect(self.on_reset_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def on_click(self): #未做错误保护，写实际应用的时候注意业务逻辑异常保护
        totalPrice = eval(self.txtPrice.text()) * eval(self.txtNum.text())
        self.total = self.total + totalPrice
        self.lbxList.addItem("单价："+self.txtPrice.text()+"  数量："+self.txtNum.text()+"  合计："+str(totalPrice))
        self.label_4.setText(str(self.total))
        self.label_4.repaint()
        print(str(self.total))

    def on_reset_click(self):
        print("Reset is Clicked")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "商场收银系统模型"))
        self.label.setText(_translate("Form", "单价："))
        self.label_2.setText(_translate("Form", "数量："))
        self.btnOK.setText(_translate("Form", "确定"))
        self.btnReset.setText(_translate("Form", "重置"))
        self.label_3.setText(_translate("Form", "总结："))
        self.label_4.setText(_translate("Form", "0.0"))

