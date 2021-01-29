'''
Author: wang
Date: 2021-01-29 12:50:31
LastEditTime: 2021-01-29 17:43:48
LastEditors: Please set LastEditors
Description: wang
FilePath: \Desktopd:\.git\vscode\yundongyuanguanlixitong\main.py
'''
################import######################
import json
############################################
def judge(r):
    try:
        r = float(r)
    except :
        r = input('格式错误，请重新输入：')
        judge(r)
        return r
    return r
def 录入(name, all_result):
    result = {}
    while True:
        t = input('球员类型（1,2）：')
        if t =="1":
            result['球员类型'] = '球员'
            xm = xiangmu[0]
            break
        elif t =="2":
            result['球员类型'] = '守门员'
            xm = xiangmu[1]
            break
        else:
            print('格式错误，请重新输入！')
        
    
    for x in xm:
        r = input(f'请输入项目“{x}”的成绩：')
        judge(r)
        result[x] = r
    all_result[name] = result


def 修改(name, all_result):
    try:
        result = all_result[name]
    except:
        name = input('查无此人，请重新输入')
        修改(name,all_result)
        return
    
    play_type = result['球员类型']
    if play_type =="球员":
        xm = xiangmu[0]
    elif play_type=="守门员":
        xm = xiangmu[1]
    
    t = 0
    for k,v in result.items():
        t+=1
        print(t,k,v)

    x = input('请输入要修改的项目编号：')
    """ def judge_cout(x):
        try: 
            x = int(x)
            if 0<x<17:
                return x
            else:
                x = input("请重新输入正确编号：")
                judge_cout(x)
                return x
        except :
            x = input("请重新输入正确编号：")
            judge_cout(x)
            return x """
    try:
        if x == "1":
            if result['球员类型'] == '球员':
                result['球员类型'] =='守门员'
            else:
                result['球员类型'] == '球员'  
        else:
            x = int(x)
            x_key = xm[x]
    except :
        print('请按照格式从新输入')
        修改(name, all_result)
        return
    #x = judge_cout(x)
    
    r = input('请输入要修改的值:')
    judge(r)
    result[x_key] = r


def 删除(name, all_result):
    all_result.pop(name)
    print(all_result)

xiangmu = [['八字滑行（不带球）（秒）', '八字滑行（带球）（秒）', '射门', "6圈（分钟）", '折线滑（秒）', '握力器（左）',
    '握力器（右）', '曲臂悬挂', '仰卧起坐', '引体向上', '模拟滑行'],['十字（秒）', '三点（秒）', '传球', '侧躺（30°）','握力器','躺举杠铃','引体向上','仰卧起坐','曲臂悬挂','模拟滑行']
]
def main():
    try:
        with open('data.txt','r') as t:
            all_result = json.loads(t.read())
    except:
        all_result={}
    
    while True:
        x = input('增，改，删')
        
        if x =="1" :
            name = input('名字')
            print(1)
            录入(name, all_result)
        elif x =="2":
            name = input('名字')
            修改(name, all_result)
        elif x=="3":
            name = input('名字')
            删除(name, all_result)
        else:
            exit()
        with open('data.txt','w') as t:
            a = json.dumps(all_result)
            t.write(a)
    #name = input("请输入姓名")
    
    #

    """ all_result = {
        'd': {
            '八字滑行（不带球）（秒）': '1',
            '八字滑行（带球）（秒）': '12',
            '射门': '13',
            '6圈（分钟）': '14',
            '折线滑（秒）': '15',
            '躺举杠铃': '16',
            '握力器（左）': '17',
            '握力器（右）': '18',
            '曲臂悬挂': '19',
            '仰卧起坐': '20',
            '引体向上': '21',
            '模拟滑行': '22',
            '十字（秒）': '23',
            '三点（秒）': '24',
            '传球': '25',
            '侧躺（30°）': '26'
        }
    } """
    #录入(name, all_result)
    #修改(name, all_result)
    #删除(name, all_result)
    #print(all_result)
    



main()