#-*- codeing = utf-8 -*-
# coding=gbk
#@Time : 2020/7/8 0:02
#@Author : ³��Դ
#@File : ��ȡ.py
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



    # �ٻ�ʦ����1 = txt[weizhi][champin]['�ٻ�ʦ����']
    # #[[['Flash', 'Dot'], ['94.05%', '49.61%']], [['Teleport', 'Flash'], ['5.29%', '50.21%']]]
    #
    # ���� = txt[weizhi][champin]['����']
    # #[['Q', 'W', 'E', 'Q', 'Q', 'R', 'Q', 'E', 'Q', 'E', 'R', 'E', 'E', 'W', 'W'], ['58.76%', '62.5%']]
    # ���� = txt[weizhi][champin]['����']
    # #[['Ӱ��֮��', 'zed', 0.5055], ['���罣��', 'yasuo', 0.5275], ['���ƴ�ʦ', 'twistedfate', 0.4974], ['������', 'sylas', 0.5039], ['��������', 'leblanc', 0.508], ['����֮��', 'katarina',]]
    #
    # ��װ = txt[weizhi][champin]['װ��']
    #{'���ĳ�װ': [[[['����֮��', '��ɫ�и���', '����֮��'], ['31.08%', '59.61%']], [['����֮��', '��ɫ�и�

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
    m1.append(input('�������Ϸ�ȱ�ٵ�Ӣ��'))
while len(m2) < 5:
    m2.append(input('�������·�ȱ�ٵ�Ӣ��'))
res ={'1':'�ϵ�',
    '2':'��Ұ',
    '3':'�е�',
    '4':'��·',
    '5':'����',
    }
for m in m1 :
    re = input(f'������{m}��λ��:(1-5��ʾ���ϵ�������)')
    if re in res.keys():
        my_team[res[re]]=m

for m in m2 :
    re = input(f'������{m}��λ��:(1-5��ʾ���ϵ�������)')
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
            t = txt[weizhi][input('���������:')]
            mt.append(t)
    return mt
mt = get_data(my_team)
et = get_data(enmies_team)

def get_arg(teamlist0,teamlist1):
    quxians = [[],[],[],[],[]]
    for i in teamlist0:
        quxians[0].append(float(i['����'][0]))
        quxians[1].append(float(i['����'][1]))
        quxians[2].append(float(i['����'][2]))
        quxians[3].append(float(i['����'][3]))
        quxians[4].append(float(i['����'][4]))
    myarg = get_arg_oneteam(quxians)
    #print('�Ϸ�����:')
    #print(myarg)
    quxians = [[],[],[],[],[]]
    for i in teamlist1:
        quxians[0].append(float(i['����'][0]))
        quxians[1].append(float(i['����'][1]))
        quxians[2].append(float(i['����'][2]))
        quxians[3].append(float(i['����'][3]))
        quxians[4].append(float(i['����'][4]))
    enarg = get_arg_oneteam(quxians)
    #print('�·�����:')
    #print(enarg)
    return [round((myarg[0]/(myarg[0]+enarg[0])*100),2),round((myarg[1]/(myarg[1]+enarg[1])*100),2),
            round((myarg[2]/(myarg[2]+enarg[2])*100),2),round((myarg[3]/(myarg[3]+enarg[3])*100),2),round
            ((myarg[4]/(myarg[4]+enarg[4])*100),2)]
sss = []
for weizhi,champin in my_team.items():
    try:
        ���� = txt[weizhi][champin]['����']
        for listss in ����:
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
print('����ָ��Ϊ:',asss)
print('�Ϸ�ʤ��Ϊ:')
print(' 0-25 , 25-30, 30-35, 35-40, 40+ ')
print(csss)
