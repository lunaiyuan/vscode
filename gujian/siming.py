'''
Author: Pilzz
Date: 2020-11-09 21:05:57
LastEditTime: 2020-11-10 02:17:21
LastEditors: Please set LastEditors
Description: Pilzz
FilePath: \vscode\gujian\main.py
'''

from skill import Skill
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
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.rightclick()
    time.sleep(0.4)


def kaichang():
    pyautogui.press("z")
    huangdiezhenyi.use()
    hongguang.use()
    cifu.kaichangcifu()
    qianjiewanhe.use()


def main():
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