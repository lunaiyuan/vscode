'''
Author: your name
Date: 2020-11-09 20:26:24
LastEditTime: 2020-11-11 11:21:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vscode\gujian\mian.py
'''
import pyautogui
import time
from threading import Thread
all_cd = {
    'cifu': 42,
    'qianjiewanhe': 115,
    #'yuhongqingjue': 42,
    'huangdiezhenyi': 90,
    'hongguang': 28
}
anjianbiao = {
    'cifu': 'q',
    'qianjiewanhe': 'F1',
    #'yuhongqingjue': 'z',
    'huangdiezhenyi': 'r',
    'hongguang': 'e'
}
canornot = {
    'cifu': True,
    'qianjiewanhe': True,
    #'yuhongqingjue': True,
    'huangdiezhenyi': True,
    'hongguang': True
}
#can_use_skill = []


def getpxmohu(px):
    #获得模糊的坐标
    npx = []
    for i in px:
        npx.append(range(i - 5, i + 5, 1))
    return npx


class Skill():
    #技能类，需要技能名称，和当前急速属性
    def __init__(self, name, jisu):
        self.name = name
        self.cd = all_cd[name] / (1 + (jisu / 100))
        self.anjian = anjianbiao[name]

    def use(self):
        #使用技能并且记录cd变化技能状态
        if canornot[self.name]:
            pyautogui.press(f"{self.anjian}")
            t1 = Thread(target=self.check)
            t1.start()
            time1 = time.time()
            if self.name == "qianjiewanhe":
                while True:
                    pyautogui.press("F1")
                    pyautogui.rightClick()
                    if time.time() - time1 > 9.5:
                        return
            elif self.name == "huangdiezhenyi":
                while True:
                    time2 = time.time()
                    if time2 - time1 >= 2.85:
                        return
                    else :
                        pyautogui.press('1')
                        time.sleep(0.1)
            elif self.name == "hongguang":
                time.sleep(1)
        else:
            print(f'技能{self.name}剩余冷却时间:{self.cdtime}秒')
    def check(self):
        canornot[self.name] = False
        time1 = time.time()
        while True:
            self.cdtime = self.cd - (time.time() - time1)
            time.sleep(1)
            if self.cdtime <= 0:
                canornot[self.name] = True
                return
        #can_use_skill.append(self.name)


class Cifu(Skill):
    #赐福专有类， kaichangcifu()用于开场使用
    def __init__(self, jisu):
        super().__init__('cifu', jisu)

    def kaichangcifu(self):
        self.use()
        Thread(target=self.kpanduanka).start()

    def kpanduanka(self):
        while True:
            im = pyautogui.screenshot(region=(1069, 599, 1, 1))
            px = im.getpixel((0, 0))
            npx = getpxmohu((87, 74, 82))
            if px[0] in npx[0] and px[1] in npx[1] and px[2] in npx[2]:
                while True:
                    im = pyautogui.screenshot(region=(1200, 580, 1, 1))
                    px = im.getpixel((0, 0))
                    npx = getpxmohu((254, 244, 169))
                    if px[0] in npx[0] and px[1] in npx[1] and px[2] in npx[2]:
                        pyautogui.press('q')
                        time.sleep(0.1)
                        pyautogui.press('q')
                        time.sleep(0.1)
                        pyautogui.press('z')
                        self.baoyin()
                        return

    def baoyin(self):
        time1 = time.time()

        while True:
            pyautogui.press('e')
            if time.time() - time1 > 12:
                #y = True
                break