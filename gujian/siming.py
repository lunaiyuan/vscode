'''
Author: Pilzz
Date: 2020-11-09 21:05:57
LastEditTime: 2020-11-11 11:25:22
LastEditors: Please set LastEditors
Description: Pilzz
FilePath: //vscode//gujian//main.py
'''

from skill import *
import pyautogui
from threading import Thread
from pynput import keyboard


skill = [
    # 技能的集合
    'cifu',
    'qianjiewanhe',
    # 'yuhongqingjue',
    'huangdiezhenyi',
    'hongguang',
]


def zuozuoyou():
    # 112循环

    global x, l
    Thread(target=lingli).start()
    while True:
        global x
        if x:
            if l:
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.55)
                pyautogui.rightClick()
                time.sleep(0.4)
            else:
                time1 = time.time()
                while time.time() - time1 <= 1.5:
                    pyautogui.click()

        else:
            return


def press1():
    global x

    while True:
        if x:
            pyautogui.press("1")
            time.sleep(0.1)
        else:
            return


def kaichang():
    # 开场爆发
    pyautogui.press("z")
    huangdiezhenyi.use()
    hongguang.use()
    cifu.kaichangcifu()
    qianjiewanhe.use()


def kaishi():
    print('开始')
    global x
    x = True


def jieshu():
    global x
    x = False


def cf():
    cifu.use()


def hd():
    huangdiezhenyi.use()


def qianjie():
    qianjiewanhe.use()


def lingli():
    global x, l
    l = True
    while x:
        im = pyautogui.screenshot(region=(1180, 500, 1, 1))
        px = im.getpixel((0, 0))
        if px[1] <= 170:
            l = False
            print(px[1])
        else:
            l = True
        time.sleep(0.3)


def hot():
    print('热键检测开始')
    with keyboard.GlobalHotKeys({
        '=': kaishi,
        '-': jieshu,
        'q': cf,
        'r': hd,
        '2': qianjie
    }) as h:
        h.join()


pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True


def main():
    global cifu, qianjiewanhe, huangdiezhenyi, hongguang, x
    x = False
    Thread(target=hot).start()
    jisu = 20.78
    cifu = Cifu(jisu)
    qianjiewanhe = Skill("qianjiewanhe", jisu)
    # yuhongqingjue = Skill("yuhongqingjue", 20)
    huangdiezhenyi = Skill("huangdiezhenyi", jisu)
    hongguang = Skill("hongguang", jisu)

    def shuchucaozup():
        while True:
            if x:
                if canornot['qianjiewanhe'] and canornot['cifu'] and canornot['huangdiezhenyi']:
                    Thread(target=press1).start()
                    txunhuan = Thread(target=zuozuoyou)
                    kaichang()
                    txunhuan.start()
                    break
                else:
                    Thread(target=press1).start()
                    txunhuan = Thread(target=zuozuoyou)
                    txunhuan.start()
                    break

            else:
                print(x)
                time.sleep(1)
        while True:
            if x:
                print('开始了')
                time.sleep(2)
            else:
                shuchucaozup()
    shuchucaozup()


if __name__ == "__main__":
    main()
