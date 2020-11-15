# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '音乐下载器.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import sys
import requests
from threading import Thread
#from multiprocessing import Pool,Manager
import os
import time


class Ui_musicdowload(object):

    def update_path(self):
        try :
            with open('path.txt','r') as t:

                self.lineEdit.setText(t.readline())
        except :
            pass

    def setupUi(self, musicdowload):
        musicdowload.setObjectName("musicdowload")
        musicdowload.resize(659, 350)
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
        #搜索按钮
        self.ButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearch.setGeometry(QtCore.QRect(540, 10, 81, 31))
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.ButtonSearch.clicked[bool].connect(self.search)


        self.textanswer = QtWidgets.QTextBrowser(self.centralwidget)
        self.textanswer.setGeometry(QtCore.QRect(80, 80, 451, 151))
        self.textanswer.setObjectName("textanswer")
        self.selectBox = QtWidgets.QComboBox(self.centralwidget)
        self.selectBox.setGeometry(QtCore.QRect(540, 90, 69, 22))
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
        # self.textfinsh = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textfinsh.setGeometry(QtCore.QRect(50, 300, 481, 131))
        # self.textfinsh.setObjectName("textfinsh")

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

    def search(self):
        # 点击确定 获取到urls列表
        self.update_path()
        name = self.inputname.text()
        url = 'https://music.liuzhijin.cn/'
        types = self.type.currentIndex()
        # print(types)
        lists = ['qq','kugou']
        tt = lists[types]
        #print(tt)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'input': name,
            'filter': 'name',
            'type': tt,
            'page': '1'
        }
        response = requests.post(url=url, headers=headers, data=data)
        self.urls = []
        songs = []
        t = 0
        for number in response.json()['data']:
            t += 1

            # print(response.json()['data'][number]['url'])
            songs.append(f'{t}.{number["title"]},歌手:{number["author"]}')
            texts = ''
            for song in songs:
                texts += song + "\n"
            self.textanswer.setText(texts)
            self.urls.append(number['url'])

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
        self.Buttonstratdownload.clicked[bool].connect(self.download)
        self.pushButton.setText(_translate("musicdowload", "选择目录文件夹"))
        self.pushButton.clicked[bool].connect(self.setBrowerPath)
        self.type.setItemText(0, _translate("musicdowload", "qq音乐"))
        self.type.setItemText(1, _translate("musicdowload", "酷狗"))


        self.label.setText(_translate("musicdowload", "<html><head/><body><p><span style=\" font-size:14pt;\">搜索</span></p><p><span style=\" font-size:14pt;\">结果</span></p></body></html>"))
    def download(self):
        print('下载开始')

        self.sizes = []
        path = self.lineEdit.text()
        name = self.inputname.text()

        t1 = Thread(target=self.start_download)
        t1.start()
        time.sleep(0.1)


        pd = True

        while pd:
            try:
                time.sleep(0.1)
                size = self.sizes[0]
                file_size = os.path.getsize(f'{path}/{name}.m4a')

                file_size = int(file_size) / 1024 / 1024
                print(f'{round(file_size, 3)}m/{round(size, 3)}m')
                if size <= file_size:
                    print(f'{name}下载完成')
                    pd = False

            except:
                pass
    def start_download(self):

        path = self.lineEdit.text()
        name = self.inputname.text()

        number = self.selectBox.currentIndex()
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        url = self.urls[number]

        response = requests.get(url=url, headers=headers, stream=True)
        size = response.headers['Content-Length']
        size = int(size) / 1024 / 1024
        self.sizes.append(size)
        with open(f'{path}/{name}.m4a', 'wb') as m:
            for music in response.iter_content(chunk_size=128):
                if music:
                    m.write(music)


    def setBrowerPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                   "浏览",
                                                                   "C:\\Users\Administrator\Desktop\下载音乐")
        self.lineEdit.setText(download_path)
        with open('path.txt','w') as t:
            t.write(download_path)
class MyWindow(QMainWindow,Ui_musicdowload):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.update_path()
app = QApplication(sys.argv)
mywin = MyWindow()
mywin.show()
sys.exit(app.exec_())