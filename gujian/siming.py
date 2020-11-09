'''
Author: Pilzz
Date: 2020-11-09 21:05:57
LastEditTime: 2020-11-10 02:28:00
LastEditors: Please set LastEditors
Description: Pilzz
FilePath: \vscode\gujian\main.py
'''

from skill import *
import pyautogui
from threading import Thread
skill = [
    'cifu',
    'qianjiewanhe',
    #'yuhongqingjue',
    'huangdiezhenyi',
    'hongguang',
]


def zuozuoyou():
    #112循环
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.rightClick()
    time.sleep(0.4)


def kaichang():
    #开场爆发
    pyautogui.press("z")
    huangdiezhenyi.use()
    hongguang.use()
    cifu.kaichangcifu()
    qianjiewanhe.use()


def main():
    global cifu, qianjiewanhe, huangdiezhenyi, hongguang
    cifu = Cifu(20)
    qianjiewanhe = Skill("qianjiewanhe", 20)
    #yuhongqingjue = Skill("yuhongqingjue", 20)
    huangdiezhenyi = Skill("huangdiezhenyi", 20)
    hongguang = Skill("hongguang", 20)

    kaichang()
    while True:
        zuozuoyou()
        pyautogui.press("1")


if __name__ == "__main__":
    main()