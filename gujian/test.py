'''
Author: your name
Date: 2020-11-10 15:34:13
LastEditTime: 2020-11-10 15:36:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vscode\gujian\test.py
'''
from pynput import keyboard
from threading import Thread
def hot():
    with keyboard.GlobalHotKeys({
        '=': kaishi,
        '-': jieshu,
        'q': cf,
        'r': hd,
        '2': qianjie
    }) as h:
        h.join()

def kaishi():
    print(111)
def jieshu():
    print(222)
def cf():
    print(333)
def hd():
    print(444)
def qianjie():
    print(555)
Thread(target=hot).start()