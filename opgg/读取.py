#-*- codeing = utf-8 -*-
# coding=gbk
#@Time : 2020/7/8 0:02
#@Author : 鲁乃源
#@File : 读取.py
#@Software : PyCharm
import json
from wenzishibie import *
import pyautogui
import time
def get_Average(list):
   sum = 0
   for item in list:
      sum += item
   return sum/len(list)
def get_arg_oneteam(quxians):
    s = []
    for ss in quxians:
        s.append(round(get_Average(ss),2))
    return s
with open('./data.txt', 'r+', encoding='utf-8')as t:
    txt = json.load(t)



    # 召唤师技能1 = txt[weizhi][champin]['召唤师技能']
    # #[[['Flash', 'Dot'], ['94.05%', '49.61%']], [['Teleport', 'Flash'], ['5.29%', '50.21%']]]
    #
    # 技能 = txt[weizhi][champin]['技能']
    # #[['Q', 'W', 'E', 'Q', 'Q', 'R', 'Q', 'E', 'Q', 'E', 'R', 'E', 'E', 'W', 'W'], ['58.76%', '62.5%']]
    # 克制 = txt[weizhi][champin]['克制']
    # #[['影流之主', 'zed', 0.5055], ['疾风剑豪', 'yasuo', 0.5275], ['卡牌大师', 'twistedfate', 0.4974], ['解脱者', 'sylas', 0.5039], ['诡术妖姬', 'leblanc', 0.508], ['不祥之刃', 'katarina',]]
    #
    # 出装 = txt[weizhi][champin]['装备']
    #{'核心出装': [[[['幽梦之魂', '黑色切割者', '死亡之舞'], ['31.08%', '59.61%']], [['幽梦之魂', '黑色切割

all_weizhi  = txt.keys()
my_team = {}
enmies_team = {}
time.sleep(3)
im = pyautogui.screenshot(region=(260,400,1410,50))
im.save('my.png')
im = pyautogui.screenshot(region=(260,935,1410,50))
im.save('en.png')
m1 = shibie('my.png')
m2 = shibie('en.png')
while  len(m1) < 5:
    m1.append(input('请输入上方缺少的英雄'))
while len(m2) < 5:
    m2.append(input('请输入下方缺少的英雄'))
res ={'1':'上单',
    '2':'打野',
    '3':'中单',
    '4':'下路',
    '5':'辅助',
    }
for m in m1 :
    re = input(f'请输入{m}的位置:(1-5表示从上单到辅助)')
    if re in res.keys():
        my_team[res[re]]=m

for m in m2 :
    re = input(f'请输入{m}的位置:(1-5表示从上单到辅助)')
    if re in res.keys():
        enmies_team[res[re]] = m

def get_data(my_team):
    mt = []
    for weizhi,champing in my_team.items():
        try:
            t = txt[weizhi][champing]
            mt.append(t)
        except Exception as e :
            print(e)
            t = txt[weizhi][input('请从新输入:')]
            mt.append(t)
    return mt
mt = get_data(my_team)
et = get_data(enmies_team)

def get_arg(teamlist0,teamlist1):
    quxians = [[],[],[],[],[]]
    for i in teamlist0:
        quxians[0].append(float(i['曲线'][0]))
        quxians[1].append(float(i['曲线'][1]))
        quxians[2].append(float(i['曲线'][2]))
        quxians[3].append(float(i['曲线'][3]))
        quxians[4].append(float(i['曲线'][4]))
    myarg = get_arg_oneteam(quxians)
    #print('上方曲线:')
    #print(myarg)
    quxians = [[],[],[],[],[]]
    for i in teamlist1:
        quxians[0].append(float(i['曲线'][0]))
        quxians[1].append(float(i['曲线'][1]))
        quxians[2].append(float(i['曲线'][2]))
        quxians[3].append(float(i['曲线'][3]))
        quxians[4].append(float(i['曲线'][4]))
    enarg = get_arg_oneteam(quxians)
    #print('下方曲线:')
    #print(enarg)
    return [round((myarg[0]/(myarg[0]+enarg[0])*100),2),round((myarg[1]/(myarg[1]+enarg[1])*100),2),
            round((myarg[2]/(myarg[2]+enarg[2])*100),2),round((myarg[3]/(myarg[3]+enarg[3])*100),2),round
            ((myarg[4]/(myarg[4]+enarg[4])*100),2)]
sss = []
for weizhi,champin in my_team.items():
    try:
        克制 = txt[weizhi][champin]['克制']
        for listss in 克制:
            try:
                if listss[0] == enmies_team[weizhi]:
                    # print(weizhi,listss[2])
                    sss.append(listss[1])
            except:
                pass
    except :
        pass

asss = get_Average(sss)

bsss =(get_arg(mt,et))
csss = []
c = 0
for b in bsss:
    c +=1
    if c <3:
        bs = ((b*2)*asss)
    elif c == 3:
        bs = ((b*4-100)*asss)
    elif c == 4:
        bs = ((b*8-300)*asss)
    elif c == 5:
        bs = (b*8-350)
    csss.append(round(bs,2))
print('克制指数为:',asss)
print('上方胜率为:')
print(' 0-25 , 25-30, 30-35, 35-40, 40+ ')
print(csss)
