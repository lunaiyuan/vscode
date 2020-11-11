'''
Author: your name
Date: 2020-11-10 15:34:13
LastEditTime: 2020-11-11 11:04:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vscode\gujian\test.py
'''
from pynput import keyboard
from threading import Thread
import pyautogui

def kaishi():
    im = pyautogui.screenshot(region=(1180, 500, 1, 1))
    px = im.getpixel((0, 0))
    print(px)
def hot():
    print('热键检测开始')
    with keyboard.GlobalHotKeys({
        '=': kaishi,
    }) as h:
        h.join()

Thread(target=hot).start()