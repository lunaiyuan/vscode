# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '音乐下载器1.1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_musicdowload(object):
    def setupUi(self, musicdowload):
        musicdowload.setObjectName("musicdowload")
        musicdowload.resize(659, 466)
        self.centralwidget = QtWidgets.QWidget(musicdowload)
        self.centralwidget.setObjectName("centralwidget")
        self.ltit = QtWidgets.QLabel(self.centralwidget)
        self.ltit.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.ltit.setTextFormat(QtCore.Qt.AutoText)
        self.ltit.setWordWrap(True)
        self.ltit.setObjectName("ltit")
        self.inputname = QtWidgets.QLineEdit(self.centralwidget)
        self.inputname.setGeometry(QtCore.QRect(170, 10, 361, 41))
        self.inputname.setInputMask("")
        self.inputname.setObjectName("inputname")
        self.ButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearch.setGeometry(QtCore.QRect(540, 10, 81, 31))
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.textanswer = QtWidgets.QTextBrowser(self.centralwidget)
        self.textanswer.setGeometry(QtCore.QRect(80, 80, 451, 151))
        self.textanswer.setObjectName("textanswer")
        self.selectBox = QtWidgets.QComboBox(self.centralwidget)
        self.selectBox.setGeometry(QtCore.QRect(540, 130, 69, 22))
        self.selectBox.setObjectName("selectBox")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.selectBox.addItem("")
        self.Buttonstratdownload = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonstratdownload.setGeometry(QtCore.QRect(550, 230, 81, 51))
        self.Buttonstratdownload.setObjectName("Buttonstratdownload")
        self.textfinsh = QtWidgets.QTextBrowser(self.centralwidget)
        self.textfinsh.setGeometry(QtCore.QRect(50, 300, 481, 131))
        self.textfinsh.setObjectName("textfinsh")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 250, 371, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 260, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 54, 91))
        self.label.setObjectName("label")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(540, 50, 69, 22))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        musicdowload.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(musicdowload)
        self.statusbar.setObjectName("statusbar")
        musicdowload.setStatusBar(self.statusbar)

        self.retranslateUi(musicdowload)
        QtCore.QMetaObject.connectSlotsByName(musicdowload)

    def retranslateUi(self, musicdowload):
        _translate = QtCore.QCoreApplication.translate
        musicdowload.setWindowTitle(_translate("musicdowload", "音乐下载器"))
        self.ltit.setText(_translate("musicdowload", "<html><head/><body><p><span style=\" font-size:18pt;\">输入音乐名称</span></p></body></html>"))
        self.ButtonSearch.setText(_translate("musicdowload", "搜索"))
        self.textanswer.setHtml(_translate("musicdowload", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.selectBox.setItemText(0, _translate("musicdowload", "1"))
        self.selectBox.setItemText(1, _translate("musicdowload", "2"))
        self.selectBox.setItemText(2, _translate("musicdowload", "3"))
        self.selectBox.setItemText(3, _translate("musicdowload", "4"))
        self.selectBox.setItemText(4, _translate("musicdowload", "5"))
        self.selectBox.setItemText(5, _translate("musicdowload", "6"))
        self.selectBox.setItemText(6, _translate("musicdowload", "7"))
        self.selectBox.setItemText(7, _translate("musicdowload", "8"))
        self.selectBox.setItemText(8, _translate("musicdowload", "9"))
        self.selectBox.setItemText(9, _translate("musicdowload", "10"))
        self.Buttonstratdownload.setText(_translate("musicdowload", "开始下载"))
        self.pushButton.setText(_translate("musicdowload", "选择目录文件夹"))
        self.label.setText(_translate("musicdowload", "<html><head/><body><p><span style=\" font-size:14pt;\">搜索</span></p><p><span style=\" font-size:14pt;\">结果</span></p></body></html>"))
        self.type.setItemText(0, _translate("musicdowload", "qq音乐"))
        self.type.setItemText(1, _translate("musicdowload", "酷狗"))

