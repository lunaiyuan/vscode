# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\.git\vscode\yundongyuanguanlixitong\AskRe.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AskRe(object):
    def setupUi(self, AskRe):
        AskRe.setObjectName("AskRe")
        AskRe.resize(342, 218)
        self.label = QtWidgets.QLabel(AskRe)
        self.label.setGeometry(QtCore.QRect(20, 10, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(AskRe)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AskRe)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(AskRe)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(AskRe)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(AskRe)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AskRe)
        QtCore.QMetaObject.connectSlotsByName(AskRe)

    def retranslateUi(self, AskRe):
        _translate = QtCore.QCoreApplication.translate
        AskRe.setWindowTitle(_translate("AskRe", "Dialog"))
        self.label.setText(_translate("AskRe", "项目："))
        self.pushButton.setText(_translate("AskRe", "下一项"))
        self.pushButton_2.setText(_translate("AskRe", "上一项"))
        self.pushButton_3.setText(_translate("AskRe", "全部取消"))
        self.label_2.setText(_translate("AskRe", "成绩："))
