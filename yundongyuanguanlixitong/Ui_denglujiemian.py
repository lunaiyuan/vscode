from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
from PyQt5.QtWidgets import *
import time
from threading import Thread
from Ui_mainui import Ui_MainWindow


class Ui_Denglu(object):
    #def __init__(self, ):
    def setupUi(self, Denglu):
        Denglu.setObjectName("Denglu")
        Denglu.resize(388, 297)
        self.centralwidget = QtWidgets.QWidget(Denglu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 54, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")

        #self.pushButton.clicked[bool].connect(Denglu.close)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked[bool].connect(self.zhuce)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Denglu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Denglu)
        self.statusbar.setObjectName("statusbar")
        Denglu.setStatusBar(self.statusbar)

        self.retranslateUi(Denglu)
        QtCore.QMetaObject.connectSlotsByName(Denglu)
        self.Denglu = Denglu
        #self.mianui = mianui

    def retranslateUi(self, Denglu):
        _translate = QtCore.QCoreApplication.translate
        Denglu.setWindowTitle(_translate("Denglu", "Sport"))
        self.label.setText(_translate("Denglu", "用户名："))
        self.label_2.setText(_translate("Denglu", "密码："))
        self.pushButton.setText(_translate("Denglu", "登录"))
        self.pushButton_2.setText(_translate("Denglu", "注册"))
        self.label_3.setText(_translate("Denglu", "运动员体能测评管理系统"))
        self.pushButton.clicked[bool].connect(self.try_denglu)

    def try_denglu(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        try:
            with open('./data/user.txt', "r") as t:
                user_json = json.loads(t.read())
                if user_json[username] == password:
                    msg_box = QMessageBox(QMessageBox.Warning, '提示',
                                          f'{username}登录成功')
                    msg_box.exec_()
                    self.Denglu.close()
                    time.sleep(0.5)
                    ui_2.get_username(username)
                    print(ui_2.username)
                    mainui.show()

                else:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '账号密码错误！')
                    msg_box.exec_()

        except Exception as e:
            print(e)
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '账号密码错误！')
            msg_box.exec_()

    def zhuce(self):
        #检查输入格式
        import os
        a = os.path.exists('./data')
        if not a:
            os.makedirs('./data')
        try:
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            #检验用户储存文件是否存在
            #读取
            try:
                with open('./data/user.txt', "r") as t:
                    user_json = json.loads(t.read())
                    try:
                        user_json[username]
                        msg_box = QMessageBox(QMessageBox.Warning, '警告',
                                              '账号已存在，请登录！')
                        msg_box.exec_()
                        return
                    except:
                        pass

            except:
                print(1)
                user_json = {}

            #写入
            user_json[username] = password
            with open('./data/user.txt', 'w') as t:
                a = json.dumps(user_json)
                t.write(a)
            msg_box = QMessageBox(QMessageBox.Warning, '提示！', '注册完成！')
            msg_box.exec_()
        except Exception as e:
            print(e)
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '格式错误请重新输入！')
            msg_box.exec_()


def denglu():
    app = QApplication(sys.argv)
    dengluui = QMainWindow()

    ui = Ui_Denglu()
    ui.setupUi(dengluui)
    dengluui.show()
    ###########################
    global mainui, ui_2
    mainui = QMainWindow()
    ui_2 = Ui_MainWindow()
    ui_2.setupUi(mainui)
    #ui_2.show()
    sys.exit(app.exec_())


denglu()
